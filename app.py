import streamlit as st
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="TruthLensAI", layout="wide")

# -------------------- CUSTOM CSS --------------------
st.markdown(
    """
    <style>
        /* Background gradient */
        .main {
            background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
            color: white;
        }

        /* Headings */
        h1, h2, h3, h4, h5 {
            color: white !important;
        }

        /* Radio label text white */
        div[role="radiogroup"] label {
            color: white !important;
            font-weight: 500;
        }

        /* Translucent white box */
        .translucent-box {
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.25);
            margin-top: 20px;
        }

        /* Navigation buttons */
        .nav-btn {
            background: rgba(255,255,255,0.12);
            color: white !important;
            padding: 10px 18px;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.25);
            text-decoration: none;
            font-size: 16px;
        }
        .nav-btn:hover {
            background: rgba(255,255,255,0.25);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- SIDEBAR NAV --------------------
st.sidebar.title("TruthLensAI")
page = st.sidebar.radio("Navigation", ["Home", "Fake News Detector"])


# =====================================================
# ======================= HOME PAGE ===================
# =====================================================
if page == "Home":
    st.title("✨ TruthLensAI")
    st.subheader("Your companion for spotting misinformation 🔍")

    # Top button to go to second screen
    st.markdown(
        """
        <a class="nav-btn" href="?page=Fake+News+Detector">Go to Detector</a>
        """,
        unsafe_allow_html=True
    )

    # Rotating tips text
    tips = [
        "🧠 Fun fact: Your brain loves shortcuts — that’s why fake news spreads faster than truth.",
        "🔍 Critical thinking is literally a superpower.",
        "📱 People share headlines they *feel*, not headlines they *check*.",
        "🤳 70% of users don’t read full articles before sharing. Oops.",
        "🎯 Misinformation targets emotions, not logic."
    ]

    tip_index = int(time.time()) % len(tips)
    st.write(f"**💡 Tip:** {tips[tip_index]}")

    # ----------------- HOW TO USE (TRANSLUCENT BOX) -----------------
    st.markdown('<div class="translucent-box">', unsafe_allow_html=True)

    st.markdown(
        """
        ### 🛠️ How to Use  
        1️⃣ Go to the **Fake News Detector** screen using the menu on the left.  
        2️⃣ Enter the headline you want to verify.  
        3️⃣ Select **gender** and **platform**.  
        4️⃣ Hit **Analyze News** — instant insights appear magically ✨  
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)



# =====================================================
# ================== SECOND SCREEN ====================
# ========= (UNCHANGED EXACTLY AS YOU SAID) ===========
# =====================================================
elif page == "Fake News Detector":
    st.title("📰 Fake News Detector")

    # Input headline
    headline = st.text_input("Enter the news headline:")

    # Gender selection (WHITE TEXT)
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])

    # Platform selection
    platform = st.selectbox("Select the platform where the news was found:",
                            ["Instagram", "YouTube", "Facebook", "X / Twitter", "WhatsApp"])

    # Analyze button
    if st.button("Analyze News"):
        if headline.strip() == "":
            st.error("Please enter a headline before analyzing!")
        else:
            st.success("Processing your headline... 🔍")
            time.sleep(1.5)
            st.info(f"Gender: **{gender}** | Platform: **{platform}**")
            st.success("Fake/Real analysis coming soon…")


