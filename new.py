import itertools

LIST = ['rugby', 'ginger', '8', 'august', 'james', 'jess', 'otto', '2011']

passwords = []

for i in range(1, len(LIST) + 1):
    for combination in itertools.permutations(LIST, i):
        passwords.append(''.join(combination))

for password in passwords:
    print(password)

with open('password_list.txt', 'w') as file:
    for password in passwords:
        file.write(password + "\n")