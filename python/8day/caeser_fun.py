alphabet = [
    "a","b","c","d","e","f","g",
    "h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u",
    "v","w","x","y","z"
]

def encrypt(orginal_text, shift_amount):
    cipher_text = ""
    for letter in orginal_text:
       shifted_position =  alphabet.index(letter) + shift_amount

       shifted_position = shifted_position % len(alphabet)
       cipher_text +=  alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")



def decrypt(orginal_text, shift_amount):
    cipher_text = ""

    for letter in orginal_text:
        shifted_positon = alphabet.index(letter) - shift_amount
        shifted_positon = shifted_positon % len(alphabet)
        cipher_text += alphabet[shifted_positon]

    print(f"Here is the decode result: {cipher_text}")



