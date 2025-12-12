class Family_sub_premium:

    days_less = 30

    def __init__(self, name):
        self.name = name

    @staticmethod
    def continue_sub():
        Family_sub_premium.days_less = Family_sub_premium.days_less + 30
        print(Family_sub_premium.days_less)


    # def __str__(self):
    #     return "Аккаунт " + self.name

father = Family_sub_premium("father")
mother = Family_sub_premium("mother")
son = Family_sub_premium("son")

print(father)

father.continue_sub()
Family_sub_premium.continue_sub()

print(father.days_less, mother.days_less, son.days_less)