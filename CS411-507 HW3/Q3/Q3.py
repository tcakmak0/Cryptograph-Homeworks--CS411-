# This code will produce the truth table of the given function

X1 = X2 = X3 = X4 = [0,1]

def F(x1,x2,x3,x4):
    return x4 ^ (x1 & x4) ^ (x1 & x4 & x2) ^ (x1 & x4 & x2 & x3) 

counter1 = 0
counter0 = 0
print("X1 | X2 | X3 | X4 | F")
for x1 in X1:
    for x2 in X2:
        for x3 in X3:
            for x4 in X4:
                result = F(x1,x2,x3,x4)
                print(x1,"  ",x2
                      ,"  ",x3,"  ",x4,"  ",result)
                if result == 1: counter1 += 1
                if result == 0: counter0 += 1


print("\n \nNumber of zeroes : ", counter0,"Number of ones : " ,counter1)
