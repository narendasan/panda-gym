# WARNING, This file will not be functional until stable-baselines3 is compatible
# with gymnasium. See https://github.com/DLR-RM/stable-baselines3/pull/780 for more information.
import gymnasium as gym
from stable_baselines3 import DDPG, HerReplayBuffer
from stable_baselines3.common.evaluation import evaluate_policy

import panda_gym

env = gym.make("PandaPushSafetyDagger-v3", reward_type="dense")

model = DDPG(policy="MultiInputPolicy", env=env, replay_buffer_class=HerReplayBuffer, verbose=1)

model.learn(total_timesteps=1000000)

model.save("trained_model")

mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")