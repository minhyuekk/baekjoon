# def partition(a, left, right):
#     low = left + 1
#     high = right
#     pivot = a[left]
#
#     while low <=high:
#         while low <= right and a[low] <= pivot: low += 1
#         while high >= left and a[high] > pivot: high -= 1
#
#         if low < high:
#             a[low], a[high] = a[high], a[low]
#
#     a[left], a[high] = a[high], a[left]
#     return high
#
#
# def quick_sort(a, left, right):
#     if left < right:
#         mid = partition(a, left, right)
#         quick_sort(a, left, mid-1)
#         quick_sort(a, mid+1, right)


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# quick_sort(arr, 0, len(arr)-1)
low, high = 0, len(arr) - 1
# 초기 두 포인터
ans = abs(arr[low] + arr[high])
final = [arr[low], arr[high]]


def binary(low, high):
    global ans, final
    while low < high:
        # 두 포인터 탐색 반복
        sum = arr[low] + arr[high]

        if ans == 0:
            break

        if abs(sum) < ans:
            ans = abs(sum)
            final = [arr[low], arr[high]]

        if sum < 0:
            low += 1
        else:
            high -= 1
    return


binary(low, high)
print(final[0], final[1])