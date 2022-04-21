# python 3.7

# 에피소드가 종료되는 조건
# 막대기 각도 : -12도 ~ +12도
# 카트의 위치 : -2.4 ~ +2.4
# 시간 > 200

from gym import spaces

# 8개의 요소를 갖는 세트 {0, 1, 2, ..., 7}
space = spaces.Discrete(8)
x = space.sample()

print(space.contains(x))
print(space.n == 8)
