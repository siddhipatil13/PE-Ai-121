import streamlit as st
import matplotlib.pyplot as plt

# App Title
st.set_page_config(page_title="Social Media Addiction Analyzer", page_icon="📱", layout="centered")
st.title("📱 Social Media Addiction Analyzer")
st.write("Analyze your social media habits and get personalized tips for digital balance!")

# --- User Inputs ---
st.subheader("🕒 Daily Usage & Habits")

time_spent = st.slider("How many hours do you spend daily on social media?", 0, 12, 2)
check_frequency = st.selectbox("How often do you check your social media?", 
                               ["Rarely", "Few times a day", "Every hour", "Constantly"])
mood_change = st.selectbox("Do you feel anxious or restless without checking social media?", 
                           ["Never", "Sometimes", "Often", "Always"])
sleep_effect = st.selectbox("Does social media affect your sleep schedule?", 
                            ["No", "A little", "Sometimes", "Yes, badly"])
productivity_effect = st.selectbox("Does social media affect your work/study focus?", 
                                   ["No", "A little", "Sometimes", "Yes, a lot"])

# --- Score Calculation ---
score = 0
score += time_spent * 2

# Frequency points
if check_frequency == "Few times a day":
    score += 5
elif check_frequency == "Every hour":
    score += 10
elif check_frequency == "Constantly":
    score += 15

# Mood effect
mood_points = {"Never": 0, "Sometimes": 5, "Often": 10, "Always": 15}
sleep_points = {"No": 0, "A little": 5, "Sometimes": 10, "Yes, badly": 15}
productivity_points = {"No": 0, "A little": 5, "Sometimes": 10, "Yes, a lot": 15}

score += mood_points[mood_change] + sleep_points[sleep_effect] + productivity_points[productivity_effect]

# --- Determine Level ---
if score < 25:
    level = "Low Addiction"
    color = "green"
    advice = "You have healthy control over your social media use. Keep it balanced!"
elif score < 50:
    level = "Moderate Addiction"
    color = "orange"
    advice = "Be mindful — try setting screen time limits and engage in offline hobbies."
else:
    level = "High Addiction"
    color = "red"
    advice = "You may be overusing social media. Consider a digital detox or set app limits."

# --- Display Results ---
st.markdown(f"### 🧩 Addiction Level: **: {level}**")
st.markdown(f"<p style='color:{color}; font-size:22px;'><b>{level}</b></p>", unsafe_allow_html=True)
st.write(advice)

# --- Visualization ---
labels = ['Social Media', 'Other Activities']
values = [min(score, 60), 60 - min(score, 60)]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, colors=['#FF6B6B', '#4ECDC4'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# --- Tips ---
st.subheader("💡 Tips for Healthy Digital Habits")
st.markdown("""
- Set daily time limits for apps.  
- Keep your phone away during meals or study.  
- Replace scrolling time with a hobby or short walk.  
- Avoid using your phone 1 hour before sleep.  
- Use “Do Not Disturb” or “Focus Mode” while working.
""")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Developed by Siddhi Patil | Simple AI Expert System Project 💻")
