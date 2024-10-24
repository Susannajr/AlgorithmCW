def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge(arr[:mid])
    right_half = merge(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

a= input("Please enter an array to have it sorted ")
sorted_a = merge(a)
print(f"Your sorrted array is: {sorted_a}")
