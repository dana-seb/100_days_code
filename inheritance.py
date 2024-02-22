class Animal:
    def __init__(self):
        self.number_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        print("doing this underwater.")
        super().breathe()
        

    def swim(self):
        print("moving in water.")





amy = Animal()
# print(amy.number_eyes)
# amy.breathe()
timmy = Fish()
timmy.breathe()