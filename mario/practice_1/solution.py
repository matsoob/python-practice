from typing import List

REVERSE_MAPPING = {
    'a': '2',
    'b': '2',
    'c': '2',
    'd': '3',
    'e': '3',
    'f': '3',
    'g': '4',
    'h': '4',
    'i': '4',
    'j': '5',
    'k': '5',
    'l': '5',
    'm': '6',
    'n': '6',
    'o': '6',
    'p': '7',
    'q': '7',
    'r': '7',
    's': '7',
    't': '8',
    'u': '8',
    'v': '8',
    'w': '9',
    'x': '9',
    'y': '9',
    'z': '9'
}

def words_typable_from_this_number(number: str, words: List[str]) -> List[str]:
    # length of orginal number <= 15
    # words list can grow long 
    # all words shorter than number
    translated_number = [char for char in number if char != '1' and char != '0']

    if not translated_number:
        return []

    matched_words = list()
    for word in words:
        translated_word = [REVERSE_MAPPING[char] for char in word]
        if not word:
            matched_words.append(word)
        else:
            word_pointer = 0
            number_pointer = 0
            while word_pointer < len(translated_word) and number_pointer < len(translated_number):
                if translated_word[word_pointer] == translated_number[number_pointer]:
                    word_pointer += 1
                    number_pointer += 1
                else:
                    number_pointer -= word_pointer
                    word_pointer = 0
                    number_pointer += 1
            if word_pointer == len(translated_word):
                matched_words.append(word)
    return matched_words
    
if __name__ == '__main__':
    print(words_typable_from_this_number('1622298', ['aba', 'aa', 'xc', 'az', 'wewe']))










