def Add(numbers):
    if len(numbers) == 0:
        return 0
    elif numbers.startswith('//'):
        newline_index = numbers.find('\n')
        delimiter = numbers[2:newline_index]
        numbers = numbers[newline_index+1:len(numbers)]
        
        integers = [int(number.rstrip()) for number in numbers.split(delimiter)]

        exception_occurred = False
        negatives = []
        sum = 0
        for integer in integers:
            if integer < 0:
                exception_occurred = True
                negatives.append(integer)
            elif integer <= 1000:
                sum = sum + integer
        if exception_occurred == False:
            return sum
        else:
            raise Exception('Negatives not allowed', negatives)

    else:
        integers = [int(number.rstrip()) for number in numbers.split(',')]

        exception_occurred = False
        negatives = []
        sum = 0
        for integer in integers:
            if integer < 0:
                exception_occurred = True
                negatives.append(integer)
            elif integer <= 1000:
                sum = sum + integer
        if exception_occurred == False:
            return sum
        else:
            raise Exception('Negatives not allowed', negatives)

if __name__ == "__main__":
    
    print("Testing start.")

    if Add("//***\n1***2***3") != 6:
        print("Error: expected Add('//***\n1***2***3') to be 6, got: ", Add("//***\n1***2***3") )

    if Add("//*&%\n1*&%2*&%3") != 6:
        print("Error: expected Add('//*&%\n1*&%2*&%3') to be 6, got: ", Add("//*&%\n1*&%2*&%3") )

    if Add("1000,1001") != 1000:
        print("Error: expected Add('1000,1001') to be 1000, got: ", Add("1000,1001") )

    if Add("6000,1001") != 0:
        print("Error: expected Add('6000,1001') to be 0, got: ", Add("6000,1001") )

    try:
        Add("//$\n1$-2$-3")
    except Exception as e:
        print(e)

    try:
        Add("-1,2,-8")
    except Exception as e:
        print(e)
        
    if Add("//$\n1$2$3") != 6:
        print("Error: expected Add('//$\n1$2$3') to be 6, got: ", Add("//$\n1$2$3") )

    if Add("//@\n2@3@8") != 13:
        print("Error: expected Add('//@\n2@3@8') to be 13, got: ", Add("//@\n2@3@8") )

    if Add("1\n,\n2,5") != 8:
        print("Error: expected Add('1\n,\n2,5') to be 8, got: ", Add("1\n,\n2,5") )

    if Add("0,8,\n9") != 17:
        print("Error: expected Add('0,8,\n9') to be 17, got: ", Add("0,8,\n9") )

    if Add("1,2,5") != 8:
        print("Error: expected Add('1,2,5') to be 8, got: ", Add("1,2,5") )

    if Add("0,8,9") != 17:
        print("Error: expected Add('0,8,9') to be 17, got: ", Add("0,8,9") )

    print("Testing finished.")


