i = 15
j = 22

log = i and j

print(log)

bit = i & j
print(bit)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#

for i in my_list:
    if i in my_list:
        print(my_list[i])
        del my_list[i]
print("The list with unique elements only:")
print(my_list)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))


def fib_r(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
 
print(fib_r(4))

























