from queue import PriorityQueue

test_grades = PriorityQueue()
overall_grade = 0

print("Input percentage grades as whole numbers (e.g. 82.4).\n")
for i in range(1,5):
    test_grades.put(float(input(f"Enter percentage for test {i}: ")))


for weight in [0.06, 0.09, 0.12, 0.18]:
    overall_grade +=  test_grades.get() * weight

for (title, weight) in [("lab", .15), ("recitation", .05),
        ("practice homework", .04), ("class participation", .04),
        ("regular homework", .05), ("reading quesitons", .02)]: 
    overall_grade += float(input(f"Enter average {title} grade: ")) * weight
# todo: bonus points

#tood: check regular homeworkg rade precentage
for grade in range(90, 69, -10):
    print(f"\n To get a {grade}, you need a: \n {(grade - overall_grade) / 0.25}% on the final")
