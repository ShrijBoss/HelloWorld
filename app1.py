# My first program 
# 1/22/2021
print("Good morning, Good after noon, Good evening")
#input return str, convert to int by using int function
time = int(input("Enter your time:"))
if time < 12:
    print("Good Morning")
elif time == 12:
    print("it is noon")
elif time > 18:
    print("Good Afternoon")
