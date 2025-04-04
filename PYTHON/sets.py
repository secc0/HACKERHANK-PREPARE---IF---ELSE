def average(array):
    numbers = set(array)
    sum = 0
    for i in numbers:
        sum += i
    avg = float(sum / len(numbers))
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)  