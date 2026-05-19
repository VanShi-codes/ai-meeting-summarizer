import streamlit as st
from utils.summarizer import summarize_meeting

st.set_page_config(
    page_title="AI Meeting Summarizer",
    layout="wide"
)

st.title("AI Meeting Notes Summarizer")

uploaded_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

if uploaded_file:

    transcript = uploaded_file.read().decode("utf-8")

    st.subheader("Transcript Preview")

    st.text_area(
        "Transcript",
        transcript,
        height=250
    )

    if st.button("Generate Summary"):

        with st.spinner("Generating AI Summary..."):

            summary = summarize_meeting(transcript)

            st.subheader("Generated Meeting Notes")

            st.write(summary)

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="meeting_summary.txt"
            )