import sys, math
from PyQt5 import QtCore, QtGui, QtWidgets
import ezdxf

t = 10
w = 300
wn =5
hwanted = 80
h =hwanted+2*t
hn =5
d = 0
dn =0
MajorMirror = 0
Length = w
Number = 5
XMajor = 0
global poly
poly = 0

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0))                      # set lineColor
        self.pen.setWidth(3)                                            # set lineWidth
        self.brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))        # set fillColor
        self.polygon = self.createPoly()                         # polygon with n points, radius, angle of the first point



    def createPoly(self):
        if poly ==0:
            polygon = QtGui.QPolygonF()
            poly = 1
        if MajorMirror == 1:
            MM = 1
        else:
            MM=-1
        inc = Length/Number
        iter = Number*2
        result=[0]*iter

        for i in range(iter):
            A = (((i)%2)+(i))/2
            B = ((((i-1)%2)+(i-1))/2)%2
            # wx[i] = [A*w_l, B*t*(-1)]
            C = A*inc
            D = B*t*MM
            print("DOING")
            polygon.append(QtCore.QPointF(self.width()/2 +C, self.height()/2 + D))
            print(result)

        return polygon
        if Add == 0:
            return result
        else:
            print("eggs")




    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon(self.polygon)

app = QtWidgets.QApplication(sys.argv)

widget = MyWidget()
widget.show()

sys.exit(app.exec_())
