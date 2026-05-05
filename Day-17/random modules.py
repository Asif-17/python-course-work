'''
import random

random.seed(40)  # Getting same output at many times, if not it gives random numbers with different outputs

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['java', 'python', 'AI', 'ML', 'SQL']

print(random.choice(l))
print(random.choices(l,k=2))

print("Before: ", l)
random.shuffle(l)
print("After: ", l)

'''


# Data Structures and Iteration Utilities
'''
import collections

s = 'python programming'


l = [1,2,4,5,6,4,2,3,8,3,2,6,8,0,9,0,8,6,4,2,1,3,4]

text = 'Heavy rain alert across these Indian states: What travellers need to know before planning a trip. Unfavorable weather conditions will be due to the presence of western disturbances, cyclonic circulations, and active troughs prevailing in the region. This weather activity is estimated until May 8, during which many states may receive heavy rainfall, thunderstorms, and high-speed winds.'

print(collections.Counter(text.split()))

print(collections.Counter(s))
print(collections.Counter(l))
'''

'''
d = collections.defaultdict(int)
for i in s:
    d[i] += int(1)

print(d)
'''

'''
import collections

d = collections.deque([])

d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(60)
d.append(100)
d.popleft()
d.popleft()
d.append(200)
d.append(300)
d.popleft()
d.append(90)
d.append(600)
d.append(500)
d.popleft()

print(d)


d = collections.deque([])

d.appendleft(10)
d.appendleft(20)
d.appendleft(30)
d.appendleft(40)
d.pop()
d.pop()
d.appendleft(60)
d.appendleft(100)
d.pop()
d.pop()
d.appendleft(200)
d.appendleft(300)
d.pop()
d.appendleft(90)
d.appendleft(600)
d.appendleft(500)
d.pop()

print(d)
'''


import itertools

print(list(itertools.combinations('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
