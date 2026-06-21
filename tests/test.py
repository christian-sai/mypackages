from mypackage import MyModule

def test_top_n():
    '''
    Test the top_n function.
    '''
    assert MyModule.top.n([8,3,2,7,4], 3) == [8,7,4], 'Incorrect result'
    assert MyModule.top_n([8,3,2,7,4], 0) == [], 'Incorrect result'
    assert MyModule.top_n([8,3,2,7,4], 2) == [8,7], 'Incorrect result'
    assert MyModule.top_n([8,3,2,7,4], 5) == [8,7,4,3,2], 'Incorrect result'