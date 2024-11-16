# rasPyCNCController
# Copyright 2016 Francesco Santini <francesco.santini@gmail.com>
#
# This file is part of rasPyCNCController.
#
# rasPyCNCController is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasPyCNCController is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasPyCNCController.  If not, see <http://www.gnu.org/licenses/>.

from PySide2.QtCore import QThread, Signal
import re
import sys
import time
from PySide2.QtWidgets import QApplication, QMessageBox

from gcode.GrblWriter import showGrblErrorMessageBox


def truncateGCode(gcode):
    def replace(match):
        match = match.group(2)
        return "." + match[0:4]

    pattern = re.compile(r"([.])([0-9]+)")
    return re.sub(pattern, replace, gcode)

class GCodeRunner(QThread):

    error_event = Signal(object)
    progress_event = Signal(object)
    stop_event = Signal()
    pause_event = Signal(object)
    end_event = Signal()


    def __init__(self):
        QThread.__init__(self)
        self.grblWriter = None
        self.gcode = None
        self.stopFlag = False
        self.pauseFlag = False
        self.currentLine = 0
        self.waitForPause = False
        self.errorStatus = False

    def setGrbl(self, grblWriter):
        self.grblWriter = grblWriter
        self.grblWriter.grbl_error.connect(self.grblError)

    def grblError(self, errorMsg):
        self.errorStatus = True
        if not showGrblErrorMessageBox(None, self.currentLine, self.gcode[self.currentLine], errorMsg):
            self.stopFlag = True
        self.errorStatus = False


    def setGcode(self, gcode):
        self.gcode = gcode
        self.currentLine = 0

    def resume(self):
        if not self.pauseFlag:
            return

        self.pauseFlag = False
        self.waitForPause = False
        self.grblWriter.resume_pos()
        self.pause_event.emit(False)

    def pause(self):
        if self.waitForPause or self.pauseFlag:
            return

        self.pauseFlag = True
        self.waitForPause = True # this flag is on when pause was requested, but grbl hasn't cleared the queue yet

    def stop(self):
        self.stopFlag = True

    def run(self):
        totLines = len(self.gcode)

        if self.grblWriter == None or self.gcode == None: return
        self.pauseFlag = False
        self.stopFlag = False

        # make sure we are in absolute positioning when we start. Should be necessary because the gcode file should do it already.
        self.grblWriter.do_command("G90")
        self.grblWriter.do_command("G21")

        errorStatus = False

        while self.currentLine < totLines:

            QApplication.processEvents()

            if (self.stopFlag):
                self.grblWriter.close()
                self.stop_event.emit()
                return

            ack, lineIn = self.grblWriter.ack_received()

            if self.errorStatus or (lineIn is not None and ('ALARM' in lineIn or 'error' in lineIn)):
                time.sleep(0.01)
                # this will be handled by the event
                continue

            if not ack:
                time.sleep(0.01)
                continue

            # check for pause is after check for ack, so we are sure that GRBL is in sync
            if (self.pauseFlag):
                if self.waitForPause:
                    self.waitForPause = False # now pause code is being processed
                    # emit an event when the gcode has picked up with the pause
                    self.grblWriter.store_pos()
                    self.pause_event.emit(True)
                # idle loop during pause
                time.sleep(0.1)
                continue

            line = truncateGCode(self.gcode[self.currentLine])
            if "@pause" in line:
                self.currentLine += 1
                self.pause()
                continue

            try:
                self.grblWriter.do_command_nonblock(line)
                self.currentLine += 1
                self.progress_event.emit(self.currentLine)
            except:
                e = sys.exc_info()[0]
                self.error_event.emit("%s" % e)

        print("File finished. Waiting for last ack")
        # wait for the last ack
        while True:
            ack, lineIn = self.grblWriter.ack_received()
            if ack:
                break
            time.sleep(0.01)

        print("Waiting for motion to finish")
        #self.grblWriter.wait_motion()
        self.grblWriter.wait_motion_nonblock()
        while True:
            ack, lineIn = self.grblWriter.ack_received()
            if ack:
                break
            if self.stopFlag:
                self.grblWriter.reset()
                self.stop_event.emit()
                return
            time.sleep(0.1)
        self.end_event.emit()

