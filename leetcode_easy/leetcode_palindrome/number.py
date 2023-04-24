

def solution_1(input: int) -> bool:
    input_string = str(input)
    i = 0
    j = len(input_string) - 1
    while (i != j):
        if abs(i-j) == 1:
            return input_string[i] == input_string[j]
        if input_string[i] == input_string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def solution_2(input: int) -> bool:
    if input < 0:
        return False 
    remaining_input = input
    flipped_num = 0
    while(remaining_input != 0):
        last_dig = remaining_input % 10
        flipped_num = flipped_num * 10 + last_dig
        remaining_input = int(remaining_input / 10)
    return flipped_num == input


if __name__ == '__main__':
    print('Input in format: 1,3,4,5')
    inp = input()
    inp.strip()
    # split_str = inp.split(',')
    # arr = [int(c) for c in split_str]
    print(solution_1(int(input)))
