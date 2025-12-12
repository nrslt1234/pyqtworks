class Cars:
    def __init__(self, color, speeed, mark):
        self.mark = mark
        self.speeed = speeed
        self.color = color

    def go_machine(self):
        return  "Запуск двигателя"

class Truck(Cars):
    def __init__(self, color, speeed, mark, container):
        super().__init__(color, speeed, mark)
        self.container = container
    def go_machine(self):
        return super().go_machine() + " у грузовика"

pickup = Truck("red", "50", "BMW", "Steel")
print(pickup.go_machine())


my_car = Cars("red", "50", "BMW")

class Sport_car(Cars):
    def __init__(self, color, speeed, mark):
        super().__init__(color, speeed, mark)


    def go_machine(self):
        return super().go_machine() + " у спортивной машины"

    def test(self):
        print("hhff")
sport = Sport_car("blue", "150","BMW" )

print(sport.go_machine())

class Super_Pickup(Truck, Sport_car):
    def __init__(self, color, speeed, mark, container):
        super().__init__(color, speeed, mark, container)


super_truck = Super_Pickup("red", "50", "BMW", "Steel")

super_truck.test()

list_1 = [pickup, super_truck, my_car]

for i in list_1:
    print(i.go_machine())