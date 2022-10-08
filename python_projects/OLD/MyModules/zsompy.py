from re import L


def zeros(dimensions = ()):
    res = []
    for i in range(dimensions[1]):
        temp_arr = []
        for x in range(dimensions[0]):
            temp_arr.append(0)
        res.append(temp_arr)
    return res

def create_arr(value, dimensions = ()):
    res = []
    for i in range(dimensions[1]):
        temp_arr = []
        for x in range(dimensions[0]):
            temp_arr.append(value)
        res.append(temp_arr)
    return res