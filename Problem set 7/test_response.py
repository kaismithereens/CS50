from response import check_email

def test_positive1():
    assert check_email("tea@gmail.com") == "Valid"

def test_positive2():
    assert check_email("malan@harvard.edu") == "Valid"

def test_positive3():
    assert check_email("sysadmins@cs50.harvard.edu") == "Valid"

def test_negative1():
    assert check_email("malan@@@harvard.edu") == "Invalid"

def test_negative2():
    assert check_email("tea..@gmail.com") == "Invalid"

def test_negative3():
    assert check_email("malan at harvard dot edu") == "Invalid"

