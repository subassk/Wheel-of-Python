import time

for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x) # "Sleep" for x seconds
print('Done!')



import random

rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))


myString = 'Hello, World! 123'

print(myString.upper()) # HELLO, WORLD! 123
print(myString.lower()) # hello, world! 123
print(myString.count('l')) # 3

s = 'python is pythonic'
print(s.count('python')) # 2


VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# PASTE YOUR WOFPlayer CLASS (from part A) HERE
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


# PASTE YOUR WOFHumanPlayer CLASS (from part B) HERE
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        firstline = "{} has ${}".format(self.name, self.prizeMoney)
        secondline = "Category: {}".format(category)
        thirdline = "Phrase: {}".format(obscuredPhrase)
        fourthline = "Guessed: {}".format(guessed)
        prompt = firstline + '\n' + '\n' + secondline + '\n' + thirdline + '\n' + fourthline + '\n' \
                 + '\n' + "Guess a letter, phrase, or type 'exit' or 'pass':"
        input(prompt)


# PASTE YOUR WOFComputerPlayer CLASS (from part C) HERE
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        currentRandom = random.randint(1, 10)
        if currentRandom > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        result = []
        guessedUpper = "".join(guessed).upper()
        for s in LETTERS:
            if (s not in guessedUpper) and ((s not in VOWELS) or (self.prizeMoney >= VOWEL_COST)):
                result.append(s)
        return result

    def getMove(self, category, obscuredPhrase, guessed):
        possibleletters = self.getPossibleLetters(guessed)
        if len(possibleletters) == 0:
            return "pass"

        if self.smartCoinFlip():
            highestIndex = 0
            resultchar = ''
            for s in possibleletters:
                index = WOFComputerPlayer.SORTED_FREQUENCIES.index(s)
                if index > highestIndex:
                    highestIndex = index
                    resultchar = s

            return resultchar
        else:
            return random.choice(possibleletters)

