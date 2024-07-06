class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self. weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():

    #packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charley, 5kg]
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charley", weight=5)
        ]
    for package in packages:
        #print(f"Package {package.number} : {package.sender} to {package.recipient}, {package.weight}kg")
        print(f"{package} costs ${package.calculate_cost(cost_per_kg = 2)}")

main()

