names = ['Marlon', 'Karla', 'Ursula', 'Jose']
not_assistant = names.pop(1)

print(f'Invite to dinner with me {names[0]}')
print(f'Invite to dinner with me {names[1]}')
print(f'Not cant\'t make it to dinner {not_assistant}')
print(f'New invite to dinner with me is {names[2]}')
print('A larger table was found.')

names.insert(0, 'Hugo')
names.insert(int(len(names) / 2), 'Marcos')
names.append('Tatiana')

print(f'Invite to dinner with me {names[0]}')
print(f'Invite to dinner with me {names[1]}')
print(f'Invite to dinner with me {names[2]}')
print(f'Invite to dinner with me {names[3]}')
print(f'Invite to dinner with me {names[4]}')
print(f'Invite to dinner with me {names[5]}')
