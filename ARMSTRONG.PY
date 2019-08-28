print("ARMSTRONG NUMBER")
print(f"\nTo check single Armstrong number enter 1"
      f"\nTo check Armstrong number's in range enter 2\n")
number = int(input("enter your choice: "))

#to check single number
while number == 1:
    num = int(input("enter your number: "))
    power = len(str(num))
    sum = 0
    arm = num
    while arm > 0:
        digit = arm % 10
        sum += digit ** power
        arm //= 10
    if num == sum:
        print(num, "is armstrong")
    else:
        print(num, "is not armstrong")
    break

#to check in range
while number == 2:
    lower = int(input("lower range: "))
    higher = int(input("higher range: "))
    for num in range(lower, higher+1):
        power = len(str(num))
        sum = 0
        arm = num
        while arm > 0:
           digit = arm % 10
           sum += digit**power
           arm //= 10
        if num == sum:
            print(num)
    break
