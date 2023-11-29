# WARNING, This file will not be functional until stable-baselines3 is compatible
# with gymnasium. See https://github.com/DLR-RM/stable-baselines3/pull/780 for more information.
import gymnasium as gym
from gymnasium.utils.play import play
from stable_baselines3 import DDPG, HerReplayBuffer
import numpy as np

import panda_gym

env = gym.make("PandaPushSafetyDagger-v3")

play(gym.make("PandaPushSafetyDagger-v3", render_mode="rgb_array"), keys_to_action={
                                               "w": np.array([ 0.5,  0.,  0.]),
                                               "s": np.array([-0.5,  0.,  0.]),
                                               "a": np.array([  0.,-0.5,  0.]),
                                               "d": np.array([  0., 0.5,  0.]),
                                               "q": np.array([  0.,  0., -0.5]),
                                               "e": np.array([  0.,  0., -0.5]),
                                              }, noop=np.array([0,0,0]))