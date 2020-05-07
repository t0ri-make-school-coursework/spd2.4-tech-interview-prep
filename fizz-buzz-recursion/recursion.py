# for num in range(start, end):
#     if num is a multiple of 3 & 5:
#         append FizzBuzz
#     else if num is a multiple of 3:
#         append Fizz
#     else if num is a multiple of 5:
#         append Buzz
#     else:
#         append num


def fizzbuzz_recursive(start, end, fizz_list=list()):
    # base case
    if len(fizz_list) is end - start + 1:
        return fizz_list
    
    # if empty
    if not fizz_list:
        fizz_list = [start]
    else:
        fizz_list.append(start + len(fizz_list))
    
    # get last element in list
    num = fizz_list[-1]
    
    # perform fizzbuzz
    if num % 3 == 0 and num % 5 == 0:
        fizz_list[-1] = 'FizzBuzz'
    elif num % 3 == 0:
        fizz_list[-1] = 'Fizz'
    elif num % 5 == 0:
        fizz_list[-1] = 'Buzz'

    return fizzbuzz_recursive(start, end, fizz_list)


print(fizzbuzz_recursive(15, 20))