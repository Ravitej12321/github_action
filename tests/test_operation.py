from src.math_operation import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_subtract():
    assert subtract(4,3)==1
    assert subtract(-2,0)==-2
    