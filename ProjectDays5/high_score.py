import random

random_list = random.sample(range(1, 101), 10)
print(random_list)

score = 0
for i in random_list:
    if i > score:
        score = i

print(score)

