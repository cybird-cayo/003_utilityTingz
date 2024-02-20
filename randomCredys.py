import random
import string

store1 = list(string.ascii_lowercase)
store2 = list(string.ascii_uppercase)
store3 = list(string.digits)
store4 = list(string.punctuation)

user_input = input("Please enter a desired password length greater than 12: ")

while True:
    try:
        characters_number = int(user_input)
        if characters_number < 12:
            print("Your number should be at least 12!")
            user_input = input("Greater than 12, please?")
        else:
            break
    except:
        print("Numbers only! Again, please!")
        user_input = input("Correct amount of characters, please? ")

random.shuffle(store1)
random.shuffle(store2)
random.shuffle(store3)
random.shuffle(store4)

part1 = round(characters_number * 30/100)
part2 = round(characters_number * 20/100)

result = []

for x in range(part1):
    result.append(store1[x])
    result.append(store2[x])

for x in range(part2):
    result.append(store3[x])
    result.append(store4[x])

random.shuffle(result)

password = "".join(result)
print("Strong Password:",password)
