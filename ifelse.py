# var1 = 6
# var2 = 66
# var3 = int(input())
# if var3 > var2:
#     print("Greater")
# else:
#     print("lesser")

# QUIZ TIME using if else ladder write the program to check the user is
# Eligible for the licence


print("Enter the age = ")
age = int(input())
if age > 70:
    print("We need NOC from DR. for clearance!!")

elif age > 18:
    print("You are eligible for the licence  ")

elif age < 18:
    print("You are not eligible for the licence under age  ")

elif age == 18:
    print("Sorry we can't decide")

else:
    print("Sorry we are not able to decide ")
