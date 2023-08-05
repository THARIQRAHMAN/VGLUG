#program for Default Arguments
def add(x,y=600):
    "Calculate percentage for 12th mark"
    return str(x/600*100) + "%"
n= int(input("Enter the Mark that you Gained in 12th Standard: "))
print(add(n))
print(add.__doc__)