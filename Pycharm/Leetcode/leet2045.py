nums = [1,3, 2, 3, 4, 5, 2,5]
nums1 = [1,2,3,6]
nums2 = [2,3,4,5]

i,j = 0,0

while i<len(nums1) and j<len(nums2):
    if nums1[i] == nums2[j]:
        print(nums1[i])
        break
    elif nums1[i] < nums2[j]:
        i+=1
    else:
        j+=1


