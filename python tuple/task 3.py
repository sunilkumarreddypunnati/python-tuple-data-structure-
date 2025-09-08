'''Task 3: Concatenation & Repetition

Problem:
Given:
t1 = (1, 2)
t2 = (3, 4)

Concatenate t1 and t2
Repeat the resulting tuple 2 times

Output:
(1, 2, 3, 4)
(1, 2, 3, 4, 1, 2, 3, 4)'''

t1 = (1, 2)
t2 = (3, 4)
concatenate=t1+t2
repeat=(concatenate*2)
print(concatenate)
print(repeat)