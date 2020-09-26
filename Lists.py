#superheros = ["Spiderman", "Superman", "Ironman", "Man"]

#print(superheros[1])

#for i in superheros:
    #print(i)

#print(superheros)
#[0,1,2,3,4]
#[2, 1, 3, 0, 4, 2]
nums = [2, 1, 3, 0, 4]
i = 0
while i < len(nums):
    if nums[i] > nums[i+1]:
        nums.append(nums[i])
        del nums[i]
    i += 1

#nums.append(5)
#del nums[0]
print(nums)

