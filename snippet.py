class Elevator:
    people_lifted = 0

    def __init__(self, name):
        self.name = name
        self.people_lifted = 0

    def lift(self):
        print(f' {self.name} lifted people')
        self.people_lifted += 1
        Elevator.people_lifted += 1

    def info(self):
        print(f'{self.name} lifted {self.people_lifted} people out of {Elevator.people_lifted}')


Elevator_Sony = Elevator('Sony')
Elevator_Apple = Elevator('Apple')

Elevator_Sony.lift()
Elevator_Sony.lift()
Elevator_Sony.lift()
Elevator_Apple.lift()

print(Elevator_Sony.info())
print(Elevator_Apple.info())