import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)

        def feed(self):
            self.hunger -= 1
            print(f"{self.name} відчувається насиченим.")

        def play(self):
            self.happiness += 1
            print(f"{self.name} радіє грі.")

        def status(self):
            print(f"{self.name}: Голод - {self.hunger}, Щастя - {self.happiness}")
if __name__ == "__main__":
    my_pet = Pet("Багіра", "Кіт")

    my_pet.status()

    my_pet.feed()

    my_pet.play()

    my_pet.status()