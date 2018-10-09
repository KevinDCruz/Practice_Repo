from operator import itemgetter
names = [
    {'fname': 'Kevin', 'lname': 'DCruz'},
    {'fname': 'Kevin', 'lname': 'NCruz'},
    {'fname': 'Fevin', 'lname': 'BCruz'},
    {'fname': 'Gevin', 'lname': 'VCruz'},
    {'fname': 'Bevin', 'lname': 'CCruz'},
    {'fname': 'aevin', 'lname': 'YCruz'},
    {'fname': 'Gevin', 'lname': 'RCruz'},
    {'fname': 'Yevin', 'lname': 'ECruz'},
    {'fname': 'Bevin', 'lname': 'WWCruz'},
    {'fname': 'Xevin', 'lname': 'QCruz'}
]


for i in sorted(names, key=itemgetter('fname', 'lname')):
    print(i)
