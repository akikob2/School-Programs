#  Description: program that runs operations on linear equations

class LinearEquation():

    def __init__(self,slope,yInt):
        self.m = slope
        self.b = yInt

    #Method that returns the string mx + b
    def showEq(self):
        
        #if b is positive then checking if m is positive, negative, or 0
        if self.b > 0:
            if self.m > 0:
                return (str(self.m)+"x + "+str(self.b))
                
            elif self.m < 0:
                return ("- "+str(int(self.m/(-1)))+"x + "+str(self.b))

            elif self.m == 0:
                return (str(self.b))
            
        #if b is negative
        elif self.b < 0:
            if self.m > 0:
                return (str(self.m)+"x - "+str(int(self.b / (-1))))

            elif self.m < 0:
                return ("- "+str(int(self.m / (-1)))+"x - "+str(int(self.b/(-1))))

            elif self.m == 0:
                return (str(self.b))
            
        #if b and m = 0
        elif self.b == 0:
            if self.m > 0:
                return (str(self.m)+"x")
            elif self.m < 0:
                return ("- "+str(int(self.m / (-1)))+"x")
            elif self.m == 0:
                return
            
    #Method that adds up two linear equations
    def add(self,eq2):
        newM = self.m + eq2.m
        newB = self.b + eq2.b
        newEq = LinearEquation(newM,newB)
        return newEq
                          
    #Method that subtracts two linear equations
    def sub(self,eq2):
        newM2 = self.m - eq2.m
        newB2 = self.b - eq2.b
        newEq2 = LinearEquation(newM2,newB2)
        return newEq2
                
    #Method that returns the composition of two equations            
    def compose(self,eq2):
        newM3 = self.m * eq2.m
        newB3 = (self.m * eq2.b) + self.b
        newEq3 = LinearEquation(newM3,newB3)
        return newEq3

    #Method that evaluate equation using an integer
    def evaluate(self,num):
        value = (self.m * num) + self.b
        return value


def main():

   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")
   
main()
        
        

        
