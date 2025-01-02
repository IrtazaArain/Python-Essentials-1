c0 = int(input("Enter a non-negative, non-zero integer: "))
steps = 0
if c0 >= 1:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2
            print(c0)
        else:
            c0 = 3 * c0 + 1
            print(c0)
        steps +=1
print("steps = ",steps)


