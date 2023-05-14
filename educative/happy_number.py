def happy_number(input: int) -> bool:
    current = input
    looping = False
    seen = set()
    while not looping:
        current_sum = 0
        while current != 0:
            current_sum += (current % 10)**2
            current = current // 10
        if current_sum == 1:
            return True
        elif current_sum in seen:
            return False
        else:
            seen.add(current_sum)
            current = current_sum


def happy_number_pointer_method(input: int) -> bool:
    def do_sum(fig: int) -> int:
        current_sum = 0
        while fig != 0:
            current_sum += (fig % 10)**2
            fig = fig // 10
        return current_sum

    slow = input
    fast = do_sum(input)

    while slow != fast and fast != 1:
        slow = do_sum(slow)
        fast = do_sum(do_sum(fast))
    
    return fast == 1



test_cases = [
    (23, True),
    (2, False)
]
if __name__ == '__main__':
    for input, output in test_cases:
        assert happy_number_pointer_method(input) == output