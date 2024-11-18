numbers = list(range(1, 16))
duplicate = []

# duplicate = [num for num in numbers]

duplicate = [number for number in numbers for _ in range(2)]
print(duplicate)

for num in range(len(duplicate), 2):
    duplicate.remove(num)

new_single_list = []
new_single_list = [num for num in duplicate if num not in new_single_list]

print(f"duplicate: {duplicate}")
print(f"new_single_list: {new_single_list}")
