def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__ == "__main__":
    countOfElements = int(input())
    numbers = list(map(int, input().split()))
    searchableNumber = int(input())

    foundIndex = search_insert_position(numbers, searchableNumber)
    print(foundIndex)
