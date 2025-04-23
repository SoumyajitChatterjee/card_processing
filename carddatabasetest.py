import unittest
from carddatabase import CardDatabase

class CardDatabaseTest(unittest.TestCase):

    def setUp(self):
        self.database = CardDatabase()

    def test_add_credit_card_non_numeric_reject(self):
        result = self.database.add_credit_card("Wnner")
        self.assertEqual(result, False)
        print(self.database)

    def test_remove_credit_card_non_existent_reject(self):
        self.database.add_credit_card("12345")
        result = self.database.remove_credit_card("12345")
        self.assertEqual(result, False)
        print(self.database)


if __name__ == "__main__":
    unittest.main()