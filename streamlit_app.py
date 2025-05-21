import streamlit as st
import pandas as pd
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from promptlist import evaluation_prompts

# === Streamlit Page Config ===
st.set_page_config(page_title="Instruction Evaluation", layout="wide")

st.title("🧠 Instruction Evaluation Interface")
st.markdown("Evaluate the quality of AI-generated instructions based on a user prompt. Submit your feedback below.")

# === Load evaluation prompts and instructions ===
@st.cache_data
def load_data():
    df = pd.read_csv("evaluation_results.csv")
    return df

df = load_data()

# === Prompt Selection ===
prompt_idx = st.number_input("Select Prompt #", 0, len(df) - 1, 0)
row = df.iloc[prompt_idx]

# === Display Prompt ===
with st.expander("🔎 Full Prompt Text", expanded=True):
    st.markdown(evaluation_prompts[prompt_idx]["prompt"])

def render_instructions(title, instructions_text):
    st.markdown(f"### {title}")
    for line in instructions_text.split("\n"):
        line = line.strip()
        if line.startswith("INSTRUCTION"):
            st.markdown(f"- **{line}**")
        elif line:
            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{line}")  # small indent for overflow lines

# === Display Instructions ===
col1, col2, col3 = st.columns(3)

with col1:
    render_instructions("🔷 Approach 1", row['gnn_instructions'])

with col2:
    render_instructions("🔶 Approach 2", row['mcts_instructions'])

with col3:
    render_instructions("🟢 Approach 3", row['rmodel_instructions'])

# === Evaluation Form ===
st.markdown("### ✍️ Rate Each Approach")

def rating_block(label_prefix):
    st.markdown(f"#### {label_prefix.upper()}")
    return {
        f"{label_prefix}_user": st.slider("User Alignment", 1, 5, 3, key=f"{label_prefix}_user_slider"),
        f"{label_prefix}_clarity": st.slider("Clarity", 1, 5, 3, key=f"{label_prefix}_clarity_slider"),
        f"{label_prefix}_action": st.slider("Actionability", 1, 5, 3, key=f"{label_prefix}_action_slider"),
        f"{label_prefix}_usefulness": st.slider("Usefulness", 1, 5, 3, key=f"{label_prefix}_usefulness_slider")
    }

st.markdown("Rate on a scale of 1 (poor) to 5 (excellent).")

gnn_scores = rating_block("Approach1")
mcts_scores = rating_block("Approach2")
rmodel_scores = rating_block("Approach3")

# === Submit Button ===
evaluator_id = st.text_input("Your name or initials (required)", "")
submit = st.button("✅ Submit Evaluation")

# === Google Sheets Logic ===
if submit:
    if not evaluator_id.strip():
        st.warning("Please enter your name or initials before submitting.")
    else:
        try:
            # === Authenticate with Google Sheets ===
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_dict(
                st.secrets["gcp_service_account"],
                scopes=scope
            )
            client = gspread.authorize(credentials)

            # === Open sheet and append row ===
            sheet = client.open("Instruction Evaluation Feedback").sheet1
            row_data = {
                "timestamp": datetime.utcnow().isoformat(),
                "evaluator": evaluator_id,
                "prompt_idx": prompt_idx,
                "title": row['title'],
                "domain": row['domain'],
                "prompt": row['prompt'],
                **gnn_scores,
                **mcts_scores,
                **rmodel_scores
            }

            sheet.append_row(list(row_data.values()))
            st.success("✅ Evaluation submitted. Thank you!")
        except Exception as e:
            st.error(f"Error submitting evaluation: {e}")
