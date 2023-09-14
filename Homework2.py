def good():
    return ["Harry", "Ron", "hermione"]
def get_odds():
    for number in range(10):
        if number % 2 != 0: 
             yield number

#use for loop to find third value
for i, number in enumerate(get_odds()):
    if i == 2:
        print(number)
        break