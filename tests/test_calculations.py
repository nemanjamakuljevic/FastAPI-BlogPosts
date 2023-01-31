#simple automated test
import pytest
from app.calculations import add, subtract, multiply, devide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

#adding fixtures in order to minimize repetitive code

@pytest.fixture
def bank_account():
    return BankAccount(200)

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 10, 20),
    (22, 22, 44),
    (15, 16, 31)
])
def test_add(num1, num2, expected):
    print("testing add ffunc") # print() is not listed by default, adding -s into pytest will show print()
    #assert = true test will pass / = false test will throw an error
    assert add(num1, num2) == expected

def test_substract():
    assert subtract(4,2) == 2

def test_multiply():
    assert multiply(6,6) == 36

def test_devide():
    assert devide(100,25) == 4


def test_bank_set_inital_amount(bank_account):
   assert bank_account.balance == 200

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(45)
    assert bank_account.balance == 155

def test_deposit(bank_account):
    bank_account.deposit(45)
    assert bank_account.balance == 245

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 220

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (500, 100, 400),
    (15000, 5000, 10000)
])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected ):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(7000)