# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        return 1 if len(player1_word) > len(player2_word) else 2 if len(player1_word) < len(player2_word) else 0
    

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        VOWELS = 'aeiou'
        vowels1 = [char for char in player1_word if char in VOWELS]
        vowels2 = [char for char in player2_word if char in VOWELS]
        return 1 if len(vowels1) > len(vowels2) else 2 if len(vowels1) < len(vowels2) else 0
    

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        RPS = ['rock', 'paper', 'scissors']
        # check for ties
        if player1_word not in RPS and player2_word not in RPS:
            return 0
        if player2_word == player1_word:
            return 0
        # check for incorrect words
        elif player2_word not in RPS:
            return 1
        elif player1_word not in RPS:
            return 2
        # correct words
        else:
            if player1_word == RPS[0]:
                return 1 if player2_word == RPS[2] else 2
            if player1_word == RPS[1]:
                return 1 if player2_word == RPS[0] else 2
            if player1_word == RPS[2]:
                return 1 if player2_word == RPS[1] else 2
    
