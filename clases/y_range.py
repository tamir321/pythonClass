class Yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return f"this is item {self.i-1}"
        else:
            raise StopIteration()

blabla = Yrange(10)
for i in blabla:
    print(i)

print(list(blabla))

def gen(n):
    print("start generate items")
    for i in range(n + 1):
        print(i)
        yield i
        print("back from yield")
    print("~*" * 20)


# print(sum(gen(10)))
# print((1+10)*(10/2))