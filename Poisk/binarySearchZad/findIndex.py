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
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())

    result = search_insert_position(nums, target)
    print(result)
