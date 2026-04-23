''' CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
'''

print("==== ENCAPSULATION ====")
# ENCAPSULATION > public __private _protected


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("----------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

my_account.__owner = "Martin"
my_account.__amount = 10000000
my_account.get_balance()

print("--------------")

# @property decoratori orqali objectdagi private malumotlarni olib ishlatishimiz mumkin
# uni state kabi call qilamiz

try:
    result = my_account.__amount
    print("resuult:", result)
except Exception as err:
    print("No target state found:", err)

# getter & setter
print("owner before:", my_account.holder)  # state
# my_account.change_ownership("Martin")  # method
my_account.holder = "Martin"  # setter
print("account_after:", my_account.holder)
