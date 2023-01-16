n = int(input())
members = input().split()
bads = set(input().split())
excellents = []
num_excellents = 0
for member in members:
    if member not in bads:
        excellents.append(member)
for excellent in excellents:
    excell = {}
    for letter in excellent:
        if letter not in excell:
            excell[letter] = 1
        else:
            excell[letter] +=1
    is_same = True
    first_letter_count = excell[excellent[0]]
    for l in excell:
        if excell[l] != first_letter_count:
            is_same= False
    if is_same:
        num_excellents +=1
print(num_excellents)