import unittest , os
import unittest.mock
from unittest.mock import patch
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000, log_file='accountLog.txt')
        self.account2 = BankAccount(1000)

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self,):
        withdrawed = self.account.withdraw(500)
        assert withdrawed == 500

    @patch("src.bank_account.datetime")
    def test_withdraw_fail_before_services_hour(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7

        with self.assertRaises(Exception):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_fail_after_services_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18

        with self.assertRaises(Exception):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_fail_saturday_services_hour(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 5
        mock_datetime.now.return_value.hour = 10

        with self.assertRaises(Exception):
            self.account.withdraw(100)

    def test_get_balance(self):
        balance = self.account.get_balance()
        assert balance == 1000

    def test_transfer(self):
        transfer = self.account.transfer(100, self.account2)
        assert transfer
        account = BankAccount(1200)

    def test_transfer_insufiicent_balance(self):
        with self.assertRaises(ValueError):
            self.account.transfer(1001, self.account2)
    
    def test_count_lines(self):
        assert self.count_lines(self.account.log_file) == 1
        self.account.deposit(200)
        assert self.count_lines(self.account.log_file) == 2

    def test_deposit_different_deposit_amounts(self):

        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 200, "expected": 1200},
            {"amount": 300, "expected": 1300},
            {"amount": 400, "expected": 1400},
            {"amount": 500, "expected": 1500},
        ]

        for case in test_cases:
            self.setUp()
            with self.subTest(case):
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])