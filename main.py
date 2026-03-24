class Flower:
    def __init__(self, name: str, petals: int, color: str, height: int):
        self.name = name
        self.petals = petals
        self.color = color
        self.height = height

    def describe(self):
        print(f"{self.name} is {self.color}, has {self.petals} petals, and is {self.height} cm tall")

    def grow(self):
        self.height += 1

def main():
    flower1 = Flower("Rose", 40, "red", 10)
    flower2 = Flower("Lily", 10, "orange", 7)
    flower3 = Flower("Violet", 9, "blue", 8)
    flower4 = Flower("Daisy", 12, "white", 5)

    garden = [flower1, flower2, flower3, flower4]

    print("Before growth:")
    for flower in garden:
        flower.describe()
        print()

    for flower in garden:
        flower.grow()
        print()

    print("After growth:")
    for flower in garden:
        flower.describe()
        print()



if __name__ == "__main__":
    main()



