from timeit import repeat

KWARGS = {
    'number': 10000,
    'repeat': 5,
    'setup': """
import json
import ujson

from string import ascii_letters, digits
import random

stringset = ascii_letters + digits

data_l = [''.join(random.choice(stringset) for _ in range(10)) for _ in range(100)]
data_d = {i: ''.join(random.choice(stringset) for _ in range(10)) for i in range(100)}
data_f = [random.random() for _ in range(100)]

data_l_stringified = json.dumps(data_l)
data_d_stringified = json.dumps(data_d)
data_f_stringified = json.dumps(data_f)
    """
}

print(repeat('json.dumps(data_l)', **KWARGS))
# [0.16449891400407068, 0.15151556502678432, 0.1580125449982006, 0.13814390401239507, 0.13809025898808613]
print(repeat('json.dumps(data_d)', **KWARGS))
# [0.31244211399462074, 0.3074658520054072, 0.3076737579831388, 0.3076680740050506, 0.3053465289995074]
print(repeat('json.dumps(data_f)', **KWARGS))
# [0.813023291004356, 0.8196172130119521, 0.8107744549924973, 0.7918939179799054, 0.8122157570032869]

print(repeat('ujson.dumps(data_l)', **KWARGS))
# [0.054413408011896536, 0.0499865919991862, 0.049398870003642514, 0.048787591978907585, 0.04701138898963109]
print(repeat('ujson.dumps(data_d)', **KWARGS))
# [0.16578996198950335, 0.1591447219834663, 0.15536322799744084, 0.16273736098082736, 0.15820176698616706]
print(repeat('ujson.dumps(data_f)', **KWARGS))
# [0.09479062299942598, 0.08573945998796262, 0.0891747290152125, 0.08534200099529698, 0.07922276100725867]

print(repeat('json.loads(data_l_stringified)', **KWARGS))
# [0.14022801499231718, 0.1321180430240929, 0.12534076999872923, 0.126832166017266, 0.12910146699869074]
print(repeat('json.loads(data_d_stringified)', **KWARGS))
# [0.350889630994061, 0.3953926430258434, 0.3161686850071419, 0.30888778300140984, 0.3175698019913398]
print(repeat('json.loads(data_f_stringified)', **KWARGS))
# [0.4083907899912447, 0.4036920420185197, 0.42496011199546047, 0.42815691299620084, 0.4169838969828561]

print(repeat('ujson.loads(data_l_stringified)', **KWARGS))
# [0.08476997198886238, 0.0892553589947056, 0.08215457299957052, 0.08539851897512563, 0.08222576102707535]
print(repeat('ujson.loads(data_d_stringified)', **KWARGS))
# [0.20141622400842607, 0.19701883601373993, 0.18553137499839067, 0.19435178601997904, 0.20086168599664234]
print(repeat('ujson.loads(data_f_stringified)', **KWARGS))
# [0.0635028760007117, 0.06082623399561271, 0.06606179801747203, 0.06481575599173084, 0.06025002500973642]