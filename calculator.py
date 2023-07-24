def calculator(numbers='0'):

    if ',' in numbers:
        for x in range(1, len(numbers)):
            before_character = numbers[x - 1]
            character = numbers[x]
            if not character.isnumeric() and not before_character.isnumeric():
                if "\n" in numbers:
                    position = numbers.index("\n")
                    return 'Number expected but "\n" found at position {}.'.format(position)
                else:
                    position = x
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
    print(calculator())
    print(calculator('1'))
    print(calculator('1,2,3'))
    print(calculator('1\n2,3'))


