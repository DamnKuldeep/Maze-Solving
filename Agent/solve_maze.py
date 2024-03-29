#define the agent

class agent:
    def __init__(self,env):
        self.q_table = np.zeros((env.observation_space.shape[0], env.observation_space.shape[1], len(env.action_space)))
        alpha = 0.1  #learning rat
        gamma = 0.99  #discount factor
        epsilon = 1.0  #for greedy policy
        max_epsilon = 1.0
        min_epsilon = 0.01
        decay = 0.001
        self.env=env
        num_episodes = 1000
        for i in range(num_episodes):
            state = env.reset()
            done = False
            for j in range(200):
                if np.random.uniform() < epsilon:  #exploring the env
                    action = random.choice(env.action_space)
                else:
                    action = np.argmax(self.q_table[env.agent_pos[0], env.agent_pos[1], :])    #exploitation
                b,c =env.agent_pos[0], env.agent_pos[1]
                next_state, reward, done, info = env.step(action)
                if done:
                    break
                    
                # Updating the q table
                old_value = self.q_table[b , c, action]
                next_max = np.max(self.q_table[env.agent_pos[0], env.agent_pos[1], :])
                new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
                self.q_table[b , c, action] = new_value  
                state = next_state  # updating the new_state
                
            # defining epsilon decay
            epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay *i)
     
    # Use the final q table to solve the maze optimally
    def solve_maze(self):     
            state = env.reset()
            total_reward=0
            done = False
            i=0
            self.plots= []
            while not done:
                prev_pos = self.env.agent_pos
                self.plots.append(plt.gcf())  # collecting the plots of agent position to make a video of it in future
                self.env.render()  # render the current maze and agent position
                action = np.argmax(self.q_table[self.env.agent_pos[0], self.env.agent_pos[1], :]) # choosing the optimal action from the q table for a state
                state, reward, done, info = self.env.step(action) # taking the action
                total_reward+=reward  # cummulating the reward
                mem.append(self.env.agent_pos)
                if max(mem.count(item) for item in mem)==5: # if the agent moves in a repetetive pattern then break the loop and print that maze couldn't be solved
                    break
                if self.env.agent_pos == prev_pos: # if agent is stuck inside the maze and no further move is possible then say that maze is not solvable
                    i+=1
                    if i==10:
                        break
                time.sleep(0.5) #time delay between rendering the plots
                display.clear_output(wait=True) # clearing the display
                
            if done:
                self.plots.append(plt.gcf())
                self.env.render()
                print(f"Maze Solved\nTotal Reward: {total_reward}")
            else:
                print("The Maze is not solvable")
        
            
        

Agent=agent(env)  # calling the agent and training it for optimal policy

Agent.solve_maze() # show the agent solving the maze using optimal policy
