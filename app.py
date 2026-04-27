import streamlit as st
from services.r2_services import upload_to_r2

st.title("LinkedIn Analyzer with R2")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Upload To Cloudflare R2"):

        key = upload_to_r2(uploaded_file)

        st.success(
           f"Uploaded: {key}"
        )