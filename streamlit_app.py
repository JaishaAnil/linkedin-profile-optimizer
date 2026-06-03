from about_generator import generate_about
from headline_generator import generate_headline
import streamlit as st
from analyzer import analyze_profile

st.title("🔍 LinkedIn Profile Optimizer")

st.write("Analyze your LinkedIn profile and discover missing keywords.")

headline = st.text_input("Enter your Headline")

about = st.text_area("Enter your About Section")

skills = st.text_area("Enter your Skills")

if st.button("Analyze Profile"):

    profile_text = headline + " " + about + " " + skills

    score, missing = analyze_profile(profile_text)

    st.subheader("Profile Score")
    st.success(f"{score}/100")

    st.subheader("Missing Keywords")

    if missing:
        for keyword in missing:
            st.write("❌", keyword)
    else:
        st.write("✅ No missing keywords")

    st.subheader("Suggestions")

    if score < 40:
        st.warning("Add more technical skills and projects.")

    elif score < 70:
        st.info("Add internships and certifications.")

    else:
        st.success("Excellent LinkedIn Profile!")
st.subheader("AI Headline Generator")

headline_skills = st.text_input(
    "Enter skills (comma separated)"
)

if st.button("Generate Headline"):
    headline = generate_headline(
        headline_skills
    )

    st.success(headline)
st.subheader("About Section Generator")

about_skills = st.text_input(
    "Enter skills for About Section"
)

if st.button("Generate About Section"):

    about_text = generate_about(
        about_skills
    )

    st.text_area(
        "Generated About Section",
        value=about_text,
        height=200
    )