# poker hands

import numpy as np
import inspect

def loadHands(fileName):
    try:
        if fileName[-4:]!=".txt":
            raise ValueError("your filename is not written in the correct format")
        # open the file and read a line
        f = open(fileName,"r")
        line = f.readline()
        player1=[]
        player2=[]
        while line:
            cards = line.split()
            if len(cards) != 10:
                print("error loading the files")
                print(inspect.getsource(loadHands))
                raise IndexError("aaaaahhhhh")
            player1.append(cards[:5])
            player2.append(cards[5:]) # watch out
            line = f.readline()
        f.close()
        print("player1[0]")
        print(player1[0])
        return player1, player2
    except:
        print("\nError!!!\n")
        raise RuntimeError("error opening the file")

def score(hand):
    if royalFlush(hand):
        return 1
    elif straightFlush(hand):
        return 2
    elif fourOfAKind(hand):
        return 3
    elif fullHouse(hand):
        return 4
    elif flush(hand):
        return 5
    elif straight(hand):
        return 6
    elif threeOfAKind(hand):
        return 7
    elif twoPairs(hand):
        return 8
    elif onePair(hand):
        return 9
    return 10

def winner(hand1,hand2): # true if first hand won
    score1= score(hand1) # associated with how good the hand is, 1 is best,10 worst
    score2= score(hand2)
    if score1>score2:
        return False
    elif score1<score2:
        return True
    else:
        highCard1 = highCard(hand1)
        highCard2 = highCard(hand2)
        if len(highCard1)!=len(highCard2):
            print("Error")
            raise EnvironmentError("badd bad error")
        for i in range(len(highCard1)):
            if highCard1[i] > highCard2[i]:
                return True
            elif highCard1[i] < highCard2[i]:
                return False
        print("Error you shouldn't get to here")
        raise Exception("baaaad")

# boolean win/loss
def royalFlush(hand): # 1 boolean
    # hand is an array of string each of which represent a card
    suit = hand[0][1]
    need = ["T","J","Q","K","A"]
    have = []
    for card in hand:
        if card[1]!=suit:
            return False
    for card in hand:
        if card[0] in need:
            have.append(card[0])
    return True

def straightFlush(hand): # 2 boolean
    # all cards are consecutive values of same suit
    suit = hand[0][1]
    have = [] # this gonna be list of integers
    for card in hand:
        # i think it will be faster if we loop through the suits first
        if card[1]!= suit:
            return False
    # they are all of the same suit now
    for card in hand:
        if card[0]=="T":
            have.append(10)
        elif card[1]=="J":
            have.append(11)
        elif card[1]=="Q":
            have.append(12)
        elif card[1]=="K":
            have.append(13)
        elif card[1]=="A":
            have.append(14)
        else:
            have.append(int(card[0]))
    have.sort()
    if have[-1]-have[0] == 4:
        return True
    return False
        
def fourOfAKind(hand): # 3 boolean
    species1=[]
    species2=[]
    for card in hand:
        if not species1:
            species1=[card[0],1]
        else:
            if species1[0] == card[0]:
                species1[1]+=1
            else:
                if not species2:
                    species2=[card[0],1]
                else:
                    if species2[0] == card[0]:
                        species2[1]+=1
                    else:
                        return False
    if species1[1]==4 or species2[1]==4:
        return True
    return False   

def fullHouse(hand): # 4 boolean
    # just gonna copy paste fourOfAKind
    species1=[]
    species2=[]
    for card in hand:
        if not species1:
            species1=[card[0],1]
        else:
            if species1[0] == card[0]:
                species1[1]+=1
            else:
                if not species2:
                    species2=[card[0],1]
                else:
                    if species2[0] == card[0]:
                        species2[1]+=1
                    else:
                        return False
    if species1[1]==3 or species2[1]==3:
        return True
    else:
        print("\nError\n")
        print(inspect.getsource(loadHands))
        raise ArithmeticError("Steve you did something wrong!\n\
            check you're function fourOfAKind")
    
def flush(hand): # 5 boolean
    suit=hand[0][1]
    for card in hand:
        if card[1]!=suit:
            return False
    return True

def straight(hand): # 6 boolean
    # copy from straightFlush
    have = [] # this gonna be list of integers
    for card in hand:
        if card[0]=="T":
            have.append(10)
        elif card[0]=="J":
            have.append(11)
        elif card[0]=="Q":
            have.append(12)
        elif card[0]=="K":
            have.append(13)
        elif card[0]=="A":
            have.append(14)
        else:
            #print(card,card[0]) # trace
            have.append(int(card[0]))
    have.sort()
    if have[-1]-have[0] == 4:
        return True

def threeOfAKind(hand): # 7 boolean
    # efficiency could be improved
    for card1 in hand:
        for card2 in hand:
            count=0
            if card1[0]==card2[0]:
                count+=1
            if count==3:
                return True
    return False

def twoPairs(hand): # 8 boolean
    onlyValues=[]
    pair1=[]
    pair2=[]
    for card in hand:
        onlyValues.append(card[0])
    onlyValues.sort()
    if onlyValues[0]!= onlyValues[1]:
        i=1
    else:
        i=0
    pair1.append(onlyValues[i+0])
    pair1.append(onlyValues[i+1])
    pair2.append(onlyValues[i+2])
    pair2.append(onlyValues[i+3])
    if pair1[0]==pair1[1] and pair2[0]==pair2[1]:
        return True
    return False

def onePair(hand): # boolean
    v=[]
    for i in hand:
        v.append(i[0])
    if v[0]==v[1] or v[1]==v[2] or v[2]==v[3] or v[3]==v[4]:
        return True
    else:
        return False

def highCard(hand): # int
    values = [] # this gonna be list of integers
    for card in hand:
        if card[0]=="T":
            values.append(10)
        elif card[0]=="J":
            values.append(11)
        elif card[0]=="Q":
            values.append(12)
        elif card[0]=="K":
            values.append(13)
        elif card[0]=="A":
            values.append(14)
        else:
            values.append(int(card[0]))
    values.sort(reverse=True)
    return values


def main():
    player1, player2 = loadHands("poker_hands.txt")
    points1=0
    points2=0
    for i in range(len(player1)):
        if winner(player1[i],player2[i]):
            points1+=1
        else:
            points2+=1
    print("player1 points",points1)
    print("player2 points", points2)
    print("sum of points",points1+points2)


main()
input("\npress enter to exit")

"""
pseudocode

unpack the cards into lists [], they are mutable

determine what player 1 has, give it a score
determine what player 2 has, give it a score

if one of them has something higher ranking thant he other than he wines, declare him winner
elif they both have the same ranking cards then they both of them win
else (if there is not a clear winner print error)

call the winner function which returns the winner

add 1 point to the winner's score and loop through
"""

 