import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# Simple Spam Detector using
# Logistic Regression + TF-IDF
# -------------------------------

st.set_page_config(page_title="Logistic Regression — Binary Classifier", page_icon="🔍", layout="centered")
st.title("Logistic Regression — Binary Classifier (Spam / Not Spam)")
st.write("This demo trains a **Logistic Regression** model (with TF-IDF for text) on a tiny built-in dataset and lets you classify text as `spam` or `not spam`.")

# -------------------------------
# Tiny demo dataset (for quick local demo)
# -------------------------------
EXAMPLES = [
    ("Free entry in 2 a wkly comp to win FA Cup final tkts", "spam"),
    ("Hey — are we still meeting for lunch today?", "not_spam"),
    ("URGENT! Your mobile number has won $2000. Call now!", "spam"),
    ("Can you send me the notes from today's class?", "not_spam"),
    ("Lowest price on meds, order today and save big", "spam"),
    ("Don't forget to submit the assignment by 11pm.", "not_spam"),
    ("Win a brand new car! Click the link to claim.", "spam"),
    ("I'll be 10 minutes late — stuck in traffic.", "not_spam"),
    ("Your account has been suspended. Verify now.", "spam"),
    ("Happy birthday! Hope you have a great day 🙂", "not_spam"),
]

texts = [t for t, label in EXAMPLES]
labels = [1 if label == "spam" else 0 for t, label in EXAMPLES]

# -------------------------------
# Train / validate a tiny model on startup
# (This happens quickly because dataset is tiny)
# -------------------------------
vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df=1)
X = vectorizer.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate on the tiny test set
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

st.markdown(f"**Demo model trained on {len(EXAMPLES)} examples — toy demo only.**")
st.write(f"Validation accuracy (toy data): **{acc*100:.1f}%**")

# -------------------------------
# Single text prediction UI
# -------------------------------
st.header("Classify a single message")
user_text = st.text_area("Enter message text", value="Congratulations! You have won a prize")
if st.button("Predict"):
    if not user_text.strip():
        st.error("Please enter a message to classify.")
    else:
        x = vectorizer.transform([user_text])
        prob = model.predict_proba(x)[0]
        label = model.predict(x)[0]
        label_name = "spam" if label == 1 else "not spam"
        st.success(f"Prediction: **{label_name}**")
        st.write(f"Spam probability: **{prob[1]*100:.2f}%** — Not-spam probability: **{prob[0]*100:.2f}%**")

# -------------------------------
# Batch file upload for predictions
# -------------------------------
st.header("Batch predictions — upload CSV")
st.write("Upload a CSV with a column named `text`. The app will append `prediction` and `prob_spam` columns.")
uploaded = st.file_uploader("Upload CSV file", type=["csv"] )
if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        if 'text' not in df.columns:
            st.error("CSV must contain a column named 'text'.")
        else:
            X_batch = vectorizer.transform(df['text'].astype(str).values)
            probs = model.predict_proba(X_batch)[:,1]
            preds = (probs >= 0.5).astype(int)
            df['prediction'] = np.where(preds==1, 'spam', 'not_spam')
            df['prob_spam'] = probs
            st.write(df.head(20))
            csv = df.to_csv(index=False)
            st.download_button("Download predictions (CSV)", data=csv, file_name="predictions.csv", mime="text/csv")
    except Exception as e:
        st.error(f"Error reading CSV: {e}")

# -------------------------------
# Show example dataset and report
# -------------------------------
with st.expander("Show toy training examples and classification report"):
    df_examples = pd.DataFrame(EXAMPLES, columns=['text','label'])
    st.write(df_examples)
    report = classification_report(y_test, preds, target_names=['not_spam','spam'], zero_division=0)
    st.text(report)

st.caption("This is a tiny demo — for real spam detection you'd train on a large labeled dataset (e.g. SMS Spam Collection) and use proper evaluation.")
