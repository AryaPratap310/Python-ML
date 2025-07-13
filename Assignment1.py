#Assignment 1 

import math

def SQUAREroot():
    try:
       n = float(input("Enter a number: "))
       if n >= 0:
              return math.sqrt(n)
       else:
              raise Exception("Square root of negative number is not possible")
    except ValueError:
        print('please enter a valid number')
    except Exception as e:
        print('unexpected Error', e)
    finally:
        print("calculation done.") 

print(SQUAREroot())

# homework we made a 2d matrix
#   x1   x2  x3
#   10  20  30 
#   14  24  34
#   16  26  36


# we have to store data in text as 
# x1, x2, x3
# 10, 20, 30
# 14, 24, 34 
# 16, 26, 36

arr = [['x1','x2', 'x3'],
       [10, 20, 30],
       [14, 24, 34],
       [16, 26, 36]
]

with open("Assignment1.csv",'w') as file:
    for i in arr:
        for j in i:
            if(i.index(j)==len(i)-1):
                file.write(str(j))
            else:
                file.write(str(j)+', ')
        file.write('\n')

# read
file=open("Assignment1.csv")
for line in file.readlines():
    print(line,end='')

# x1, x2, x3
# 10, 20, 30
# 14, 24, 34
# 16, 26, 36