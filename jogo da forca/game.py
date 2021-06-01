###########################
#      JOGO DA FORCA      #
###########################

import random

# tabuleiros
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']



class Hangman():

	def __init__(self, word): # metodo construtor
		self.word = word
		self.wrongLetters = []
		self.correctLetters = []

	def guess(self, letter): # metodo para adivinhar letra
		if letter in self.word and letter not in self.correctLetters: # se a letra estiver na palavra e nao estiver na lista de letras corretas...
			self.correctLetters.append(letter)
		elif letter not in self.word and letter not in self.wrongLetters: # se a letra nao estiver na palavra e nao estiver na lista de letras erradas...
			self.wrongLetters.append(letter) # adcionar na lista
		else:
			return False
		return True

	def hangman_over(self): # metodo para verificar se o jogo terminou
		return self.hangman_won() or (len(self.wrongLetters) == 6)

	def hangman_won(self): # metodo se o jogador venceu
		if '_' not in self.hide_word(): # se nao tiver mais '_' como espacos para completar
			return True
		return False

	def hide_word(self): # metodo para ocultar as letras
		hidLine = ''
		for letter in self.word:
			if letter not in self.correctLetters:
				hidLine += '_'
			else:
				hidLine += letter
		return hidLine

	def print_game_status(self): # metodo para checar status do jogo
		print(board[len(self.wrongLetters)])
		print("Palavra: " + self.hide_word())
		print("\nLetras erradas:")
		for letter in self.wrongLetters:
			print(letter)
		print("\nLetras corretas:")
		for letter in self.correctLetters:
			print(letter)



def rand_word():  # funcao para escolher palavra aleatoria
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0, len(bank))].strip()



# FUNCAO MAIN
def main():

	game = Hangman(rand_word()) # objeto

	# enquanto o jogo nao tiver terminado: imprime status e le uma nova letra
	while not game.hangman_over():
		game.print_game_status()
		letter = input("\nDigite uma letra: ")
		game.guess(letter)

	game.print_game_status()

	if game.hangman_won():
		print("\nParabens, voce venceu!")
	else:
		print("\nGame Over! Voce perdeu!")
		print("A palavra era: " + game.word)



# executar o programa		
if __name__ == "__main__":
	main()
