import copy

d = {'name': 'derek', 'age': '22'}
c1 = copy.copy(d)
c2 = copy.deepcopy(d)

d['age'] = 25

print(d, c1, c2)

d = {'name': {'first': 'zhang', 'last': 'derek'},
     'job': ['IT', 'HR']}
c1 = copy.copy(d)
c2 = copy.deepcopy(d)

d['job'][0] = 'tester'

print(d, c1, c2)