class MyNumber:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5: # stop condition
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration # stop here
        
obj = MyNumber()
for number in obj:
    print(number)