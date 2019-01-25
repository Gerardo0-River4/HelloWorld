word = "spercalifrigilisticexpialidocious"
alist = list(word)

print(alist)

new_list = []
for letter in alist:
    if letter not in new_list:
        new_list.append(letter)

print(new_list)


from gerardolib import elim_repeats

print(elim_repeats(alist))




