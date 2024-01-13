def max_product_memoization(nums, k, index, remaining, memo):
    if remaining == 0 or index >= len(nums):
        return 1

    if (index, remaining) in memo:
        return memo[(index, remaining)]

    include_current = nums[index] * max_product_memoization(nums, k, index + 1, remaining - 1, memo)
    exclude_current = max_product_memoization(nums, k, index + 1, remaining, memo)

    result = max(include_current, exclude_current)
    memo[(index, remaining)] = result

    return result

def max_product(nums, k):
    if not nums or k == 0:
        return 0

    effective_k = min(k, len(nums))
    
    memo = {}
    return max_product_memoization(nums, effective_k, 0, effective_k, memo)

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

result = max_product(nums, k)
print(result)