from queens import NQueens

def test_n_2():
    nqueens = NQueens(2)
    nqueens.solve()
    assert nqueens.solutions == 0

def test_n_3():
    nqueens = NQueens(3)
    nqueens.solve()
    assert nqueens.solutions == 0

def test_n_4():
    nqueens = NQueens(4)
    nqueens.solve()
    assert nqueens.solutions == 2

def test_n_5():
    nqueens = NQueens(5)
    nqueens.solve()
    assert nqueens.solutions == 10

def test_n_6():
    nqueens = NQueens(6)
    nqueens.solve()
    assert nqueens.solutions == 4

def test_n_7():
    nqueens = NQueens(7)
    nqueens.solve()
    assert nqueens.solutions == 40

def test_n_8():
    nqueens = NQueens(8)
    nqueens.solve()
    assert nqueens.solutions == 92

def test_n_9():
    nqueens = NQueens(9)
    nqueens.solve()
    assert nqueens.solutions == 352

def test_n_10():
    nqueens = NQueens(10)
    nqueens.solve()
    assert nqueens.solutions == 724

def test_n_11():
    nqueens = NQueens(11)
    nqueens.solve()
    assert nqueens.solutions == 2680

def test_n_12():
    nqueens = NQueens(12)
    nqueens.solve()
    assert nqueens.solutions == 14200