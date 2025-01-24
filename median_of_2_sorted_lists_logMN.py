def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # Get the left and right elements at the partitions
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]

        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]

        # Check if the partition is valid
        if maxX <= minY and maxY <= minX:
            # Found the median
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            # Move partitionX left
            high = partitionX - 1
        else:
            # Move partitionX right
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted.")

# Example usage
nums1 = [1, 3, 5, 7]
nums2 = [2, 3, 4, 5, 6, 7]
print(findMedianSortedArrays(nums1, nums2))  # Output is 4.5 (not doing ciel)

nums1 = [1, 2, 8, 9, 9]
nums2 = [3, 4, 6, 6]
print(findMedianSortedArrays(nums1, nums2))  # Output is 6
