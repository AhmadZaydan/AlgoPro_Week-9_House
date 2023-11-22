class House:
    """A simple house class"""

    total_house = 0  # Keep track of the total number of houses

    def __init__(self, floors, doors, windows, color="white", has_garage=False, address=""):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        # Increment
        House.total_house +=1

    def displayInfo(self):
        '''Displays attribute information of the house object'''
        print("House Information:")
        print(f"     -Address: {self.address}")
        print(f"     -Floors: {self.floors}")
        print(f"     -Doors: {self.doors}")
        print(f"     -Windows: {self.windows}")
        print(f"     -Color: {self.color}")
        print(f"     -Has Garage: {self.has_garage}")

    @classmethod
    def display_total_houses(cls):
        print(f"Total number of houses = {cls.total_house}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False    # Not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False    # Floors, Doors, Windows should all be positive integers

        return True
    
    # Change the color of the house
    def paint_house(self):
        newColor = str(input("Enter new color: "))
        self.color = newColor

        return self.color
    
    # Add garage
    def add_garage(self):
        if self.has_garage == True:
            print("Already have garage")
        else:
            print("Garage added")
            self.has_garage = True

        return self.has_garage
    
    # Change the address
    def set_address(self):
        new_address = str(input("Enter new address: "))
        self.address = new_address

        return self.address
    
# Creating intrepeters (objects) of the house class
house1 = House(floors=2, doors=3, windows=2, color="green", has_garage=True, address="123 blue street")
house2 = House(floors=5, doors=4, windows=4,address="11 redreef street")

house1.displayInfo()
print()
house2.displayInfo()
print()
House.display_total_houses()
print()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")
print()

# Change color of house 1
house1.paint_house()
house1.displayInfo()
print()

# Add garage to house 1
house1.add_garage()
print()

# Add garage to house 1
house2.add_garage()
house2.displayInfo()
print()

# Change address of house 2
house2.set_address()
house2.displayInfo()
print()


