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

print("list(blabla)",list(blabla))
print("list(blabla)",list(blabla))
"""
That is because the Yrange object is an iterator. 
Iterators are objects that can be used to iterate over a sequence of values. 
When you iterate over an iterator, the iterator will return the next value in the sequence each time.

The list() function takes an iterator as an argument and returns a list containing the values in the iterator. 
When you call the list() function on the blabla object, 
the blabla object will return the values in the sequence, which are the numbers from 0 to 9.

However, once the blabla object has returned all of the values in the sequence,
it will no longer have any values to return. 
Therefore, if you call the list() function on the blabla object again, it will return an empty list."""


def gen(n):
    print("start generate items")
    for i in range(n + 1):
        print(i)
        yield i
        print("back from yield")
    print("~*" * 20)


# print(sum(gen(10)))
