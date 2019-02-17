import math

a = int(input("Enter the smallest number of your desired interval.\n\t"))
while a < 2:
    a = int(input("The number has to be equal or greater than 2.\n\t"))
b = int(input("Now enter the greatest number of your desired interval.\n\t"))
while b <= a:
    b  = int(input("The number has to be greater than the first number you entered.\n\t"))
d = int(input("Now enter an integer.\n\t"))
prime_nums = []
for i in range(a, b + 1):
    if i > 1 :
        for j  in range(2, i):
            if (i % j) == 0:
                break
        else:
            prime_nums.append(i)
print(prime_nums)
p = -1
q = -1
i = 0
flag = False
while i < (len(prime_nums) - 1) and flag == False:
        if abs(prime_nums[i] - prime_nums[i+1]) == d:
                p = i
                q = i + 1
                flag = True
        i += 1
if p == -1 and q == -1:
    print("The pair you are looking for does not exist")
else:
    print("The pair you are looking for is [", prime_nums[p], ",", prime_nums[q], "] .")
