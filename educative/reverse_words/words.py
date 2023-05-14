def reverse_words(sentence: str):
    words = sentence.split(' ') # O_n
    words = [word for word in words if word]
    result = list()
    for i in range(len(words)): # O_n
        result.append(words[len(words) - 1 - i])
        
    return ' '.join(result) # O_n

def reverse_words2(sentence: str):
    sentence = list(sentence)
    if not sentence or len(sentence) == 1:
        return sentence
    left = 0
    right = len(sentence) - 1
    while left < right: # O_n time, constant space
        temp = sentence[left]
        sentence[left] = sentence[right]
        sentence[right] = temp
        # sentence[left], sentence[right] = sentence[right], sentence[left]
        left += 1
        right -= 1
    # now reversed
    left = 0
    right = 0
    
    def do_swap(start: int, end: int):
        # end is non-inclusive
        end -= 1
        while start < end:
            sentence[start], sentence[end] = sentence[end], sentence[start],
            start += 1
            end -= 1
        
    while right < len(sentence) - 1:
        if sentence[right] == ' ':
            do_swap(left, right)
            left = right + 1
            right = left
        else:
            right += 1
    if left != right:
        do_swap(left, right+1)
    return ''.join(sentence)

