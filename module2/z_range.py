class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Zrange_iter(self.n)


class Zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n


    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i - 1
        else:
            raise StopIteration()


blabla = Zrange(10)
for i in blabla:
    print(i)

print("list(blabla)",list(blabla))
print("list(blabla)",list(blabla))
print("list(blabla)",list(blabla))