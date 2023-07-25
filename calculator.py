def contain_two_different_delimiter(numbers):
    for x in range(1, len(numbers)):
        before_character = numbers[x - 1]
        character = numbers[x]
        if not character.isnumeric() and not before_character.isnumeric():
            return x
    return -1


def add(numbers='0'):
    if not numbers[len(numbers) - 1].isnumeric():
        return "Number expected but EOF found."

    if ',' in numbers:
        position = contain_two_different_delimiter(numbers)
        if position != -1:
            if "\n" in numbers:
                position = numbers.index("\n")
                return 'Number expected but "\n" found at position {}.'.format(position)
            else:
                return 'Number expected but "," found at position {}.'.format(position)

        numbers = numbers.replace("\n", ",")
        print(numbers)
        array_numbers = numbers.split(',')
        result = 0
        for numbers in array_numbers:
            result += int(numbers)
        return str(result)

    return numbers


if __name__ == '__main__':
    print(add())
    print(add('1'))
    print(add('1,2,3'))
    print(add('1\n2,3'))


