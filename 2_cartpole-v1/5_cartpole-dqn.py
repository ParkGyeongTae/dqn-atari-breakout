import numpy as np
import tensorflow as tf
import random
# import dqn
from collections import deque

import gym
env = gym.make('CartPole-v1')

input_size  = env.observation_space.shape[0]
output_size = env.action_space.n

dis = 0.9
REPLAY_MEMORY = 50000

class DQN:
  def __init__(self, session, input_size, output_size, name = 'main'):
    self.session     = session
    self.input_size  = input_size
    self.output_size = output_size
    self.net_name    = name
    self._build_network()

  def _build_network(self, h_size = 10, l_rate = 0.1):
    with tf.variable_scope(self.net_name):
      self._X = tf.placeholders(
        tf.float32, [None, self.input_size], name = 'input_x'
      )
      W1 = tf.get_variable('W1', shape = [self.input_size, h_size],
                            initializer = tf.contrib.layers.xavier_initializer())
      layer1 = tf.nn.tanh(tf.matmul(self._X, W1))
      W2 = tf.get_variable('W2', shape = [self.input_size, h_size],
                            initializer = tf.contrib.layers.xavier_initializer())
      self._Qpred = tf.matmul(layer1, W2)
    self._Y = tf.placeholder(
      shape = [None, self.output_size], dtype = tf.float32
    )
    self._loss = tf.reduce_mean(tf.square(self._Y - self._Qpred))
    self._train = tf.train.AdamOptimizer(
      learning_rate = l_rate).minimize(self._loss)
  
  def predict(self, state):
    x = np.reshape(state, [1, self.input_size])
    return self.session.run(self._Qpred, feed_dict = {self._X: x})
  
  def update(self, x_stack, y_stack):
    return self.session.run([self._loss, self._train], feed_dict = {
      self._X: x_stack, self._Y: y_stack
    })

def replay_train(mainDQN, targetDQN, train_batch):
  x_stack = np.empty(0).reshape(0, input_size)
  y_stack = np.empty(0).reshape(0, output_size)
  for state, action, reward, next_state, done in train_batch:
    Q = mainDQN.predict(state)
    if done:
      Q[0, action] = reward
    else:
      Q[0, action] = reward + dis * np.max(targetDQN.predict(next_state))
    y_stack = np.vstack([y_stack, Q])
    x_stack = np.vstack([x_stack, state])
  return mainDQN.update(x_stack, y_stack)

def get_copy_var_ops(*, dest_scope_name = 'target', src_scope_name = 'main'):
  op_holder = []
  src_vars = tf.get_collections(
    tf.GraphKeys.TRAINABLE_VARIABLES, scope = src_scope_name)
  dest_vars = tf.get_collection(
    tf.GraphKeys.TRAINABLE_VARIABLES, scope = dest_scope_name)
  for src_var, dest_var in zip(src_vars, dest_vars):
    op_holder.append(dest_var.assign(src_var.value()))

def bot_play(mainDQN):
  s = env.reset()
  reward_sum = 0
  while True:
    env.render()
    a = np.argmax(mainDQN.predict(s))
    s, reward, done, _ = env.step(a)
    if done:
      print('Total score: {}'.format(reward_sum))
      break

