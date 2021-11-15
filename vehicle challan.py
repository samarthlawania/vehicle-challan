a = int(input("Is it your birth day?"))
s = int(input("Enter the speed of your vehicle"))
# a = 1 means there is my birthday on that day
# a = 0 means there is not my birthday on that day
if a == 1 and s<=65:
    print(0)
elif a == 1 and 65<s<86:
    print(1)
elif a == 1 and s>=86:
    print(2)
if a == 0 and s<=60:
    print(0)
elif a == 0 and 60<s<81:
    print(1)
elif a == 0 and s>=81:
    print(2)
    
