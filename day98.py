#Q-Learning
import numpy as np
import random

# Ortam tanımı (4x4 grid)
num_states = 16
num_actions = 4 

q_table = np.zeros((num_states, num_actions))

alpha = 0.1 # learning rate
gamma = 0.9 # discount factor
epsilon = 0.2 # exploration rate
episodes = 1000


rewards = np.zeros(num_states)
rewards[15] = 1  # hedef state

def get_next_state(state, action):
    if action == 0 and state >= 4:         
        return state - 4
    elif action == 1 and (state + 1) % 4 != 0:  
        return state + 1
    elif action == 2 and state < 12:    
        return state + 4
    elif action == 3 and state % 4 != 0:   
        return state - 1
    else:
        return state  

for episode in range(episodes):
    state = random.randint(0, num_states - 1)

    while state != 15: 
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, num_actions - 1)
        else:
            action = np.argmax(q_table[state])

        next_state = get_next_state(state, action)
        reward = rewards[next_state]

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = old_value + alpha * (reward + gamma * next_max - old_value)
        q_table[state, action] = new_value

        state = next_state

print("Öğrenilen Q Tablosu:")
print(q_table)

# Bu Q tablosu, ajanının 4x4 grid ortamında Q-learning algoritması ile öğrenmiş olduğu durum–aksiyon değerlerini göstermektedir.
# Hedef durum (state 15) terminal olduğu için bu durumun Q değerleri sıfırdır.
# Diğer durumlarda ise, hedefe yaklaştıkça özellikle doğru yönlerdeki aksiyonların Q değerlerinin arttığı görülmektedir.
