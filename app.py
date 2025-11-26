import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="TruthLensAI",
    page_icon="🔍",
    layout="centered"
)

# ---------------- CUSTOM STYLING ----------------
st.markdown("""
<style>

/* Smooth, clean layout */
.block-container {
    padding-top: 2rem;
    max-width: 750px;
}

/* Title styling */
h1 {
    text-align: center;
    font-size: 2.6rem !important;
    color: #0A3D62;
    font-weight: 700;
}

/* Subheading */
h3 {
    color: #1B4F72;
    font-weight: 500;
}

/* Input fields */
textarea, input {
    border-radius: 8px !important;
    border: 1.8px solid #A9C5E8 !important;
    font-size: 1rem !important;
}

/* Button style */
.stButton button {
    border-radius: 8px;
    background-color: #0A3D62;
    color: white;
    font-size: 1.05rem;
    padding: 0.45rem 1rem;
    border: none;
    transition: 0.25s ease-in-out;
}

.stButton button:hover {
    background-color: #062D49;
}

</style>
""", unsafe_allow_html=True)

# ---------------- INTERFACE ----------------
st.title("🔍 TruthLensAI")
st.subheader("Fake News Detection Interface")

st.write("Please enter the news text below for verification:")

user_input = st.text_area("News Content", height=180)

if st.button("Analyze"):
    st.write("Processing your input...")
    # Your model logic here


