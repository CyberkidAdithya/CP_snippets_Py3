def binSearch_iter(arr, key):
	beg, end = 0, len(arr) - 1
	while beg <= end:
		mid = beg + (end - beg) // 2  # to avoid mid overflow
		if key == arr[mid]:
			return True
		elif key < arr[mid]:
			end = mid - 1
		else:
			beg = mid + 1
	return False
# arr = [84, 21, 47, 96, 15]
# print(binSearch_iter(arr, 96))

def binSearch_recur(arr, key, beg, end):
	if beg > end:
		return False
	else:
		mid = (beg + end) // 2  # may face mid overflow!
		if key == arr[mid]:
			return True
		elif key < arr[mid]:
			return binSearch_recur(arr, key, beg, mid - 1)
		else:
			return binSearch_recur(arr, key, mid + 1, end)
# arr = [84, 21, 47, 96, 15]
# print(binSearch_recur(arr, 96, 0, len(arr) - 1))
