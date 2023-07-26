def position_two_delimiters_together(numbers):
    for x in range(1, len(numbers)):
        before_character = numbers[x - 1]
        character = numbers[x]
        if not character.isnumeric() and not before_character.isnumeric():
            return x
    return -1


def custom_delimiter(numbers, separator):
    newline_position = numbers.index("\n")
    separator = numbers[2:newline_position]
    return numbers[(newline_position + 1):len(numbers)], separator


def send_error_delimiters_together(numbers, separator, is_custom_delimiter):
    if separator == ',':
        position = position_two_delimiters_together(numbers)
        if position != -1:
            if "\n" in numbers:
                position = numbers.index("\n")
                return 'Number expected but "\n" found at position {}.'.format(position)

            return 'Number expected but "," found at position {}.'.format(position)

    elif is_custom_delimiter:
        for character in numbers:
            if character not in separator and not character.isnumeric():
                return "'{}' expected but '{}' found at position {}.".format(
                    separator, character, numbers.index(character))
    return ''


def add_numbers(numbers, separator):
    array_numbers = numbers.split(separator)
    result = 0
    for numbers in array_numbers:
        result += int(numbers)
    return str(result)


def calculator(numbers='0'):
    separator = ','
    is_custom_delimiter = False
    have_delimiter_at_end = not numbers[len(numbers) - 1].isnumeric()
    have_custom_delimiter =numbers.startswith("//")
    is_not_only_one_number = len(numbers) > 1

    if have_delimiter_at_end:
        return "Number expected but EOF found."

    if have_custom_delimiter:
        is_custom_delimiter = True
        numbers, separator = custom_delimiter(numbers, separator)

    is_a_comma_separator = separator == ','

    if is_not_only_one_number:
        have_delimiter_together = send_error_delimiters_together(numbers, separator, is_custom_delimiter) != ''

        if have_delimiter_together:
            return send_error_delimiters_together(numbers, separator, is_custom_delimiter)

        if is_a_comma_separator:
            numbers = numbers.replace("\n", ",")

        return add_numbers(numbers, separator)

    return numbers


if __name__ == '__main__':
    print(calculator())
