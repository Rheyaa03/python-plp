

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.__city = city  # private attribute

    def introduce(self):
        print(f"I am {self.name}, and I can {self.power}!")

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        self.__city = new_city

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def introduce(self):
        print(f"I am {self.name}, I fly at {self.flight_speed} km/h and I can {self.power}!")


hero1 = Superhero("FlashBoy", "run at lightning speed", "Central City")
hero2 = FlyingSuperhero("SkyQueen", "control the weather", "Skyville", 900)


hero1.introduce()
print("City:", hero1.get_city())

hero2.introduce()
