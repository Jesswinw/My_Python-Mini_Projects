import random

print("""Guess the Number
Instructions:
1.The computer guesses a number b/w 1 to 100
2.You have only 30 chances
3.Enter q to quit

---Best of Luck---""")

chnce=30
num = random.randint(1,100)

print("I Guessed a Number,",end='')
pdif=100
while(chnce):
    try:
        gus = int(input("Enter:>"))
    except:break
    chnce-=1
    
    print(pdif)
    if(gus==num):
        print("Wonderful Job")
        break
    elif(abs(gus-num)<=pdif):
        print("hotter")
    elif(abs(gus-num)<=10):
        print("hot")
    else:
        print("cold")
    print(f"You have {chnce} chances to go\n")
    pdif = abs(gus-num)
if(chnce==0):
    print(f"Number was {num}")