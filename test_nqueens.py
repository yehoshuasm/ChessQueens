from queens import NQueens

def test_n_2():
    nqueens = NQueens(2, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 0

def test_n_3():
    nqueens = NQueens(3, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 0

def test_n_4():
    nqueens = NQueens(4, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 2

def test_n_5():
    nqueens = NQueens(5, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 10

def test_n_6():
    nqueens = NQueens(6, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 4

def test_n_7():
    nqueens = NQueens(7, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 40

def test_n_8():
    nqueens = NQueens(8, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 92

def test_n_9():
    nqueens = NQueens(9, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 352

def test_n_10():
    nqueens = NQueens(10, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 724

def test_n_11():
    nqueens = NQueens(11, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 2680

def test_n_12():
    nqueens = NQueens(12, None, False)
    nqueens.solve()
    assert nqueens.numberOfSolutions == 14200