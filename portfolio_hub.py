import streamlit as st

# --- LIVE URLs for Deployed Applications ---
# These are the final, confirmed live links for your public portfolio.
APP_LINKS = {
    "1. Structured AI Meal Planner (JSON)": {
        "url": "https://lisa-silva-structured-ai-meal-planner.streamlit.app/",
        "description": "Uses a precise **JSON Schema** to enforce structured output, ensuring the Gemini API returns machine-readable data for database entry or immediate use."
    },
    "2. The Political Fact Checker": {
        "url": "https://lisa-silva-the-political-fact-checker-appr-app.streamlit.app/",
        "description": "Uses **Google Search Grounding** to verify user claims against real-time web results. Demonstrates reliable, grounded AI responses."
    },
    "3. CSV Data Analyzer": {
        "url": "https://lisa-silva-csv-data-analyzer.streamlit.app/",
        "description": "Allows users to upload a CSV file, utilizing the LLM to analyze the data's structure and generate **summaries and insights**."
    },
    "4. Dark Triad Detector Quiz": {
        "url": "https://polisheddarktriadquiz-tmmxtafdgumdetmgboo8bz.streamlit.app/",
        "description": "An interactive, multi-question quiz demonstrating **complex internal logic** and session state management for tracking progress and calculating assessment results."
    }
}

st.set_page_config(layout="wide", page_title="Lisa Silva - AI Portfolio Hub", icon="🚀")

st.markdown("""
    <style>
    .big-font {
        font-size:42px !important;
        font-weight: 800;
        color: #FF4B4B; /* Streamlit Primary Red */
        margin-bottom: -10px;
    }
    .subheader-desc {
        font-size: 20px;
        color: #555;
        font-style: italic;
    }
    .app-card {
        padding: 25px;
        border-radius: 12px;
        background-color: #f9f9f9;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        border-left: 6px solid #FF4B4B;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .app-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    .launch-button {
        background-color: #FF4B4B;
        color: white !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-align: center;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        transition: background-color 0.2s;
    }
    .launch-button:hover {
        background-color: #e64242;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="big-font">Lisa Silva | Applied AI Portfolio Hub</p>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="subheader-desc">
    Expert in Prompt Engineering, Structured Output, and deploying modern, high-accuracy AI applications powered by Gemini.
    </p>
    """, unsafe_allow_html=True
)
st.write("---")

st.subheader("Four Key Projects: Demonstrating Full-Stack AI Capabilities")

# --- App Cards ---
for title, data in APP_LINKS.items():
    with st.container():
        st.markdown(f'<div class="app-card">', unsafe_allow_html=True)
        
        # Use two columns for the title/description and the launch button
        col1, col2 = st.columns([5, 1])
        
        with col1:
            st.markdown(f"### {title}")
            st.markdown(data['description'])
            
        with col2:
            st.markdown("<br>", unsafe_allow_html=True) # Add some vertical space
            # Use the custom CSS class for the link
            st.markdown(f'<a href="{data["url"]}" target="_blank" class="launch-button">Launch App &rarr;</a>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

st.info(
    "These projects collectively showcase skills in real-time web grounding, structured data enforcement (JSON), data handling, and complex application logic."
)
st.markdown(
    "Connect with me on [GitHub](https://github.com/lisa-silva) or [LinkedIn](your-linkedin-profile-here)!"
)
