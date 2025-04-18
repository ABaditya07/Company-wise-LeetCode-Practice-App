import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Company-wise LeetCode Practice", layout="wide")

COMPANY_DIR = 'companies'

# ----- Sidebar -----
st.sidebar.title("📁 Select Filters")
companies = sorted([d for d in os.listdir(COMPANY_DIR) if os.path.isdir(os.path.join(COMPANY_DIR, d))])
selected_company = st.sidebar.selectbox("🏢 Select Company", companies)

if selected_company:
    folder_path = os.path.join(COMPANY_DIR, selected_company)
    csv_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])
    period = st.sidebar.selectbox("⏳ Time Period", csv_files)

# ----- Background Image and Title Section -----
st.markdown("""
    <style>
        body {
            background-image: url('https://avatars.githubusercontent.com/u/41718343?s=280&v=4');
            background-size: cover;
            background-position: center;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .header {
            text-align: center;
            color: #4e73df;
            font-size: 40px;
            font-weight: bold;
            background: linear-gradient(to right, #FF6B6B, #FFD93D, #6BCB77);
            padding: 15px;
            border-radius: 15px;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: #FF6B6B;
            font-size: 14px;
            font-weight: bold;
        }
    </style>
    <div class="header">
        👨‍💻 Company-wise LeetCode Practice App
    </div>
    <div class="footer">
        Made with ❤️ by Aditya
    </div>
""", unsafe_allow_html=True)

# ----- Difficulty Filter -----
difficulty_options = ['All', 'Easy', 'Medium', 'Hard']
selected_difficulty = st.sidebar.selectbox("🎯 Select Difficulty Level", difficulty_options)

# ----- Display Questions -----
if selected_company and period:
    file_path = os.path.join(folder_path, period)
    df = pd.read_csv(file_path)

    # Handle different column names
    if 'Question' in df.columns:
        df.dropna(subset=['Question', 'Link'], inplace=True)
        df.drop_duplicates(subset=['Question'], inplace=True)
        question_col = 'Question'
    elif 'Title' in df.columns:
        df.dropna(subset=['Title', 'Link'], inplace=True)
        df.drop_duplicates(subset=['Title'], inplace=True)
        df.rename(columns={'Title': 'Question'}, inplace=True)
        question_col = 'Question'
    else:
        st.error("❌ CSV must contain a 'Question' or 'Title' column.")
        st.stop()

    # Check if 'Difficulty' column exists
    if 'Difficulty' not in df.columns:
        st.error("❌ The dataset does not contain a 'Difficulty' column.")
        st.stop()

    # Normalize Difficulty column to handle any case inconsistencies
    df['Difficulty'] = df['Difficulty'].str.strip().str.lower()

    # Apply difficulty filter if not 'All'
    if selected_difficulty != 'All':
        selected_difficulty = selected_difficulty.lower()
        df = df[df['Difficulty'] == selected_difficulty]

    st.markdown(f"### 📋 Showing {len(df)} Questions for **{selected_company}** ({period.replace('.csv', '')})")

    # Split into two columns for better layout
    col1, col2 = st.columns(2)

    for i, row in df.iterrows():
        target_col = col1 if i % 2 == 0 else col2

        freq = row.get('Frequency', 'N/A')
        freq_style = "background-color:#FF6B6B" if freq != 'N/A' and freq >= 500 else "background-color:#FFD93D" if freq != 'N/A' and freq >= 100 else "background-color:#6BCB77"

        card_html = f"""
        <div style="border: 1px solid #e6e6e6; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); transition: transform 0.3s ease-in-out;">
            <h4 style="margin-bottom: 8px; font-size: 18px; color: #4e73df; font-weight: bold; text-transform: uppercase;">{i+1}. {row[question_col]}</h4>
            <a href="{row['Link']}" target="_blank" style="color:#1f77b4; text-decoration:none; font-weight: 600;">🔗 View on LeetCode</a><br>
            <span style="{freq_style}; padding: 4px 8px; border-radius: 5px; color: white;">🔥 Frequency: {freq}</span>
        </div>
        """

        # Hover effect: on hover, the card will slightly scale up
        target_col.markdown(f'<div style=":hover{{transform: scale(1.05);}}">{card_html}</div>', unsafe_allow_html=True)

    # Show filtered count message with a custom gradient effect
    filtered_count = len(df)
    st.markdown(f"<h4 style='color:#4e73df;'>🧐 Showing {filtered_count} questions with difficulty **{selected_difficulty.capitalize()}**</h4>", unsafe_allow_html=True)
