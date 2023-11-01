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
    
    letras_corretas = 0
    erros = 0
    letras_restantes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letras_usadas = []
    
    # Variável que servirá para reproduzir mensagens de erro ou outras
    message = ""

    # Repete-se até chegar aos 7 erros
    while erros < 7:
        
        # Este comando serve só para limpar o que está acima para uma visibilidade mais fácil
        print(10* "\n")
        
        print(' '.join(hiddenWord))
        print("Erros = ", erros, "/ 7")
        print("Letras disponíveis: ", ', '.join(letras_restantes))

        print(message)
       
        # O jogador escolhe uma letra
        playerInput = input("Escolhe uma letra: ").upper()
        
        # Verificação de letras repetidas
        if playerInput in letras_restantes:
           
            # Verificação de input válido
            if str.isalpha(playerInput) == False:
                message = "ERRO: Inválido."
                continue
        
            # Substituição (ou não no caso de errar) das letras.
            else:
                # Valor que se permanecer a 0 contará um erro
                acertou = 0
                
                # Comparação de cada letra em secret com a letra inputed pelo player
                for index in range(len(secret)):
                    if playerInput == rawSecret[index]:
                        hiddenWord[index] = secret[index]
                        acertou = 1
                        letras_corretas += 1

                        message = "Acertaste!"
                        
                        # Substituição da letra correta por um "+"
                        if playerInput in letras_restantes:
                            letras_restantes[letras_restantes.index(playerInput)] = "+"
                            letras_usadas.append(playerInput)
                
                # Caso o valor "acertou" seja 0, significa que o player não acertou nenhuma letra, logo o valor de "erros" subirá por 1.
                if acertou == 0:
                    erros += 1
                    letras_restantes[letras_restantes.index(playerInput)] = "-"
                    message = "Letra errada! Tenta outra vez!"
                    letras_usadas.append(playerInput)
                

            # Se o número de letras certas for do mesmo comprimento da palavra, o jogador vence
            if letras_corretas == len(hiddenWord):
                print("\nGANHASTES!")
                print("Palavra: ", ''.join(secret))
                break

        # Caso o player escolha uma letra já escolhida
        elif playerInput in letras_usadas:
            message = "ERRO: Letra repetida."

        # Caso o player apenas prima enter sem escrever nada
        else:
           message = "ERRO: Inválido."
        
    # GameOver se o player chegar aos 7 erros        
    else:
        print(10* "\n")
        print("Erros = ", erros, "/ 7")
        print("YOU LOSE! \nA palavra era:", ''.join(secret))
        

# Função principal
def main():
    print("The Hangman!")
    from wordlist import words1, words2
    
    # Testagem dos diferentes tipos de palavras (O programa final usará apenas "words")
    wordsNormal = words1             # palavras sem acentos nem cedilhas.
    wordsSpecial = words2            # palavras com acentos ou cedilhas.
    words = words1 + words2          # palavras de ambos os tipos
   
    # Palavra secret (todos os caracteres tão em maiúscula)
    secret = random.choice(words).upper()

    #Palavra "secret" convertida em "_"
    hiddenWord = len(secret) * "_"
    
    # Palavra secret mas normalizada (sem caracteres especiais)
    rawSecret = normaliseWord(secret)
    
    
    # Programa com o jogo  
    hangmanGame(secret, hiddenWord, rawSecret)





if __name__ == "__main__":
    main()