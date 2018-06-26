from timeit import repeat

KWARGS = {
    'setup': 'from datetime import datetime, date',
    'number': 100000,
    'repeat': 5
}

print(repeat('datetime.now().date()', **KWARGS))
# [0.08314683201024309, 0.0701644640066661, 0.06673972099088132, 0.06598724500508979, 0.06692519498756155]
print(repeat('date.today()', **KWARGS))
# [0.14072584098903462, 0.12500371798523702, 0.12156020899419673, 0.12681547499960288, 0.12752758999704383]