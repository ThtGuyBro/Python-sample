import time

#superheros = ["Spiderman", "Superman", "Ironman", "Man"]

#print(superheros[1])

#for i in superheros:
    #print(i)

#print(superheros)
#[0,1,2,3,4]
#[2, 1, 3, 0, 4, 2]
nums = [2, 1, 3, 4, 10, 9, 8, 7, 6, 5]
nums.sort()
"""for num in nums:
    print(f"{num}, mississippi")
    time.sleep(1)"""

#range(1,5)
for count in range(2,7):
    print(nums[count])

print(11 in nums)


if 11 not in nums:
    print("This is not a num")