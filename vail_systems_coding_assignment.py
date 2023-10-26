arr = [1,2,3,4,5,6,7]
position = 6

def array_rotation(arr, position):
    if position < 0: raise Exception("Position argument can't be below zero.")
    if position > len(arr): position = position - len(arr)

    while position > 0:
        arr.append(arr[0])
        arr.pop(0)
        position -= 1    

    return arr

try:
    print(array_rotation(arr, position))
except Exception as err:
    print(err)