
#4 Classes defined
# 1 With composition
# 1 with inheritence 
# All using __init__

#Methods
#Each class has 2 methods
#Subclass overrides at least one superclass method

#Attributes
#Each class has 2 __init__ attributes

class BasicMath:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Addition(self):
        return self.x + self.y
    
    def Subtraction(self):
        return self.x - self.y
    
    def Multiply(self):
        return self.x * self.y

    def Divide(self):
        return self.x / self.y 
    
    def Times_table(self):
        for i in range(1, self.y):
            print("%i * %i = %i" % (i, self.y, (i*self.y)))
#Inheritance
class Advanced(BasicMath):
    def __init__(self, x, y, avg, n):
        super().__init__(x, y)
        #inheriting values x and y
        self.avg = avg
        self.n = n

    def Z_Score_of_x(self):
        return (self.x - self.avg)


#Compositions
class Composition:
    def __init__(self):
        self.base = BasicMath()

    #Overrides the previous multiply function
    def Multiply(self):
        return self.base.x * self.base.y
    
    def Times_of_y(self):
        return self.base.Times_table()

    

#One class for physics like gravity, newton, force, gravity can be __9.8

b = BasicMath(2, 4)
print(b.Addition())
print(b.Times_table())
c = Composition(x,y)
print(c.Multiply())