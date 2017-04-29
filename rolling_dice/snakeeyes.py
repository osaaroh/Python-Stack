from Dicee import A,B,dice1,dice2
count = 1
while(1>0):
    C = dice1()
    D = dice2()
    if ( C==1 and D == 1):
        text = "You got snake eyes "+ "A" + " is " + str(C) +  " B" + " is " + str(D)+ ' '
        print text+str(count)
        break
    else:
        text = "OOPs try Again "+ "A" + " is " + str(C) +  " B" + " is " + str(D)+ ' '
        print text + str(count)
    count = count + 1
