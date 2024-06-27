from watch import parse

def test_https():
    assert parse("<iframe src=\"https://youtube.com/embed/xvFZjo5PgG0\"></iframe>") == "https://youtu.be/xvFZjo5PgG0"

def test_http():
    assert parse("<iframe src=\"http://youtube.com/embed/xvFZjo5PgG0\"></iframe>") == "https://youtu.be/xvFZjo5PgG0"

def test_www():
    assert parse("<iframe src=\"https://www.youtube.com/embed/xvFZjo5PgG0\"></iframe>") == "https://youtu.be/xvFZjo5PgG0"

