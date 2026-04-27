import io
import streamlit as st

from services.r2_services import upload_to_r2
from services.pdf_parser import extract_text
from services.llm_service import analyze_profile


st.title("AI LinkedIn Analyzer with Cloudflare R2")

uploaded_file = st.file_uploader(
    "Upload LinkedIn PDF",
    type=["pdf"]
)


if uploaded_file:

    st.success("PDF uploaded successfully")

    if st.button("Analyze Profile"):

        try:
            with st.spinner("Processing..."):

                # Read uploaded file once
                file_bytes = uploaded_file.read()


                # Extract PDF text
                profile_text = extract_text(
                    io.BytesIO(file_bytes)
                )


                # Upload PDF to Cloudflare R2
                object_key = upload_to_r2(
                    io.BytesIO(file_bytes)
                )


                # Run LLM Analysis
                analysis = analyze_profile(
                    profile_text
                )


            st.success(
                f"Stored in R2: {object_key}"
            )

            st.subheader("Profile Analysis")
            st.write(analysis)

        except Exception as e:
            st.error(
                f"Error: {str(e)}"
            )