

one = [1,2,3,4,5]
two = [2,5,6,9,3,1,4,5,7]

size = min(len(one), len(two))
final_list = [one[i] + two[i] for i in range(size)]
print(final_list)

print([x + y for x, y in zip(one, two)])