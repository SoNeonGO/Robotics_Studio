import os
import time
from stable_baselines3.common.utils import set_random_seed
from bienv import BipEnv
from stable_baselines3 import PPO
from Sim.sim import Sim


def train():
    save_dir = "log/m1/"
    bipedal = Sim(model='./urdf/bluebody-urdf.xml', dt=0.01)
    vec_env = BipEnv(bipedal)
    model = PPO("MlpPolicy", vec_env, verbose=1, batch_size=1000)
    model.learn(total_timesteps=10000)
    model.save(save_dir)


if __name__ == "__main__":
    train()
