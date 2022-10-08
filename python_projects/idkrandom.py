def binary(number):
    result = ""
    n = number
    while n != 0:
        result += str(n % 2)
        n = int(n/2)

    # Filling with 0 until divisible by 8

    while len(result) % 8 != 0:
        result += "0"
    
    result = result[::-1]

    return result

def base64(input):

    # Converting the 

    binary_of_string = ""
    for letter in input:
        binary_of_string += binary(ord(letter))
    
    # If not divisible by 0 add 0 to the end

    old_len = len(binary_of_string) % 6

    if old_len != 0:
        binary_of_string += "0" * old_len
    
    new_bin = []

    x = 0
    cl = []
    while x < len(binary_of_string):
        if len(cl) == 8:
            new_bin.append(cl)
            cl = []
            cl.append(binary_of_string[x])
        else:
            cl.append(binary_of_string[x])
        x += 1
    
    result = ""
    for j in new_bin:
        result += chr(int(''.join(i for i in j)))
    
    return result


print(base64("abc"))
