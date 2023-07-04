from db_Trucks import DataBase

class Trucks():
    def __init__(self, number ,name, weight, booking='Свободен'):
        self.name = name
        self.weight = weight
        self.booking = booking
        self.number = number

        self._bd = DataBase()
        self._bd.add_to_db(number, name, weight, booking) 

    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight
    
    def get_number(self):
        return self.number
    
    def can_carry(self, weight_truck):
        if  weight_truck <= self.weight:
            return True 
        else:
            return False
        
    def is_free(self):
        return self.booking
    
    def book_car(self):
        self.booking = 'Занят'
        self._bd.update_free(self.number)
