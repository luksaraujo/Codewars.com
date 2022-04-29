# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata). Strings
# passed in will consist of only letters and spaces. Spaces will be included only when more
# than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    
    # Lista que armazena todas as palavras da sentença
    splitted_sentence = sentence.split() # Flag
    
    # Variável que armazena a quantidade de palavras na frase
    splitted_sentence_lenght = len(splitted_sentence)
    
    # Nova sentença que será formada
    new_sentence = ""
    
    # Laço que obtem a palavra e seu índice
    for index, word in enumerate(splitted_sentence):
        
        # Variável que armazena o tamanho da palavra
        word_length = len(word) # Flag
        
        # Se o tamanho da palavra for maior ou igual à cinco
        if word_length >= 5:
            
            # Reverte a palavra
            reversed_word = word[word_length::-1] # Flag
            
            # Chama a função que insere a palavra na nova sentença
            new_sentence = insert_word(reversed_word, index, splitted_sentence_lenght, new_sentence)

        # Se o tamanho da palavra for menor do que cinco    
        else:

            # Insere a palavra na nova sentença
            new_sentence = insert_word(word, index, splitted_sentence_lenght, new_sentence)

    # Retorna a nova sentença
    return new_sentence

def insert_word(word, index, splitted_sentence_lenght, new_sentence):
    
    # Flag que indica se a palavra é a última da frase
    is_last_word = True if index == splitted_sentence_lenght - 1 else False
    is_single_word = True if index == 0 and splitted_sentence_lenght == 1 else False
    
    # Se for uma frase de uma palavra única OU uma frase com apenas duas palavras e a palavra analisada for a última OU se for a última palavra da frase
    if is_single_word or (splitted_sentence_lenght == 2 and index == splitted_sentence_lenght - 1) or is_last_word:
                
        # Adiciona a palavra sem um espaço no final
        return (new_sentence + word)
                
    # Se for a primeira palavra
    elif index == 0:
                
        # Adiciona a palavra juntamente com um espaço na nova frase que será formada
        return (new_sentence + word + " ")
            
    # Se for uma palavra no meio da frase
    else:
                
        # Adiciona a palavra com um espaço
        return (new_sentence + word + " ")
          
print(spin_words("Teste de execução"))
