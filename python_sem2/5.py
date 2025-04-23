# part 1
num = input("Enter a number: ")
if int(num) % 2 == 0:
    print(num + " is even")
else:
    print(num + " is odd")

# part2
num = input("Enter a number up to which the odd and even numbers should be listed: ")
num = int(num)
for i in range(num):
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

#part3
num = input("Enter a number up to which the odd and even numbers should be listed: ")
num = int(num)
i = 0
while i < num:
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
    i += 1
