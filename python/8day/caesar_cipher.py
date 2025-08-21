import caeser_fun

alphabet = [
    "a","b","c","d","e","f","g",
    "h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u",
    "v","w","x","y","z"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

if direction == "encode":
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caeser_fun.encrypt(orginal_text=text, shift_amount=shift)

elif direction == "decode":
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caeser_fun.decrypt(orginal_text=text, shift_amount=shift)

else:
    print("please enter correct data")


