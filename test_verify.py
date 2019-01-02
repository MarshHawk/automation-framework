import sys
import pytest

def test_passing_no_verify():
    assert 2 == 2
    assert 'black' == 'black'
    assert True == True

def test_failing_no_verfiy():
    assert 3 == 4
    assert 'black' == 'blue'
    assert True == False

def test_passing_verify(verify):
    verify(2, 2)
    verify('black', 'black')
    verify(True, True)

def test_failing_with_verify(verify):
    verify(1, 2)
    verify('black', 'blue')
    verify(True, False)

def test_failing_verify(verify):
    verify(1, 2)
    verify('black', 'blue')
    verify(True, False)

#def test_mixed_pass_fail_first(verify):
def test_mixed_pass_fail_middle(verify):
#def test_mixed_pass_fail_last(verify):
    #assert 2 == 2
    verify(1, 2)
    assert 3 == 4
    verify('black', 'blue')
    #assert True == False