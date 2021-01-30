def Add(numbers):
    if len(numbers) == 0:
        return 0
    elif numbers.startswith('//'):
        newline_index = numbers.find('\n')
        delimiter = numbers[2:newline_index]
        integers = numbers[newline_index+1:len(numbers)].split(delimiter)
        return sum([ int(integer.rstrip()) for integer in integers])
    else:
        return sum([ int(integer.rstrip()) for integer in numbers.split(',')])

if __name__ == "__main__":
    
    print("Testing start.")

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