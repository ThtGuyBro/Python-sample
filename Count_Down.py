import time

nums = [2, 1, 3, 0, 4, 10, 9, 8, 7, 6, 5]
nums.sort(reverse=True)
for num in nums:
    print(num)
    time.sleep(1)
print("Have a nice day.")
time.sleep(1)
print("KABOOOM!!!")