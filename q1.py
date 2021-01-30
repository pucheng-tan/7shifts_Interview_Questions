def Add(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum([ int(integer) for integer in numbers.split(',')])

print(Add("1,2,5"))
print(Add("0,8,9"))