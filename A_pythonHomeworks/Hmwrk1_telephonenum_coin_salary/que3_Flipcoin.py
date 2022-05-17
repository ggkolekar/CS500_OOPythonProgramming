import random

def flip():
    rand = random.randint(0,1)
    return rand

def flipcoin():
    H = 0
    T = 1

    hside = 0
    tside = 0

    while (0==0):
        usrinput= input("Type F to flip the coin and R to see the result and exit.")
        if(usrinput == "F"):
            outcome = flip()
            if(outcome == 0):
                hside=hside+1
            else:
                tside=tside+1
            continue
        elif usrinput == "R":
            print("number of heads= "+ str(hside))
            print("number of tails= "+ str(tside))
            break
        else:
            print ('Enter valid input')

if __name__ == '__main__':
    flipcoin()

