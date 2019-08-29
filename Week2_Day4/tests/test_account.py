from unittest import TestCase
import os
from app.account import Account

Account.filepath = "test.json"

class TestAccount(TestCase):

    def setUp(self):
        if os.path.exists(Account.filepath):
            os.unlink(Account.filepath)
        greg = Account("Greg")
        greg.balance = 10.50
        greg.pin = "1234"
        greg.save()

    def testLogin(self):
        greg = Account.login("Greg", "1234")
        self.assertIsNotNone(greg)
        self.assertIsInstance(greg, Account)

    def testWithdraw(self):
        greg = Account("Greg")
        greg.balance = 5002.00
        greg.withdraw(5000.00)
        self.assertEqual(greg.balance, 2.00)

    def testDeposit(self):
        greg = Account("Greg")
        greg.balance = 5002.00
        greg.deposit(5000.00)
        self.assertEqual(greg.balance, 10002.00)

    def testLoad(self):
        greg = Account("Greg")
        self.assertEqual(greg.pin, "1234")

    def testSave(self):
        greg = Account("Greg")
        greg.balance = 10000.90
        greg.save()
        newgreg = Account("Greg")
        self.assertEqual(newgreg.balance, 10000.90)

    def tearDown(self):
        pass
