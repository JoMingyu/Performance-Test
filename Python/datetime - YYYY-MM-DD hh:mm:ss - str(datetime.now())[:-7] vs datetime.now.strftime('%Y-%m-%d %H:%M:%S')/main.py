from timeit import repeat

KWARGS = {
    'setup': 'from datetime import datetime',
    'number': 100000,
    'repeat': 5
}

print(repeat('str(datetime.now())[:-7]', **KWARGS))
# [0.21474009499070235, 0.19047646300168708, 0.1964569199772086, 0.19521897000959143, 0.18940392701188102]
print(repeat('datetime.now().strftime("%Y-%m-%d %H:%M:%S")', **KWARGS))
# [0.4531171690032352, 0.4316533110104501, 0.4431185509893112, 0.4436805319855921, 0.43941104601253755]