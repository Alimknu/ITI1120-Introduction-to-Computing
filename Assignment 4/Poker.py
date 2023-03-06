#Ali Mirzakhalili 300 288 698
import random
import copy

class PokerGame:
    def __init__(self, p = 2):
        self.players = p
        self.playerHands = []
        for i in range(p):
            self.playerHands.append(i)
            self.playerHands[i] = []#creates an empty array in the place of the player's number

        self.table = []

        self.deck = []#creating the deck of cards
        for i in range(4):
            for j in range(13):
                if j == 0:
                    string = "A"
                elif j < 9:
                    string = str(j+1)
                elif j == 9:
                    string = "T"
                elif j == 10:
                    string = "J"
                elif j == 11:
                    string = "Q"
                elif j == 12:
                    string = "K"
                if i == 0:
                    string = string+"D"
                elif i == 1:
                    string = string+"C"
                elif i == 2:
                    string = string+"S"
                elif i == 3:
                    string = string+"H"
                self.deck.append(string)

        for i in range(100):#shuffles the deck 100 times
            x = random.randint(0,len(self.deck)-1)
            y = random.randint(0,len(self.deck)-1)
            temp = self.deck[x]
            self.deck[x] = self.deck[y]
            self.deck[y] = temp

    def add_card(self, playerIndex):
        self.playerHands[playerIndex].append(self.deck.pop(len(self.deck)-1))

    def add_to_table(self):
        self.table.append(self.deck.pop(len(self.deck)-1))

    def sortHand(self, hands):#sorts the hand from lowest value card to highest
        sorted = False
        while sorted == False:
            for i in range(5):
                if i+1<5:
                    temp = list(hands[i])
                    temp2 = list(hands[i+1])

                    if temp[0] == "T":
                        temp[0] = 10
                    if temp[0] == "A":
                        temp[0] = 1
                    if temp[0] == "J":
                        temp[0] = 11
                    if temp[0] == "Q":
                        temp[0] = 12
                    if temp[0] == "K":
                        temp[0] = 13
                        
                    if temp2[0] == "T":
                        temp2[0] = 10
                    if temp2[0] == "A":
                        temp2[0] = 1
                    if temp2[0] == "J":
                        temp2[0] = 11
                    if temp2[0] == "Q":
                        temp2[0] = 12
                    if temp2[0] == "K":
                        temp2[0] = 13

                    if int(temp[0]) > int(temp2[0]):
                        g = hands[i+1]
                        hands[i+1] = hands[i]
                        hands[i] = g

            temp = list(hands[0])
            temp2 = list(hands[1])
            temp3 = list(hands[2])
            temp4 = list(hands[3])
            temp5 = list(hands[4])

            if temp[0] == "T":
                    temp[0] = 10
            if temp[0] == "A":
                    temp[0] = 1
            if temp[0] == "J":
                    temp[0] = 11
            if temp[0] == "Q":
                    temp[0] = 12
            if temp[0] == "K":
                    temp[0] = 13

            if temp2[0] == "T":
                    temp2[0] = 10
            if temp2[0] == "A":
                    temp2[0] = 1
            if temp2[0] == "J":
                    temp2[0] = 11
            if temp2[0] == "Q":
                    temp2[0] = 12
            if temp2[0] == "K":
                    temp2[0] = 13

            if temp3[0] == "T":
                    temp3[0] = 10
            if temp3[0] == "A":
                    temp3[0] = 1
            if temp3[0] == "J":
                    temp3[0] = 11
            if temp3[0] == "Q":
                    temp3[0] = 12
            if temp3[0] == "K":
                    temp3[0] = 13    

            if temp4[0] == "T":
                    temp4[0] = 10
            if temp4[0] == "A":
                    temp4[0] = 1
            if temp4[0] == "J":
                    temp4[0] = 11
            if temp4[0] == "Q":
                    temp4[0] = 12
            if temp4[0] == "K":
                    temp4[0] = 13

            if temp5[0] == "T":
                    temp5[0] = 10
            if temp5[0] == "A":
                    temp5[0] = 1
            if temp5[0] == "J":
                    temp5[0] = 11
            if temp5[0] == "Q":
                    temp5[0] = 12
            if temp5[0] == "K":
                    temp5[0] = 13

            if int(temp[0]) <= int(temp2[0]) <= int(temp3[0]) <= int(temp4[0]) <= int(temp5[0]):
                sorted = True
                return hands

    def isStraightFlush(self, hands):
        hands = self.sortHand(hands)
        suit = list(hands[0])
        suit = suit[1]
        for i in range(5):
            checker = list(hands[i])
            if checker[1] != suit:
                return False
            if i+1 < 5:
                checkNext = list(hands[i+1])

                if checker[0] == "T":
                    checker[0] = 10
                if checker[0] == "A":
                    checker[0] = 1
                if checker[0] == "J":
                    checker[0] = 11
                if checker[0] == "Q":
                    checker[0] = 12
                if checker[0] == "K":
                    checker[0] = 13

                if checkNext[0] == "T":
                    checkNext[0] = 10
                if checkNext[0] == "A":
                    checkNext[0] = 1
                if checkNext[0] == "J":
                    checkNext[0] = 11
                if checkNext[0] == "Q":
                    checkNext[0] = 12
                if checkNext[0] == "K":
                    checkNext[0] = 13

                checker[0] = int(checker[0])
                checkNext[0] = int(checkNext[0])

                if checker[0] == 1 and checkNext[0] != 2:
                    found = False
                    temp = list(hands)
                    for i in range(1,5):
                        tempX = list(temp[i])
                        tempX = str(tempX[0])
                        if tempX == "K":
                            found = True
                    if found == False:
                        return False 

                elif ((checker[0]+1) != checkNext[0]):
                    return False

        return True

    def isFourOfAKind(self, hands):
        hands = self.sortHand(hands)

        stringOneCounter = 0
        stringTwoCounter = 0
        
        stringOne = ""
        stringTwo = ""

        for i in range(5):
            temp = list(hands[i])
            if stringOne == "":
                stringOne = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo == "":
                stringTwo = temp[0]
            if temp[0] == stringOne:
                stringOneCounter = stringOneCounter + 1
            elif temp[0] == stringTwo:
                stringTwoCounter = stringTwoCounter + 1
        
        if stringOneCounter == 4 or stringTwoCounter == 4:
            return True
        else:
            return False

    def isFullHouse(self, hands):
        hands = self.sortHand(hands)

        stringOneCounter = 0
        stringTwoCounter = 0

        stringOne = ""
        stringTwo = ""

        for i in range(5):
            temp = list(hands[i])
            if stringOne == "":
                stringOne = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo == "":
                stringTwo = temp[0]
            if temp[0] == stringOne:
                stringOneCounter = stringOneCounter + 1
            elif temp[0] == stringTwo:
                stringTwoCounter = stringTwoCounter + 1

        if (stringOneCounter == 3 and stringTwoCounter == 2) or (stringOneCounter == 2 and stringTwoCounter == 3):
            return True
        else:
            return False

    def isFlush(self, hands):
        suit = list(hands[0])
        suit = suit[1]
        for i in range(5):
            temp = list(hands[i])
            if temp[1] != suit:
                return False
        return True

    def isStraight(self, hands):
        hands = self.sortHand(hands)
        for i in range(5):
            if i+1 < 5:
                temp = list(hands[i])
                temp2 = list(hands[i+1])

                if temp[0] == "T":
                    temp[0] = 10
                if temp[0] == "A":
                    temp[0] = 1
                if temp[0] == "J":
                    temp[0] = 11
                if temp[0] == "Q":
                    temp[0] = 12
                if temp[0] == "K":
                    temp[0] = 13

                if temp2[0] == "T":
                    temp2[0] = 10
                if temp2[0] == "A":
                    temp2[0] = 1
                if temp2[0] == "J":
                    temp2[0] = 11
                if temp2[0] == "Q":
                    temp2[0] = 12
                if temp2[0] == "K":
                    temp2[0] = 13

                temp[0] = int(temp[0])
                temp2[0] = int(temp2[0])

                if temp[0] == 1 and temp2[0] != 2:
                    found = False
                    temp = list(hands)
                    for i in range(1,5):
                        tempX = list(temp[i])
                        tempX = str(tempX[0])
                        if tempX == "K":
                            found = True
                    if found == False:
                        return False 

                elif temp[0]+1 != temp2[0]:
                    return False

        return True

    def isThreeOfAKind(self, hands):
        hands = self.sortHand(hands)

        stringOneCounter = 0
        stringTwoCounter = 0
        stringThreeCounter = 0
        
        stringOne = ""
        stringTwo = ""
        stringThree = ""

        for i in range(5):
            temp = list(hands[i])
            if stringOne == "":
                stringOne = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo == "":
                stringTwo = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo != ("" or temp[0]) and stringThree == "":
                stringThree = temp[0]

            if temp[0] == stringOne:
                stringOneCounter = stringOneCounter + 1
            elif temp[0] == stringTwo:
                stringTwoCounter = stringTwoCounter + 1
            elif temp[0] == stringThree:
                stringThreeCounter = stringThreeCounter + 1
        
        if stringOneCounter == 3 or stringTwoCounter == 3 or stringThreeCounter == 3:
            return True
        else:
            return False

    def isTwoPairs(self, hands):
        hands = self.sortHand(hands)

        stringOneCounter = 0
        stringTwoCounter = 0
        stringThreeCounter = 0
        
        stringOne = ""
        stringTwo = ""
        stringThree = ""

        for i in range(5):
            temp = list(hands[i])
            if stringOne == "":
                stringOne = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo == "":
                stringTwo = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo != ("" or temp[0]) and stringThree == "":
                stringThree = temp[0]

            if temp[0] == stringOne:
                stringOneCounter = stringOneCounter + 1
            elif temp[0] == stringTwo:
                stringTwoCounter = stringTwoCounter + 1
            elif temp[0] == stringThree:
                stringThreeCounter = stringThreeCounter + 1
        
        if (stringOneCounter == 2 and (stringTwoCounter == 2 or stringThreeCounter == 2)) or (stringTwoCounter == 2 and stringThreeCounter == 2):
            return True
        else:
            return False

    def isOnePair(self, hands):
        hands = self.sortHand(hands)

        stringOneCounter = 0
        stringTwoCounter = 0
        stringThreeCounter = 0
        stringFourCounter = 0
        
        stringOne = ""
        stringTwo = ""
        stringThree = ""
        stringFour = ""

        for i in range(5):
            temp = list(hands[i])
            if stringOne == "":
                stringOne = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo == "":
                stringTwo = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo != ("" or temp[0]) and stringThree == "":
                stringThree = temp[0]
            elif stringOne != ("" or temp[0]) and stringTwo != ("" or temp[0]) and stringThree != ("" or temp[0]) and stringFour == "":
                stringFour = temp[0]

            if temp[0] == stringOne:
                stringOneCounter = stringOneCounter + 1
            elif temp[0] == stringTwo:
                stringTwoCounter = stringTwoCounter + 1
            elif temp[0] == stringThree:
                stringThreeCounter = stringThreeCounter + 1
            elif temp[0] == stringFour:
                stringFourCounter = stringFourCounter + 1

        if stringOneCounter == 2 or stringTwoCounter == 2 or stringThreeCounter == 2 or stringFourCounter == 2:
            return True
        else:
            return False
        
class TexasHoldem(PokerGame):
    def __init__(self, p = 2):
        PokerGame.__init__(self, p)
    
    def deal(self):
        for i in range(self.players):
            for j in range(2):
                self.playerHands[i].append(self.deck.pop(len(self.deck)-1))
        for i in range(5):
            self.table.append(self.deck.pop(len(self.deck)-1))

    def hands(self):
        have = []
        for i in range(self.players):
            x = ""
            straightFlush = False
            FourofaKind = False
            FullHouse = False
            Flush = False
            Straight = False
            ThreeofaKind = False
            TwoPairs = False
            OnePair = False

            for a in range(3):
                for b in range(5):

                    currentThing = copy.deepcopy(self.table)
                    if a == (0 or 1):
                        currentThing[b] = self.playerHands[i][a]

                    elif a == 2:
                        if b+1 < 5:
                            currentThing[b] = self.playerHands[i][a-2]
                            currentThing[b+1] = self.playerHands[i][a-1]
                        else:
                            currentThing[0] = self.playerHands[i][a-1]
                            currentThing[4] = self.playerHands[i][a-2]

                    if self.isStraightFlush(currentThing):
                        x = "Straight Flush"
                        straightFlush = True
                    elif self.isFourOfAKind(currentThing) and straightFlush == False:
                        x = "Four of a Kind"
                        FourofaKind = True
                    elif self.isFullHouse(currentThing) and straightFlush == False and FourofaKind == False:
                        x = "Full House"
                        FullHouse = True
                    elif self.isFlush(currentThing) and straightFlush == False and FourofaKind == False and FullHouse == False:
                        x = "Flush"
                        Flush = True
                    elif self.isStraight(currentThing) and straightFlush == False and FourofaKind == False and FullHouse == False and Flush == False:
                        x = "Straight"
                        Straight = True
                    elif self.isThreeOfAKind(currentThing) and straightFlush == False and FourofaKind == False and FullHouse == False and Flush == False and Straight == False:
                        x = "Three of a Kind"
                        ThreeofaKind = True
                    elif self.isTwoPairs(currentThing) and straightFlush == False and FourofaKind == False and FullHouse == False and Flush == False and Straight == False and ThreeofaKind == False:
                        x = "Two Pairs"
                        TwoPairs = True
                    elif self.isOnePair(currentThing) and straightFlush == False and FourofaKind == False and FullHouse == False and Flush == False and Straight == False and ThreeofaKind == False and TwoPairs == False:
                        x = "One Pair"
                        OnePair = True
                    else:
                        if straightFlush == False and FourofaKind == False and FullHouse == False and Flush == False and Straight == False and ThreeofaKind == False and TwoPairs == False and OnePair == False:
                            x = "High Card"
            have.append(x)
        return have