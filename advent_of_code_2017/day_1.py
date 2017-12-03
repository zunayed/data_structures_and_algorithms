#!/usr/local/bin/python3
"""
Day 1
The captcha requires you to review a sequence of digits (your puzzle input)
and find the sum of all digits that match the next digit in the list. The
list is circular, so the digit after the last digit is the first digit in
the list.
"""

def Input(day):
    "Open and read this day's input file."
    filename = 'input/input_{}.txt'.format(day)
    try:
        with open(filename, 'r') as content_file:
            return content_file.read().strip()
    except FileNotFoundError:
        return "file not found"

def part1(input):
    """
    input: string of digits
    output: sum of repeating nums
    """
    if not input:
        return 0

    count = 0

    for i in range(len(input)):
        if input[i] == input[i - 1]:
            count += int(input[i])

    return count

def part2(input):
    count = 0
    N = len(input)

    for i in range(N):
        if input[i] == input[i - N // 2]:
            count += int(input[i])

    return count


def main():
    assert part1("0") == 0
    assert part1("") == 0
    assert part1("33") == 6
    assert part1("1122") == 3
    assert part1("1111") == 4
    assert part1("1234") == 0
    assert part1("91212129") == 9

    input  = Input(1)

    print ("part1", part1(input))
    print ("part2", part2(input))

if __name__ == "__main__":
    main()
