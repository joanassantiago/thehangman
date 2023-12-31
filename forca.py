# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [120420, 119705, "P12G"]

import random

# Defenição das funções

#So falta o boneco mas podemos faze-lo bonitao


# Desenho do hangman a ser chamado pelo numero de erros
def hangDrawing(erros):
    if erros == 0: hangman = ("     _________  \n    |/        |\n    |           \n    |            \n    |           \n    |            \n    |          \n----+----------------")
    if erros == 1: hangman = ("     _________  \n    |/        |\n    |         O \n    |            \n    |           \n    |            \n    |          \n----+----------------")
    if erros == 2: hangman = ("     _________  \n    |/        |\n    |         O \n    |         |  \n    |         | \n    |            \n    |          \n----+----------------")
    if erros == 3: hangman = ("     _________  \n    |/        |\n    |         O \n    |        /|  \n    |         | \n    |            \n    |          \n----+----------------")
    if erros == 4: hangman = ("     _________  \n    |/        |\n    |         O \n    |        /|\ \n    |         | \n    |            \n    |          \n----+----------------")
    if erros == 5: hangman = ("     _________  \n    |/        |\n    |         O \n    |        /|\ \n    |         | \n    |        /   \n    |          \n----+----------------")
    if erros == 6: hangman = ("     _________  \n    |/        |\n    |         O \n    |        /|\ \n    |         | \n    |        / \ \n    |          \n----+----------------")
    if erros == 7: hangman = ("     _________  \n    |/        |\n    |       (x_x) \n    |        /|\ \n    |         | \n    |        / \ \n    |          \n----+----------------")
    return hangman

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
        print(hangDrawing(erros))
        
        print("\nPalavra:", ' '.join(hiddenWord))
        
        print("\nErros = ", erros, "/ 7")
        
        print("Letras disponíveis: ", ', '.join(letras_restantes))
 
        print(message)
        
        # O jogador escolhe uma letra
        playerInput = input("\nEscolhe uma letra (Se estiveres confiante, podes tentar adivinhar a palavra): ").upper()
        
        # Se o jogador quiser adivinhar apenas uma letra
        if len(playerInput) == 1:   
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
                    print("\nGANHASTE!")
                    print("Palavra: ", ''.join(secret))
                    break
        

            # Caso o player escolha uma letra já escolhida
            elif playerInput in letras_usadas:
                message = "ERRO: Letra repetida."

            # Caso o player apenas prima enter sem escrever nada
            else:
                message = "ERRO: Inválido."
        
        # Caso o player tente acertar a palavra toda de uma vez
        elif len(playerInput) == len(hiddenWord):
            if list(playerInput) == rawSecret: # Se as letras em playerInput forem as mesmas do que em rawSecret
                print("\nGANHASTE!")
                print("WOW, adivinhaste a palavra por completo!")
                break
            # Será contado um erro se ele 
            else:
                message = "Ah! Estavas quase... A palavra não é essa."
                erros += 1 
        
        elif playerInput not in letras_usadas:
            message = "ERRO: Inválido."

        else:
            message = "ERRO: A palavra introduzida não tem o mesmo comprimeto do que a palavra escondida."

    
    
    # GameOver se o player chegar aos 7 erros        
    else:
        print()
        print(hangDrawing(7))
        print("\nErros = ", erros, "/ 7")
        print("Letras disponíveis: ", ', '.join(letras_restantes))
        print("YOU LOSE! \nA palavra era:", ''.join(secret))
        

# Função principal
def main():
    print("The Hangman!")
    from wordlist import words1, words2
    
    # Testagem dos diferentes tipos de palavras (O programa final usará apenas "words")
    wordsNormal = words1             # palavras sem acentos nem cedilhas.
    wordsSpecial = words2            # palavras com acentos ou cedilhas.
    words = words1 + words2          # palavras de ambos os tipos

    import sys                  # INCLUA estas 3 linhas para permitir
    if len(sys.argv) > 1:       # correr o programa com palavras dadas:
        words = sys.argv[1:]    #   python3 forca.py duas palavras
   
    # Palavra secret (todos os caracteres tão em maiúscula)
    secret = random.choice(words).upper()

    # Print de secret (apenas para troubleshooting)
    # print(secret)

    #Palavra "secret" convertida em "_"
    hiddenWord = len(secret) * "_"
    
    # Palavra secret mas normalizada (sem caracteres especiais)
    rawSecret = normaliseWord(secret)
    
    
    # Programa com o jogo  
    hangmanGame(secret, hiddenWord, rawSecret)





if __name__ == "__main__":
    main()