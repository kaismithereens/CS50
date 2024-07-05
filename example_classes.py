class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self. weight = weight

def main():

    #packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charley, 5kg]
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charley", weight=5)
        ]
    print(packages)

main()

