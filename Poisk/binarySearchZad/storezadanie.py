def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            print("true")
            return
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print("false")

countOfElements = int(input())
prices = list(map(int, input().split()))
target_price = int(input())

binary_search(prices, target_price)