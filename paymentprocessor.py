from carddatabase import CardDatabase

class PaymentProcessor:
    def __init__(self):
        self.max_transactions = 5
        self.card_database = CardDatabase()

    def validate_card_number(self, card_number):
        is_valid = True
        
        if not card_number.isdigit():
            is_valid = False

        if len(card_number) != 16:
            is_valid = False

        if not card_number.startswith("4"):
            is_valid = False

        return is_valid
    
    def check_balance(self, credit_card):
        if not self.card_database.check_credit_card_in_database(credit_card):
            print("Card does not exists in database")
            return False
        
        print(f"The credit card has a balance of {self.card_database.check_balance(credit_card)}" )

        return True
    
    def add_balance(self, credit_card, balance):
        if len(balance) < 0:
            print("balance has to be greater than zero")
            return False
        
        if not self.card_database.check_credit_card_in_database(credit_card):
            print("Credit card does not exist in the database")
            return False

        return
        
        
