def calculator(number='0'):
    if ',' in number:
        array_number = number.split(',')
        result = 0
        for number in array_number:
            result += int(number)
        return str(result)

    return number


if __name__ == '__main__':
    print(calculator())
    print(calculator('1'))
    print(calculator('1,2,3'))


