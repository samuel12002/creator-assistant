import streamlit as st
from ai_helper import generate_creator_content

# إعداد الصفحة
st.set_page_config(page_title="SAMUEL - Creator Assistant", page_icon="🚀")

st.title("SAMUEL's Creator Assistant 🚀")
st.markdown("Your ultimate open-source AI assistant to generate titles, descriptions, scripts, and social media copy.")
st.divider()

# خيارات الواجهة
platform = st.selectbox(
    "Choose your target platform:",
    ["YouTube", "Instagram Carousel", "General Social Post"]
)

topic = st.text_area("What is the main topic or idea?", placeholder="e.g., How to optimize AI prompts for better results...")

if st.button("Generate Content ✨"):
    if topic:
        with st.spinner("Crafting your content..."):
            result = generate_creator_content(platform, topic)
            st.success("Done!")
            st.markdown("### Generated Output:")
            st.write(result)
    else:
        st.warning("Please enter a topic first.")
      
