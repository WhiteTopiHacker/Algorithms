from random import randrange

# i -> position where next element is present
# j -> position where next smaller element has to be placed

def partition(arr, left, right):
	j = left
	pivot_index = randrange(left, right)
	pivot = arr[pivot_index]
	arr[right], arr[pivot_index] = arr[pivot_index], arr[right]

	for i in range(left, right):
		if (arr[i] <= pivot):
			arr[i], arr[j] = arr[j], arr[i]
			j += 1

	arr[j], arr[right] = arr[right], arr[j]
	return j

def quick_sort(arr, left, right):
	if left >= right:
		return

	pivot_index = partition(arr, left, right)
	quick_sort(arr, left, pivot_index - 1)
	quick_sort(arr, pivot_index + 1, right)

	return

li = list(map(int, input().split()))
n = len(li)
quick_sort(li, 0, n - 1)

print(li)