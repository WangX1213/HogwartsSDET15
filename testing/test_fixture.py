

# @pytest.mark.usefixtures()
def test_case1(login):
    print(login)
    print("用例1")

def test_case2():
    print("用例2")

def test_case3(conn_db,login):
    print(login)
    print(conn_db)
    print("用例3")
