arr = [1,2,3,4,5,6,7]
position = 2

def array_rotation_slice(arr, position):
    if position < 0: 
        raise Exception("Position argument can't be below zero.")
    elif position > len(arr): position = position - len(arr)

    arr = arr[position:] + arr[:position]

    return arr

try:
    print(array_rotation_slice(arr, position))
except Exception as err:
    print(err)