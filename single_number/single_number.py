'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import defaultdict

def single_number(arr):
    
    # res = arr[0]
    # for i in range(1, len(arr)):
    #     res = res ^ arr[i]
    # return res
    # print(f"arr: {set(arr)} sum: {sum(arr)}\nsum.set: {2*sum(set(arr))} ")
    # return 2 * sum(set(arr)) - sum(arr)

    # res = []
    # for x in arr:
    #     if x not in res:
    #         res.append(x)
    #     else:
    #         res.remove(x)
    # return res.pop()

    table = defaultdict(int)
    for x in arr:
        table[x] += 1
    
    for i in table:
        if table[i] == 1:
            return i 


    

# def main():
#     print('working')


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    print(f"The odd-number-out is {single_number(arr)}")