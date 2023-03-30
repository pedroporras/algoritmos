


# Esta propuesta no es valida porque no esta tomando en cuenta el orden si no que esta tomando en cuenta el valor
def compute_word_weight(word, dictionary):
    """Return the weight of a word."""
    weight = 0
    for letter in word:
        if letter in dictionary:
            weight += dictionary[letter]
        else:
            weight += 0

    return weight

# Esta propuesta no resuelve el problema
def check_words(words, alphabet):
    """Return a list of words that appear in dictionary."""
    result = []
    dictionary = {letter: index for index, letter in enumerate(alphabet)}
    for word in words:
        word_weight = compute_word_weight(word, dictionary)
        for other_word in words:
            other_word_weight = compute_word_weight(other_word, dictionary)
            if word_weight > other_word_weight:
                return False

    return True


# Recorrer la lista de palabras
# Comparar el orden de palabras de i y i+1
# Si el orden de i es mayor que el orden de i+1 entonces no es valido
def check_words(words, alphabet):
    """Return a list of words that appear in dictionary."""
    dictionary = {letter: index for index, letter in enumerate(alphabet)}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        min_length = min(len(word), len(next_word))

        if not next_word:
            return True

        for j in range(min_length):
            print(word[j], next_word[j], dictionary[word[j]], dictionary[next_word[j]])
            if dictionary[word[j]] > dictionary[next_word[j]]:
                return False
        
        if len(word) > len(next_word):
            return False

        print(word, next_word, min_length)
    return True


if __name__ == "__main__":
    palabras = ["conocer", "cono"]
    orden_alfabeto = "abcdefghijklmnopqrstuvwxyz"
    print(check_words(palabras, orden_alfabeto))

    palabras = ["habito", "hacer", "lectura", "sonreir"]
    orden_alfabeto = "hlabcdefgijkmnopqrstuvwxyz"
    print(check_words(palabras, orden_alfabeto))

    print(compute_word_weight("asd", {"a": 1, "s": 2, "d": 3}))
    print(compute_word_weight("dsa", {"a": 1, "s": 2, "d": 3}))