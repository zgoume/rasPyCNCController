from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys
from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QWidget):

    joyChanged = Signal()
    joyReleased = Signal()

    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 100
        self.__valueRange = 10
        self.__x = 0
        self.__y = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())
        painter.drawRect(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        
        relX = (limitLine.x2() - limitLine.x1())
        relY = (limitLine.y2() - limitLine.y1())

        # print("DEBUG x = %f / y = %f" % (relX, relY))

        if (relX > self.__maxDistance):
            limitLine.setP2(QPointF(limitLine.x1() + self.__maxDistance, limitLine.y2()))
        elif (relX < -self.__maxDistance):
            limitLine.setP2(QPointF(limitLine.x1() - self.__maxDistance, limitLine.y2()))


        if (relY > self.__maxDistance):
            limitLine.setP2(QPointF(limitLine.x2(), limitLine.y1() + self.__maxDistance))
        elif (relY < -self.__maxDistance):
            limitLine.setP2(QPointF(limitLine.x2(), limitLine.y1() - self.__maxDistance))

        # if (limitLine.length() > self.__maxDistance):
        #      limitLine.setLength(self.__maxDistance)

        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        
        valX = int(((normVector.x2() - normVector.x1()) * self.__valueRange) / self.__maxDistance)
        valY = int(((normVector.y2() - normVector.y1()) * self.__valueRange) / self.__maxDistance)

        return (valX, valY)

    def setRangeValue(self, value):
        self.__valueRange = value

    def value(self):
        return (self.__x, self.__y)

    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.update()
        self.joyReleased.emit()

    def mouseMoveEvent(self, event):
        if self.grabCenter:
            # print("Moving")

            tempX = self.__x
            tempY = self.__y

            self.movingOffset = self._boundJoystick(event.pos())
            self.__x, self.__y = self.joystickDirection()
            
            self.update()

            if (self.__x != tempX or self.__y != tempY):
                # print("emit")
                self.joyChanged.emit()
        # print(self.joystickDirection())


if __name__ == '__main__':
    # Create main application window
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mw = QMainWindow()
    mw.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    cw = QWidget()
    ml = QGridLayout()
    cw.setLayout(ml)
    mw.setCentralWidget(cw)

    # Create joystick 
    joystick = Joystick()
    joystick.setRangeValue(6)

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
    ml.addWidget(joystick,0,0)

    mw.show()

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()