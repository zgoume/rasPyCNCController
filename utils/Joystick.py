from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys


class Joystick(QWidget):

    joyChanged = Signal()
    joyReleased = Signal()

    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        # self.setFixedSize(400, 400)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistanceX = 200
        self.__maxDistanceY = 200
        self.__valueRange = 10
        self.__x = 0
        self.__y = 0
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def heightForWidth(self, width):
        return self.width()
    
    def resizeEvent(self, event):

        # Récupérer la largeur et la hauteur disponibles
        new_size = min(self.width(), self.height())

        # Appliquer une taille carrée
        self.resize(new_size, new_size)

        # Appeler l'événement parent pour gérer le comportement standard
        super().resizeEvent(event)
        
        self.__maxDistanceX = int(self.width() / 2)
        self.__maxDistanceY = int(self.height() / 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width()
        height = self.height()
        bounds = QRectF(0, 0, (width - 1), (height - 1))
        painter.setPen(Qt.green)
        painter.drawRect(bounds)
        painter.setBrush(Qt.green)
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

        if (relX > self.__maxDistanceX):
            limitLine.setP2(QPointF(limitLine.x1() + self.__maxDistanceX, limitLine.y2()))
        elif (relX < -self.__maxDistanceX):
            limitLine.setP2(QPointF(limitLine.x1() - self.__maxDistanceX, limitLine.y2()))


        if (relY > self.__maxDistanceY):
            limitLine.setP2(QPointF(limitLine.x2(), limitLine.y1() + self.__maxDistanceY))
        elif (relY < -self.__maxDistanceY):
            limitLine.setP2(QPointF(limitLine.x2(), limitLine.y1() - self.__maxDistanceY))

        # if (limitLine.length() > self.__maxDistance):
        #      limitLine.setLength(self.__maxDistance)

        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        
        valX = int(((normVector.x2() - normVector.x1()) * self.__valueRange) / self.__maxDistanceX)
        valY = int(((normVector.y2() - normVector.y1()) * self.__valueRange) / self.__maxDistanceY)

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