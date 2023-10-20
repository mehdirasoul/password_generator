import random
letter=['a','b','c','d','e''f','g','A','B','C','D','E','F']
number=['1','2','3','4','5','6','7','8','9']
symbol=['!','#','$','%','&','(',')','*','+']

nr_letters= int(input("how many letter would you like?\n"))
nr_numbers= int(input("how many number would you like?\n"))
nr_symbols= int(input("how many symbols would you like?\n"))
 # logic
password = []

for nr in range(1,nr_letters + 1):
    password += random.choice(letter)


for num in range(1, nr_numbers + 1 ):
    password += random.choice(number)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbol)
random.shuffle(password)
pasworded = ''.join(password)
print(f" your password is {pasworded} ")

