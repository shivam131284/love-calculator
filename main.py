# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name_1 = name1.lower()
name_2 = name2.lower()
both_names = (name_1 + name_2).lower()
#Write your code below this line 👇
a = (both_names).count("t")
b = (both_names).count("r")
c = (both_names).count("u")
d = (both_names).count("e")
e = (both_names).count("l")
f = (both_names).count("o")
g = (both_names).count("v")
h = (both_names).count("e")
true = (a + b + c + d)
love = (e + f + g + h)
print(f"your love score is {true}{love}")



