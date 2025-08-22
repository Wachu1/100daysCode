# auction ={
#     "name": [],
#     "price": []
# }
#
# next = True
#
# print("Welcome to the secret auction program")
# while next == True:
#     name = input("What is your name?: ")
#     bid = int(input("What's your bid?: $"))
#
#     auction['name'].append(name)
#     auction['price'].append(bid)
#     next_quest = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
#
#     if next_quest != 'yes':
#         next = False
#
#     print("\n" * 100)

lista =  [32 ,321, 33, 12, 12 ,42, 21, 21, 42]
a = 0
for x in lista:
    if x > a:
        a = x
print(a)


