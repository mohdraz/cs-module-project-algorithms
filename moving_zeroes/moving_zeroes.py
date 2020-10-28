'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # zeroes = []

    # for i, x in enumerate(arr):
    #     print(f"i: {i} arr: {arr[i]} ")
    #     if arr[i] == 0:
    #         # zeroes.append(arr.pop(i))
    #         if arr[len(arr) - 1] != 0:
    #             arr[i] = arr

    # print(f"zeroes: {zeroes} ")

    # # arr = arr + zeroes
    # for x in zeroes:
    #     arr.append(x)
    # return arr
    i = 0
    j = 0

    while i <= j and j < len(arr):
        j = len(arr) - 1
        if arr[i] == 0:
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
            else:
                while arr[j] == 0:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)} ")
