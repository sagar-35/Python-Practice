class EvenNumbers:
    def __iter__(self):
        self.num = 2
        return self
    
    def __next__(self):
        if self.num <= 20:
            current = self.num
            self.num += 2
            return current
        else:
            raise StopIteration

evens = EvenNumbers()
for number in evens:
    print(number)