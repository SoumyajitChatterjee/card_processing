class CardDatabase:
    def __init__(self):
        self.__database = {}
    
    def add_credit_card(self, credit_card):

        if not credit_card.isnumeric():
            print("Card is not numeric")
            return False

        if credit_card in self.__database:
            print("credit card already in database")
            return False
        else:
            self.__database[credit_card] = {"transactions" : 0, "balance": 0}
            print("credit card has been inserted into database")
            return True

    def remove_credit_card(self, credit_card):
        if credit_card not in self.__database:
            print("credit does not exist in database")
            return False
        else:
            self.__database.pop(credit_card)
            print("credit card has been successfully removed from database")
            return True
        
    def show_database(self):
        for credit_card, details in self.__database.items():
            print(f"Credit_Crad : {credit_card}")
            for key in details.keys():
                print(f"{key} is {details[key]} ")
        return 
    
    def check_credit_card_in_database(self, credit_card):
        return credit_card in self.__database
    
    def check_balance(self, credit_card):
        return self.__database.get(credit_card, {}).get("balance", 0)
    
    




