# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [120420, 119705, "P12G"]

import random

# Defenição das funções

#EXTRA: se o utilizador introduzir uma palavra para tentar acertar fazer isso ya

#falta you win, o desnho, you lose, contador de erros, lista de letras, meter pimpao e comentarios repeticao de erradas e de letras

# Função que transforma caracteres especiais em normais
def normaliseWord (word):
    word = list(word)
    for char in word:
        
        if char == "Á" or char == "À" or char == "Ã" or char == "Â":
            word[word.index(char)] = "A"

        if char == "É" or char == "È" or char == "Ê":
            word[word.index(char)] = "E"

        if char == "Í" or char == "Ì" or char == "Î":
            word[word.index(char)] = "I"

        if char == "Ó" or char == "Ò" or char == "Õ" or char == "Ô":
            word[word.index(char)] = "O"

        if char == "Ú" or char == "Ù":
            word[word.index(char)] = "U"

        if char == "Ç":
            word[word.index(char)] = "C"

    return word
    
# função do jogo    
def hangmanGame(secret, hiddenWord, rawSecret):
    secret = list(secret)
    hiddenWord = list(hiddenWord)
    rawSecret = list(rawSecret)

    erros = 0
    letrasUsadas = []

    print(''.join(secret))

    while erros < 7:
        print(' '.join(hiddenWord))
        # O jogador escolhe uma letra
        playerInput = input("Escolhe uma letra: ").upper()
        
        # Verificação de letras repetidas
        if playerInput in letrasUsadas:
            print("ERRO: Letra repetida.")
        else:

            # Verificação de input válido
            if str.isalpha(playerInput) == False:
                print("ERRO: Só podes escrever letras.")
                continue
        
            # Substituição (ou não no caso de errar) das letras.
            else:
                acertou = 0

                for index in range(len(secret)):
                    if playerInput == rawSecret[index]:
                        hiddenWord[index] = secret[index]
                        acertou = 1
                
                if acertou == 0:
                    erros += 1

        
        
        
        
        
        
        




# Função função principal
def main():
    print("The Hangman!")
    from wordlist import words1, words2
    
    # Testagem dos diferentes tipos de palavras (O programa final usará apenas "words")
    wordsNormal = words1              # palavras sem acentos nem cedilhas.
    wordsSpecial = words2             # palavras com acentos ou cedilhas.
    words = words1 + words2          # palavras de ambos os tipos
   
    # Palavra secret (todos os caracteres tão em maiúscula)
    secret = random.choice(words).upper()

    #Palavra "secret" convertida em "_"
    hiddenWord = len(secret) * "_"
    
    # Palavra secret mas normalizada (sem caracteres especiais)
    rawSecret = normaliseWord(secret)
    
    
    # Programa principal 
    hangmanGame(secret, hiddenWord, rawSecret)





if __name__ == "__main__":
    main()