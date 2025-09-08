'''Task 9: Tuple as Dictionary Key

Problem:
Create a dictionary with tuples as keys:
coords = {(10, 20): "Point A", (30, 40): "Point B"}
Print the value of key (10, 20)

Output:
Point A'''

coords = {(10, 20): "Point A", (30, 40): "Point B"}
print(coords.get((10,20)))
