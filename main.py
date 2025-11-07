import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# ====== CUSTOM STYLING ======
page_bg_img = """
<style>
/* Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&w=1740&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Overlay for readability */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.55);
    z-index: -1;
}

/* Title Styling */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    font-weight: 800 !important;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
}

/* Subheader text */
div[data-testid="stMarkdownContainer"] > p {
    color: #f0f0f0;
    font-size: 1.05rem;
}

/* Dropdown Boxes (Select inputs) */
div[data-baseweb="select"] > div {
    background-color: rgba(0, 0, 0, 0.8) !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 0 10px rgba(255,255,255,0.1);
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

/* Labels above inputs */
label {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* Generate Button */
button[kind="primary"] {
    background: linear-gradient(90deg, #0077b5, #00a0dc);
    color: white;
    border-radius: 12px;
    font-weight: bold;
    border: none;
    box-shadow: 0px 4px 10px rgba(0, 119, 181, 0.4);
    transition: all 0.2s ease-in-out;
}

button[kind="primary"]:hover {
    background: linear-gradient(90deg, #00a0dc, #0077b5);
    transform: scale(1.03);
}

/* Generated Post Box */
div.stMarkdown {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 15px;
    margin-top: 25px;
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 500;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Hide Streamlit default footer/header */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# ====== MAIN APP ======
def main():
    st.markdown("<h1 style='text-align: center;'>🚀 LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Create catchy, professional posts in seconds!</p>", unsafe_allow_html=True)

    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=["Short", "Medium", "Long"])

    with col3:
        selected_language = st.selectbox("Language", options=["English", "Hinglish"])

    # Generate Button
    if st.button("✨ Generate"):
        with st.spinner("Crafting your LinkedIn post... 💡"):
            post = generate_post(selected_length, selected_language, selected_tag)
            st.markdown(f"<div class='stMarkdown'>{post}</div>", unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()

