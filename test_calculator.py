from main import evaluateExpression

# Writing test cases to test the functionality of the app
def test_evaluateExpression():
    assert evaluateExpression("0") == "0"
    assert evaluateExpression("3*3") == "9"
    assert evaluateExpression("5*(55/11+66)/2") ==  "177.5"
    assert evaluateExpression("10000+(543*50/24)+50*40000") =="2011131.25"