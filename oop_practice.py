class MyNumbers: 
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x <= 5:
            i = self.x
            self.x += 1
            return i
        else:
            raise StopIteration

num = MyNumbers()
for number in num:
    print(number)