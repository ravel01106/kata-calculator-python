def position_two_delimiters_together(numbers):
    for x in range(1, len(numbers)):
        before_character = numbers[x - 1]
        character = numbers[x]
        if not character.isnumeric() and not before_character.isnumeric():
            return x
    return -1


def add(numbers='0'):
    separator = ','
    if not numbers[len(numbers) - 1].isnumeric():
        return "Number expected but EOF found."

    if numbers.startswith("//"):
        newline_position = numbers.index("\n")
        separator = numbers[2:newline_position]
        numbers = numbers[(newline_position + 1):len(numbers)]

    if len(numbers) > 1:
        if separator == ',':
            position = position_two_delimiters_together(numbers)
            if position != -1:
                if "\n" in numbers:
                    position = numbers.index("\n")
                    return 'Number expected but "\n" found at position {}.'.format(position)
                else:
                    return 'Number expected but "," found at position {}.'.format(position)

            numbers = numbers.replace("\n", ",")

        for character in numbers:
            if character not in separator and not character.isnumeric():
                return "'{}' expected but '{}' found at position {}.".format(
                    separator, character, numbers.index(character))

        array_numbers = numbers.split(separator)
        result = 0
        for numbers in array_numbers:
            result += int(numbers)
        return str(result)

    return numbers


if __name__ == '__main__':
    print(add())
