from timeit import repeat
from string import digits
import random

KWARGS = {
    'number': 1000,
    'repeat': 5,
    'setup': """
from string import digits
import random
csv_data=", ".join(["".join(random.choice(digits) for _ in range(10)) for a in range(100)])
    """
}

print(repeat('list(map(int, csv_data.split(", ")))', **KWARGS))
# [0.02881924799294211, 0.029857174988137558, 0.02695651099202223, 0.022837748983874917, 0.02235270498204045]
print(repeat('[int(n) for n in csv_data.split(", ")]', **KWARGS))
# [0.036404724000021815, 0.03202701002010144, 0.03152783898985945, 0.0298233000212349, 0.029828407015884295]