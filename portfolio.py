from database import Database


class Portfolio:
    def __init__(self):
        db = Database()
        db.connect()


p = Portfolio()
print("success!")
