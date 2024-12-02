# day 1 part 1

with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))

list1 = sorted(numbers[::2])
list2 = sorted(numbers[1::2])    

total_distance = 0

for i in range(0, 1000):
    distance = abs(list1[i] - list2[i])
    total_distance += distance    

print(total_distance)