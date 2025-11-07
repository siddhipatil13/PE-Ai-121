import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Q-Learning Game AI", page_icon="🎮", layout="centered")

st.title(" Q-Learning Game AI")
st.write("This demo shows how Q-Learning helps an agent learn to reach the goal in a grid environment.")

# -------------------------------
# Environment setup
# -------------------------------
grid_size = 4
goal_state = (3, 3)
actions = ["up", "down", "left", "right"]
Q = np.zeros((grid_size, grid_size, len(actions)))

def get_next_state(state, action):
    x, y = state
    if action == "up" and x > 0: x -= 1
    elif action == "down" and x < grid_size - 1: x += 1
    elif action == "left" and y > 0: y -= 1
    elif action == "right" and y < grid_size - 1: y += 1
    return (x, y)

def get_reward(state):
    return 1 if state == goal_state else -0.04

# -------------------------------
# Q-Learning parameters
# -------------------------------
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # exploration rate
episodes = st.slider("Number of Episodes", 10, 200, 50)

train = st.button(" Train the Agent")

if train:
    st.write("Training in progress...")
    for episode in range(episodes):
        state = (0, 0)
        done = False
        while not done:
            if np.random.rand() < epsilon:
                action_idx = np.random.randint(len(actions))
            else:
                action_idx = np.argmax(Q[state[0], state[1]])
            next_state = get_next_state(state, actions[action_idx])
            reward = get_reward(next_state)
            Q[state[0], state[1], action_idx] += alpha * (reward + gamma * np.max(Q[next_state[0], next_state[1]]) - Q[state[0], state[1], action_idx])
            state = next_state
            if state == goal_state:
                done = True
        time.sleep(0.01)
    st.success("✅ Training complete!")

    st.subheader("Q-Table (Max Q-value for each state)")
    Q_table = np.max(Q, axis=2)
    st.dataframe(Q_table)

    st.write(" Goal is at position (3,3). The agent starts at (0,0).")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Developed by Siddhi Patil ")
