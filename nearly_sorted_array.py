def nearly_sorted_array(arr): 
    for i in range(len(arr) - 1): 
        if arr[i] > arr[i+1]: 
            arr[i+1], arr[i] = arr[i], arr[i+1]
        
    for i in range(len(arr) - 1, 0, -1): 
        if arr[i] < arr[i-1]: 
            arr[i-1], arr[i] = arr[i], arr[i-1]

    return arr

def sort_nearly_sorted_array(arr):
    n = len(arr)
    if n <= 1:
        return arr  # Already sorted
    
    # Find the position where the array is out of order
    pos = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            pos = i
            break
    
    if pos == -1:
        return arr  # Array is already sorted
    
    # Find the correct position for the out-of-place element
    # We need to determine which element is out of place: arr[pos] or arr[pos+1]
    
    # Assume arr[pos] is correct and arr[pos+1] needs to move
    misplaced = arr[pos+1]
    correct_pos = pos+1
    
    # Check if arr[pos] is correct
    if pos > 0 and arr[pos] < arr[pos-1] or pos+2 < n and arr[pos] > arr[pos+2]:
        # arr[pos] is out of place
        misplaced = arr[pos]
        correct_pos = pos
        
    # Find the correct position for the misplaced element
    while correct_pos > 0 and arr[correct_pos-1] > misplaced:
        correct_pos -= 1
    while correct_pos < n-1 and arr[correct_pos+1] < misplaced:
        correct_pos += 1
    
    # Move the misplaced element to its correct position
    if pos+1 == correct_pos and misplaced == arr[pos]:
        # Just swap the two elements
        arr[pos], arr[pos+1] = arr[pos+1], arr[pos]
    else:
        # Remove the misplaced element
        if misplaced == arr[pos]:
            del arr[pos]
        else:
            del arr[pos+1]
        
        # Insert at the correct position
        arr.insert(correct_pos, misplaced)
    
    return arr

# [1, 2, 9, 3 , 7, 8 ] # pos
# [1, 2, 3, -1, 7, 8 ] # pos + 1
if __name__ == "__main__": 
    print(nearly_sorted_array([1, 2, 3, -1, 7, 8 ]))