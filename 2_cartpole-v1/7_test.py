# import random

# for _ in range(10):
#     print(_, random.randrange(4, 6))

# for _ in range(10):
#     print(_, random.random())


from keras.models                import Sequential
from keras.layers                import Dense
from tensorflow.keras.optimizers import Adam

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def build_model():
  model = Sequential()
  model.add(Dense(128, input_dim = 4, activation = 'relu'))
  model.add(Dense(64, activation = 'relu'))
  model.add(Dense(32, activation = 'relu'))
  model.add(Dense(16, activation = 'relu'))
  model.add(Dense(2, activation = 'softmax'))
  model.compile(loss='mse', optimizer = Adam())
  return model

print(build_model())