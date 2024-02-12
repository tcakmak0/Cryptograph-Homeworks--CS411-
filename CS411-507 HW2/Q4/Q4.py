from hw01_helper import *

def modularEquationSolver(a,b,n):
    gcd,x,_ = egcd(a,n)
    results = []
    if gcd == 1:
        # If a adnd n is co-prime solution is unique which could be found as follows:
        print("There is only 1 solution = ")
        print((b * x) % n)
    
    else:
        if b % gcd != 0:
            # If gcd is not 1 and does not divide the b there is no solution
            print("No valid answer!")
        else:
            # If gcd is not 1 and divides the b there are n solutions which could be found as follows
            a2 = a // gcd
            n2 = n // gcd
            b2 = b // gcd
            gcd2, x2, _ = egcd(a2,n2)
            result = (b2 * x2) % n2
            print(result)
            while result + n2 < n:
                result = (result + n2)
                print(result)


# For set a, b, and n in part a
a_a = 790561357610948121359486508174511392048190453149805781203471
a_b = 789213546531316846789795646513847987986321321489798756453122
a_n = 2163549842134198432168413248765413213216846313201654681321666

# For set a, b, and n in part b
b_a = 789651315469879651321564984635213654984153213216584984653138
b_b = 798796513213549846121654984652134168796513216854984321354987
b_n = 3213658549865135168979651321658479846132113478463213516854666

# For set a, b, and n in part c
c_a = 654652132165498465231321654946513216854984652132165849651312
c_b = 987965132135498749652131684984653216587986515149879613516844
c_n = 5465132165884684652134189498513211231584651321849654897498222

# For set a, b, and n in part d
d_a = 798442746309714903987853299207137826650460450190001016593820
d_b = 263077027284763417836483408268884721142505761791336585685868
d_n = 6285867509106222295001894542787657383846562979010156750642244

# Combine into lists
list_a = [a_a, b_a, c_a, d_a]
list_b = [a_b, b_b, c_b, d_b]
list_n = [a_n, b_n, c_n, d_n]



for i in range(0,4):
    print("Answer for part  ", i + 1, ":\n")
    modularEquationSolver(list_a[i],list_b[i],list_n[i])
    print("-----------------------------------------------------------------------------------")