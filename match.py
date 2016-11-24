import random

# contains tuples giving pairs that should not be matched
# (e.g. couples)
no_match = [
    ('mom', 'dad'),
    ('LL', 'C'),
    ('M', 'J')]

# contains strings giving names in gift train
people = ['mom', 'dad', 'LL', 'C', 'M', 'J']

givers = people[:]
receivers = people[:]
matches = []

for giver in givers:
    match = False
    while not match:
        r_index = random.randint(0, len(receivers) - 1)
        candidate = receivers[r_index]
        if (giver, candidate) and (candidate, giver) \
                not in no_match and giver != candidate:
            match = True
            matches.append((giver, candidate))
            receivers.pop(r_index)

print matches
