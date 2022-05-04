dict = {"one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"}

def num_translate_adv(number):
        for key, value in dict.items():
                if number == key:
                        return value
                elif number == key.title():
                        return value.title()

print(num_translate_adv("Four"))
print(num_translate_adv("ten"))
print(num_translate_adv("chto-to"))


