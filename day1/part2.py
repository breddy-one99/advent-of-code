# day 1 part 2

with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))

list1 = sorted(numbers[::2])
list2 = sorted(numbers[1::2])    
similarity_score = 0

for i in range(0, 1000):
    num_count = list2.count(list1[i])
    similarity_score += list1[i] * num_count

# print(len(similarity_list))
print(similarity_score)