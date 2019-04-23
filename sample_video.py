import cv2

writer = cv2.VideoWriter("eps.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30, (320,240), True)
import gym
import vizdoomgym
env = gym.make("VizdoomTakeCover-v0")
obs = env.reset()
while True:
	obs = cv2.cvtColor(obs, cv2.COLOR_RGB2BGR)
	writer.write(obs)
	obs, _, done, _ = env.step(env.action_space.sample())
	if done:
		break
writer.release()
