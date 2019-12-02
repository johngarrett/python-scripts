from queue import PriorityQueue

test_grades = PriorityQueue()
overall_grade = 0

for i in range(1,5):
    test_grades.put(float(input(f"Enter grade for test {i}: ")))


for weight in [0.06, 0.09, 0.12, 0.18]:
    overall_grade +=  test_grades.get() * weight

overall_grade += float(input("Enter average lab grade: ")) * .15
overall_grade += float(input("Enter average recitation grade: ")) * .05
overall_grade += float(input("Enter average practice homework grade: ")) * .04
overall_grade += float(input("Enter average class participation grade: ")) * .04
overall_grade += float(input("Enter average regular homework grade: ")) * .05 #todo: check
overall_grade += float(input("Enter average reading questions grade: ")) * .02
# todo: bonus points

# A
print("TO get an A: \n")
print((90 - overall_grade) / 0.25)
print("TO get a B: \n")
print((80 - overall_grade) / 0.25)
print("TO get a C: \n")
print((70 - overall_grade) / 0.25)
