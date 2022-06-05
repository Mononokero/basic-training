import string
import random
dict_size = 7
keys1 = random.sample(string.ascii_lowercase, dict_size)
values1 = (random.randint(1, 20) for _ in range(dict_size))
d1 = dict_1 = dict(zip(keys1, values1))
print(dict_1)

dict_size = 7
keys2 = random.sample(string.ascii_lowercase, dict_size)
values2 = (random.randint(1, 20) for _ in range(dict_size))
d2 = dict_2 = dict(zip(keys2, values2))
print(dict_2)
same_keys = set(d1) & set(d2)
association = {key: d1[key]
                     if d1[key] > d2[key]
                     else d2[key]
                for key in same_keys}
association_result = d1.copy()
association_result.update(d2)
association_result.update(association)

print(association_result)

