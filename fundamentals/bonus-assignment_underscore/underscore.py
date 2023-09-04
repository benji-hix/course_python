class Underscore:
    def map(self, iterable, callback):
        new_iterable = iterable
        iterable[:] = [callback(x) for x in iterable]
        return new_iterable

    def find(self, iterable, callback):
        for entry in iterable:
            if (callback(entry) == True):
                 return entry 

    def filter(self, iterable, callback):
        new_iterable = [entry for entry in iterable if callback(entry)]
        return new_iterable

    def reject(self, iterable, callback):
        new_iterable = [entry for entry in iterable if not callback(entry)]
        return new_iterable


_ = Underscore()

print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
