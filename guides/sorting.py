student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
student_tuples.sort(key=lambda x: x[2], reverse=True)
print(student_tuples)
