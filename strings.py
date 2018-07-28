strings = ['This', 'List', 'is', 'now', 'all','together']
sentence = ''
combine = []
final = ''

#for i in strings:
#    if i == strings[-1]:
#        combine = combine + i + ' ';
#    else:
        
combine = strings[:-1]

for i in combine:
    sentence = sentence + i + ' '

final = sentence + strings[-1]

print(final)

print(' '.join(strings))
