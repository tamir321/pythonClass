class MyCars:
    def __init__(self,*my_cars):
        self.my_cars = list(my_cars)
        self._i = 0

    def add_car(self,car_name):
        self.my_cars.append(car_name)

    def remove_car(self,car_name):
        self.my_cars.remove(car_name)




    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self.my_cars):
            self._i +=1
            return self.my_cars[self._i-1]
        else:
            raise StopIteration


my_cars = MyCars("test1","test2","test3","test4","test5","test6","test7")

#print("list(my_cars)",list(my_cars))
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)
a = my_cars.__next__()
print(a)