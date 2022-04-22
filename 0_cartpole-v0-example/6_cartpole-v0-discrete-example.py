from gym import spaces

space = spaces.Discrete(8)
x = space.sample()

print(space.contains(x))
print(space.n == 8)

'''

from gym import spaces

# 8개의 요소를 갖는 세트 {0, 1, 2, ..., 7}
space = spaces.Discrete(8)
x = space.sample()

print(space.contains(x))
print(space.n == 8)

'''