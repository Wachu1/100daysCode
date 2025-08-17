# Program składa się z elementu losowego funckja random losuje liczbe 0,1,2 każda
# z nich odzwerciedla papier kamien lub nozyce user wybiera numer od 0,1,2 i sprawdza
# warunek i pokazuje wygranego

import random
rock = '🧱'
paper = '📄'
Scissors = '✂️'


game = [0, 1, 2]

enemy = random.randint(0,2)
print("Gra w hiphaphop \n")
user = int(input(""))