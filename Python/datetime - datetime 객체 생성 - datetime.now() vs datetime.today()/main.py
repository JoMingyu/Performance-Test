from timeit import repeat

KWARGS = {
    'setup': 'from datetime import datetime',
    'number': 100000,
    'repeat': 5
}

print(repeat('datetime.now()', **KWARGS))
# [0.07037944399053231, 0.05819433002034202, 0.05640839898842387, 0.0580228139879182, 0.0536179689806886]
print(repeat('datetime.today()', **KWARGS))
# [0.1369732620078139, 0.12346025000442751, 0.11891667699092068, 0.1174138079804834, 0.12986598801217042]