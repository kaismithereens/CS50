"""
Open your test_jar.py file and import your Jar class with from jar import Jar.
Create a function called test_init, wherein you create a new instance of Jar with jar = Jar().
assert that this jar has the capacity it should, then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_str.
In test_str, create a new instance of your Jar class and deposit a few cookies.
assert that str(jar) prints out as many cookies as have been deposited, then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_deposit.
In test_deposit, create a new instance of your Jar class and deposit a few cookies.
assert that the jar’s size attribute is as large as the number of cookies that have been deposited.
Also assert that, if you deposit more than the jar’s capacity, deposit should raise a ValueError.
Run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_withdraw.
In test_withdraw, create a new instance of your Jar class and first deposit a few cookies.
assert that withdrawing from the jar leaves the appropriate number of cookies in the jar’s size attribute.
Also assert that, if you withdraw more than the jar’s size, withdraw should raise a ValueError.
Run your tests with pytest test_jar.py.
"""
import pytest
from jar import Jar

#test default capaacity
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

#test set capacity
def test_init2():
    jar2 = Jar()
    jar2 = Jar(capacity = 1)
    assert jar2.capacity == 1

#test str method prints out correct value after deposit
def test_str_after_deposit():
    jar = Jar()
    jar.deposit(10)
    assert str(jar) == "🍪" * 10

#test str method prints out correct value before deposit
def test_empty_str():
    jar = Jar()
    assert str(jar) == ""

#test deposit method deposits correct amount of cookies
def test_deposit():
    jar = Jar()
    assert jar.deposit(3) == 3

#test deposit method raises Value Error if deposit value exceeds the jar capacity
def test_deposit_too_many():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

#test withdraw method displays correct value
def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

#test withdraw method raises ValueError when there aren't enogh cookies in the jar
def test_withdraw_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)

def test_empty_jar():
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0
    assert str(jar) == ""





