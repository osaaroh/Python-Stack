from random import randint
#program to to roll a die
def dice1():
    return randint(1,6)
def dice2():
    return randint(1,6)
A = dice1()
B = dice2()
total = A+B
text = 'The value of dice1 is ' + str(A)
text2 = 'The value of dice2 is ' + str(B)
text3 = 'Total value of both dice is ' + str(total)

print text
print text2
print text3
