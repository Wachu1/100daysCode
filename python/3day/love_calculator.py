print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

concat_name = name1 + name2

lower_name = concat_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
firstNumber = t + r + u + e
secedNumber = l + o + v + e
result = str(firstNumber) + str(secedNumber)
result = int(result)
if (result < 10) or (result > 90):
    print(f"Your score is {result}, you go together like coke and mentos.")
elif (result >= 40) and (result <= 50):
    print(f"Your score is {result}, you are alright together")

else :
    print(f"Your score is {result}.")
#Angela Yu
#Jack Bauer
