def majority_element(arr):
    n = len(arr)
    
    countsOfELement = {}
    
    for num in arr:
        if num in countsOfELement:
            countsOfELement[num] += 1
        else:
            countsOfELement[num] = 1
        
        if countsOfELement[num] > n // 2:
            return num
    
    return -1

countOfElements = int(input())

listOfNumbers = list(map(int, input().split()))

majority_number = majority_element(listOfNumbers)
print(majority_number)