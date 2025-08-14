#student grade tracker

#dictionary for student names and scores
names_scores = {
    "Amani":56,
    "Riziki":78,
    "Rose":90,
    "John":65,
    "Benue":49,
    "Prince":88,
    "Joyce":56,
    "Gaby":57,
    "Ireen":78,
    "Paul":90
}

#calculating average test score
#average = sum(names_scores.values())/len(names_scores)
total_score = 0
for i in names_scores.values():
    total_score += i
number_of_student = len(names_scores)
average_score = total_score/number_of_student
print(f"The average score is {average_score}")

print("")

#updating score
names_scores["Joyce"] = 100        

#highest score
for i, v in names_scores.items():
    if v == max(names_scores.values()):
        print(f"{i} has the highest score")

print("")

#score more than 80
print("The following have the score greater than 80:")

for i, v in names_scores.items():
    if v > 80 :
        print(i) 