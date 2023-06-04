import random

def generator():
    # Busca na UTF-8 caracteres do end. 33 ao 126
    characters_all = [chr(i) for i in range(33, 127)]
    characters_number = [chr(i) for i in range(48, 58)]
    characters_word = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    # Seleciona n caracteres aleatórios do vetor caracters
    # E usa o "".join para concatenar como string
    pass_all = "".join(random.sample(characters_all, 8))
    pass_number = "".join(random.sample(characters_number, 8))
    pass_word = "".join(random.sample(characters_word, 8))

    return(pass_all, pass_number, pass_word)

if(__name__ == "__main__"):
    generator()