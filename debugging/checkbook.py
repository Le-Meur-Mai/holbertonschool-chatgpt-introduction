#!/usr/bin/python3
class Checkbook:
    """
    Fonction principale du programme de gestion de chéquier.

    Elle propose à l'utilisateur un menu interactif pour effectuer les opérations suivantes :
    - déposer de l'argent (deposit)
    - retirer de l'argent (withdraw)
    - consulter le solde actuel (balance)
    - quitter le programme (exit)

    Chaque opération est traitée en fonction de l'entrée utilisateur.
    Si l'utilisateur entre une valeur non numérique lors d'un dépôt ou d'un retrait,
    le programme génère une exception (ValueError) et affiche une trace complète de l'erreur.
    """

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))  # ← crash if invalid
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))  # ← crash if invalid
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()