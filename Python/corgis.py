#import school_scores
#list_of_record = school_scores.get_all()

#print(list_of_record)

import suicide_attacks
import matplotlib.pyplot as plt
import numpy as np

list_of_attack = suicide_attacks.get_attacks()
ages = []
male = 0
female = 0
unknown = 0


for idx in range(len(list_of_attack)):
    gender = list_of_attack[idx]['attacker']['demographics']['gender']
    if gender == "Male":
        male += 1
    if gender == "Female":
        female += 1
    if gender == "Unknown":
        unknown += 1

objects = ("Male", "Female", "Unknown")

genders = [male, female, unknown]

y_pos = np.arange(len(objects))

s
plt.bar(y_pos, genders, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel("Number of People")
plt.title('Number of Attackers')
plt.show()
