# import necessary modeules
import random
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display
import time
from PIL import Image
from gym import spaces

# creating the maze env
class MazeEnv():
    
    def __init__(self, maze, start=(0, 0)):
        super(MazeEnv, self).__init__()

        self.maze = maze
        self.start = start
        self.end =(self.maze.shape[0]-1, self.maze.shape[1]-1) #end point of maze is bottom right of the maze.
        self.current_pos = self.start
        self.agent_pos = self.start
       
        self.action_space = [0,1,2,3] # 4 actions , up ,down ,left and right
        self.observation_space = spaces.Box(low=0, high=255, shape=(10, 10, 2))

    def reset(self): #reset the agent position to start
        self.current_pos = self.start
        self.agent_pos = self.start 
        obs = self._get_obs()
        return obs

    def step(self, action): #gives new state,reward and if the maze is solved or not, after taking action a in current state
        new_pos = self._get_new_pos(action)
        reward = self._get_reward(new_pos)
        done = self._get_done(new_pos)
        if self.maze[new_pos] == 0:
            self.current_pos = new_pos
            self.agent_pos = new_pos 
        obs = self._get_obs()
        return obs, reward, done, {}

    def render(self, mode='human'): #renders the maze and the agent
        if mode not in ['rgb_array', 'human']:
            raise ValueError(f"Invalid input '{mode}'. Mode must be either 'rgb_array' or 'human'.")
        if mode == 'rgb_array':
            img = np.zeros((self.maze.shape[0], self.maze.shape[1], 3))
            img[self.maze == 1] = [1, 1, 1]
            img[self.agent_pos[0], self.agent_pos[1]] = [0, 0, 1]
            if self.start == self.agent_pos:
                pass
            else:
                img[self.start[0], self.start[1]] = [255, 0, 0]
            if self.end==self.agent_pos:
                pass
            else:
                img[self.end[0], self.end[1]] = [0, 255, 0]
            img = np.clip(img, 0, 1)
            return img
        elif mode == 'human':
            img = self.render(mode='rgb_array')
            plt.imshow(img)
            plt.show()
            plt.clf()
            

    def _get_obs(self):  #gives the observation from maze 
        obs = np.zeros(self.maze.shape + (2,))
        obs[self.maze == 1] = [0, 0]
        obs[self.maze == 0] = [255, 255]
        obs[self.start] = [0, 255]
        obs[self.end] = [255, 0]
        obs[self.agent_pos] = [255, 255]
        return obs

    def _get_new_pos(self, action): #new position of agent after taking action a
        row, col = self.current_pos
        if action == 0: # move up
            row = max(row-1, 0)  
        elif action == 1: # move down
            row = min(row+1, self.maze.shape[0]-1)  
        elif action == 2: # move left
            col = max(col-1, 0)  
        elif action == 3: # move right
            col = min(col+1, self.maze.shape[1]-1)  
        return (row, col)

    def _get_reward(self, new_pos): #reward associated with states
        if new_pos == self.end:
            return 100
        elif self.maze[new_pos[0], new_pos[1]] == 1:
            return -100
        else:
            return -1
        

    def _get_done(self, new_pos):
        return new_pos == self.end

#defining the maze, 0 means free path and 1 means walls
maze = np.array([[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                  [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])


# if image input is given then solve the image maze by converting it first into numpy array , and if image input is not given then solve the numpy array maze. 
try:
    maze_image = Image.open('sample.png').convert('L')

    threshold_value = 128
    maze_binary = maze_image.point(lambda x: 255 if x > threshold_value else 0, mode='1')
    
    maze_resized = maze_binary.resize((10, 10), resample=Image.BILINEAR)
    
    maze_array = 1 - np.array(maze_resized)
    env = MazeEnv(maze_array, start=(0,0))
    
except:
    env= MazeEnv(maze,start=(0,0))
