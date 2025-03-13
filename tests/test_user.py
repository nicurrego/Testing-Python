import unittest
from faker import Faker
from src.bank_account import BankAccount
from src.user import User

class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale="en")

    def test_user_creation(self):
        generated_name = self.faker.name()
        generated_email = self.faker.email()
        user = User(generated_name, generated_email)
        self.assertEqual(user.name, generated_name)
        self.assertEqual(user.email, generated_email)

    def test_user_with_multiple_accounts(self):
        user = User(self.faker.name(), self.faker.email())

        for _ in range(3):
            bank_account = BankAccount(
                self.faker.random_int(min=100, max=2000, step=50)
            )
            user.add_account(bank_account)

        expected_value = user.get_total_balance()
        value = sum(bank_account.get_balance() for bank_account in user.accounts)
        self.assertEqual(expected_value, value)