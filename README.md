# Maze-Solving
This is a model based on Reinforcement learning to solve Mazes, taking input as a numpy array or an image.

Project by ArIES(Artificial Intelligence & Electronic Society)

Team members - Kuldeep, Yashwanth, Anupriya, Ishaan Garg & Pranav 

# Requirements
The MazeEnv class requires the following packages to be installed:

1. numpy

2. matplotlib

3. Pillow

4. gym

5. ipython

6. opencv-python-headless

# MazeEnv
MazeEnv is a Python class that represents a simple 2D maze environment. The environment is grid-based, with the grid represented as a 2D numpy array. The environment includes a start point, an end point, and walls that cannot be traversed.

Example input of maze - 

![alt text](https://i.stack.imgur.com/nedrk.jpg)



# Usage
We have a MazeEnv class that defines the environment for a maze game. The class is a subclass of gym.Env which is the base class for all OpenAI gym environments. The MazeEnv has an observation space, an action space, and a set of methods that define how the environment behaves, such as reset() and step().

The maze variable at the end of the script is a NumPy array that represents the maze. It is a 2D array where each element can be either 0 or 1. A value of 0 indicates an open cell that the agent can move to, and a value of 1 indicates a blocked cell that the agent cannot move to. The starting position of the agent is the top left corner (0,0), and the ending position is the bottom right corner.

The render() method of the MazeEnv class can be used to visualize the environment. It takes an argument mode which can be either 'human' or 'rgb_array'. If mode is 'human', it displays the maze as an image using the Matplotlib library. If mode is 'rgb_array', it returns a NumPy array that represents the maze as an RGB image.

To use the MazeEnv class, you would need to create an instance of the class by passing in the maze array and optionally the starting position of the agent. You can then call the reset() method to initialize the environment, and the step() method to perform an action and receive an observation, reward, and done signal. You can also call the render() method to visualize the environment.




# The MazeEnv class has the following methods:

1. reset()
Resets the environment to its initial state and returns the initial observation.

2. step(action)
Performs the given action in the environment and returns the new observation, reward, done flag, and a dictionary of extra information.

3. render(mode='human')
Renders the environment in the given mode. The available modes are 'human' and 'rgb_array'.

4. _get_obs()
Returns the current observation of the environment.

5. _get_new_pos(action)
Given an action, returns the new position of the agent if the action is taken.

6. _get_reward(new_pos)
Given a new position, returns the reward associated with moving to that position.

7. _get_done(new_pos)
Given a new position, returns a boolean flag indicating whether the environment is in a terminal state.


# The agent:-
The agent gets trained using greedy policy , and updates the q table for max return associated with the state-action pair, this happens for 100 epsiodes and we finally get the optimal policy.

after that we use the optimal policy and make the agent follow optimal policy and renders the maze environment on display which shows the course of action of agent to solve the maze.


CLICK HERE TO SEE THE FINAL PROJECT: -

  https://damnkuldeep-mazesolvingusingrl-mazesolver-gajetg.streamlit.app/
