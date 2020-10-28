'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    n = 0
    ret_value = []

    while (n+k) < (len(nums) + 1):
        # number = 0
        # for i in range(n, n+k):
        #     if nums[i] > number:
        #         print(f"number: {number} ")
        #         number = nums[i]
        # ret_value.append(number)
        # number = 0
        # n += 1

        number = []
        for i in range(n, n+k):
            number.append(nums[i])
        ret_value.append(max(number))
        number = []
        n += 1
    return ret_value


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

'''
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7]

 arr = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 2  
        output = sliding_window_max(arr, k)
        expected = [3, 3, -1, 5, 5, 6, 7]

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''