class Result:
    def calculate(self, a, b, c=None):
        if c is None:
            total = a + b
            print("Total (2 subjects):", total)
        else:
            total = a + b + c
            print("Total (3 subjects):", total)
r = Result()
r.calculate(50, 60)     
r.calculate(50, 60, 70)    
