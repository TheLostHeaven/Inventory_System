from models.supplies import Supplies as SuppliesModel



class SuppliesService():
    def __init__(self, db):
        self.db = db

    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result


