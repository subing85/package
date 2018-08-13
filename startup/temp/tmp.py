from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
 
app = QApplication(sys.argv)
 
style = """QSlider::groove:horizontal {
border: 1px solid #999999;
height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
}
"""
 
slider = QSlider()
slider.setOrientation(Qt.Horizontal)
slider.setStyleSheet(style)
 
layout = QVBoxLayout()
layout.addWidget(slider)

widget = QWidget()
widget.setLayout(layout)
widget.show()
 
app.exec_()