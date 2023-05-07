class agent:
    def __init__(self,env):
        self.q_table = np.zeros((env.observation_space.shape[0], env.observation_space.shape[1], len(env.action_space)))
        
        alpha = 0.1  
        gamma = 0.99  
        epsilon = 1.0  
        max_epsilon = 1.0
        min_epsilon = 0.01
        decay = 0.001
        self.env=env
        
        num_episodes = 1000
        for i in range(num_episodes):
            state = env.reset()
            done = False
            
            for j in range(200):
                if np.random.uniform() < epsilon:
                    action = random.choice(env.action_space)
                else:
                    action = np.argmax(self.q_table[env.agent_pos[0], env.agent_pos[1], :])  
                    
                
                b,c =env.agent_pos[0], env.agent_pos[1]
                next_state, reward, done, info = env.step(action)
                if done:
                    break
                
                old_value = self.q_table[b , c, action]
                next_max = np.max(self.q_table[env.agent_pos[0], env.agent_pos[1], :])
                new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
                self.q_table[b , c, action] = new_value
                
                state = next_state
            
            epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay *i)
            
    def solve_maze(self):     
            state = env.reset()
            total_reward=0
            done = False
            i=0
            mem = []
            self.plots= []
            while not done:
                prev_pos = self.env.agent_pos
                self.plots.append(plt.gcf())
                self.env.render()
                action = np.argmax(self.q_table[self.env.agent_pos[0], self.env.agent_pos[1], :])
                state, reward, done, info = self.env.step(action)
                total_reward+=reward
                mem.append(self.env.agent_pos)
                if max(mem.count(item) for item in mem)==5:
                    break
                if self.env.agent_pos == prev_pos:
                    i+=1
                    if i==10:
                        break
                time.sleep(0.5)
                display.clear_output(wait=True)
                
            if done:
                self.plots.append(plt.gcf())
                self.env.render()
                print(f"Maze Solved\nTotal Reward: {total_reward}")
            else:
                print("The Maze is not solvable")
        
            
        

Agent=agent(env)

Agent.solve_maze()
