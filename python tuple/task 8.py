'''Task 8: Nested Tuples

Problem:
Given nested = (1, (2, 3), (4, 5, (6, 7)))
Print 3, 6, 7

Output:
3
6
7'''

nested = (1, (2, 3), (4, 5, (6, 7)))

print(nested[1][1])
print(nested[2][2][0])
print(nested[2][2][1])
