#nested loops
scores = []

students = int(input("How many students are in your class?"))

print ("Now enter each student's score ontheir last test")

for i in range(students):
    while True:
        scr= int(input("Enter a score: "))
        if scr < 0:
            print("Try again")
        else:
            scores.append(scr)
            break

scores.sort()
print(scores)
print("Highest score : ", max(scores))
print("Lowest score : ", min(scores))
print("Average: " , sum(scores)/len(scores))
