# OpenAI Gym Tutorial

import gym
# 게임 환경 생성
env = gym.make('FrozenLake-v1')

# 게임을 Graphic으로 렌더링
# env.render()

# while True:
# 	key = inkey()
# 	if key not in arrow_keys.keys():
# 		print("Game aborted")
# 		break

# 	action = arrow_keys[key]

# 	"""
# 		Action에 따른 결과값 반환
		
# 		state : 현재 위치
# 		reward : 보상
# 		done : 게임이 끝났는지 여부
# 		Info : 게임 정보
# 	"""
# 	state, reward, done, info = env.step(action)
# 	env.render()
# 	print("S: ", state, "Action: ", action, "Reward: ", reward, "Info: ",info)

# 	if done:
# 		print("Finished with reward", reward)
# 		break