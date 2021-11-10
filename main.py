import sys
from calculator import PyCalcUi 
from calculator import PyCalcCtrl
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

ERROR_MSG = 'ERROR'

# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

def main():
    """Main function."""
    # Create an instance(object) of `QApplication`
    pycalc = QApplication([])
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()