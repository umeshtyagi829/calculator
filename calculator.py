"""It is simple calculator built using Python and PyQt5."""

# Import QApplication and the required widgets from PyQt5.QtWidgets
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *

ERROR_MSG = 'ERROR'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
   
    def __init__(self):
        """View initializer."""
        super().__init__()
        # setting font
        self.setFont(QFont('Times', 15))
        # setting title for app
        self.setWindowTitle("Calculator")
        self.setFixedSize(235, 235)
        # setting central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        font = self.display.font()
        font.setPointSize(30)
        self.display.setFont(font)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "X": (0, 3), "C": (0, 4), "/": (0, 5),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "(": (1, 3), "*": (1, 4),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), ")": (2, 3), "-": (2, 4),
            "0": (3, 0), "00": (3, 1),".": (3, 2), "+": (3, 3), 
        }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        #creating equal push button
        self.push_equal = QPushButton("=", self) 
        self.push_equal.setFixedSize(80,40)
        buttonsLayout.addWidget(self.push_equal, 3,4)

        #creating push multiply push button
        self.push_mul = QPushButton("*", self) 
        self.push_mul.setFixedSize(80,40)
        buttonsLayout.addWidget(self.push_mul, 1,4)
        #creating minus push button
        self.push_minus = QPushButton("-", self) 
        self.push_minus.setFixedSize(80,40)
        buttonsLayout.addWidget(self.push_minus, 2,4)
        
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()
    
    def delSingleDigit(self):
        # clearing a single digit
        text = self.display.text()
        self.display.setText(text[:len(text)-1])

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")


# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'X'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.push_equal.clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['X'].clicked.connect(self._view.delSingleDigit)
