import random


class Building:
    def __init__(self, floors=0, customers=0):
        while True:
            try:
                self.floors = int(input("How many floors does the building have?\n"))
                break
            except ValueError:
                print("Please enter an integer value.")
        while True:
            try:
                self.customers = int(input("How many customers do you have?\n"))
                break
            except ValueError:
                print("Please enter an integer value.")


class Elevator:
    def __init__(self):
        self.waiting_que = []
        self.finished = []
        self.max_floor = new_building.floors
        self.current_floor = 0
        self.moves = 0
        self.people_in_elevator = []

    def run(self):
        """method to start the elevator"""
        for i in range(0, new_building.customers):
            customer = Customer()
            self.waiting_que.append(customer)

        # print all the customers waiting
        print('===========================================================')
        print('Waiting Queue:')
        for obj in self.waiting_que:
            if obj.starting_floor == obj.destination_floor:
                print(f'**[{obj.starting_floor} - {obj.destination_floor}]')
            else:
                print(f'[{obj.starting_floor} - {obj.destination_floor}]')
        print('===========================================================')
        print('\n')

        while True:
            if self.current_floor > new_building.floors:
                break
            else:
                print(f'Current floor is {self.current_floor}.')
                # using "reversed" method for the list since it doesnt modify the index position upon removing
                for user in reversed(self.waiting_que):
                    if user.starting_floor == user.destination_floor:
                        self.finished.append(user)
                        self.waiting_que.remove(user)
                for user in reversed(self.waiting_que):
                    if user.starting_floor == self.current_floor:
                        self.people_in_elevator.append(user)
                        print(f'Entered The Elevator: [{user.starting_floor} - {user.destination_floor}]')
                        self.waiting_que.remove(user)
                for user_leaving in reversed(self.people_in_elevator):
                    if user_leaving.destination_floor == self.current_floor:
                        print(f'Left The Elevator: [{user_leaving.starting_floor} - {user_leaving.destination_floor}]')
                        self.finished.append(user_leaving)
                        self.people_in_elevator.remove(user_leaving)
            self.current_floor += 1

        self.current_floor = 5

        while True:
            if self.current_floor < 0:
                break
            else:
                print(f'Current floor is {self.current_floor}.')
                # using "reversed" method for the list since it doesnt modify the index position upon removing
                for user_leaving in reversed(self.people_in_elevator):
                    if user_leaving.destination_floor == self.current_floor:
                        print(f'Left The Elevator: [{user_leaving.starting_floor} - {user_leaving.destination_floor}]')
                        self.finished.append(user_leaving)
                        self.people_in_elevator.remove(user_leaving)
            self.current_floor -= 1

        for obj in self.people_in_elevator:
            print(f'Currently Riding: [{obj.starting_floor} - {obj.destination_floor}]')

        for obj in self.finished:
            print(f'Finished: [{obj.starting_floor} - {obj.destination_floor}]')

        for obj in self.waiting_que:
            print(f'Waiting: [{obj.starting_floor} - {obj.destination_floor}]')


class Customer:
    def __init__(self, arrived=False):

        self.starting_floor = random.randint(0, random.randint(0, new_building.floors))
        self.destination_floor = random.randint(0, new_building.floors)
        self.arrived = arrived


if __name__ == "__main__":
    while True:
        start = input('Would you like to start the simulation? Enter y or n\n')
        if start == 'y':
            new_building = Building()
            print(f'The building has {new_building.floors} floors.')
            print(f'You have {new_building.customers} customers.')
            new_elevator = Elevator()
            new_elevator.run()
        else:
            break

