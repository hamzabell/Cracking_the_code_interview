def add_array(array, oldSum, index):
    if (index == len(array)):
        return array
    else:
        newSum = array[index] + oldSum
        array[index] = newSum
        return add_array(array, newSum, index+1)


print(add_array([1,2,3,4,5,6], 0, 0))