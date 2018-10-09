def no_duplicates(list):
    length_list = len(list)
    b = set()
    for i in list:
        if i not in b:
            b.add(i)
    return b


def duplicates(list):
    no_dups = set(list)
    return no_dups


list = ['cat', 'dog', 'horse', 'sheep', 'horse', 'elephant', 'horse', 'lion', 'dog', 'tiger']
print('Unique Animal Names: ', no_duplicates(list))
print('Repeated Animal Names:', duplicates(list))
