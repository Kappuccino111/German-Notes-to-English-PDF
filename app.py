import streamlit as st
import os
from pathlib import Path
from utils.convert import convert_pdf_to_images
from utils.ai import process_images
from utils.markdown_corrector import final_corrector
from utils.combine import combine_md_files

def process_pdf(api_key, pdf_path):
    st.write("Converting PDF to images...")
    convert_pdf_to_images(pdf_path)
    st.success("PDF converted to images!")

    st.write("Processing images with AI...")
    process_images(api_key)
    st.success("Images processed and Markdown files created!")

    st.write("Correcting Markdown files...")
    final_corrector()
    st.success("Markdown files corrected!")

    st.write("Combining Markdown files...")
    combine_md_files()
    st.success("Markdown files combined!")

    st.write("Generating PDF...")
    os.system("pandoc combined_Electrodynamics_final.md -o output.pdf --pdf-engine=xelatex")
    st.success("PDF generated successfully!")

# Initialize session state for tracking processing status and stored PDF filename.
if "processed" not in st.session_state:
    st.session_state.processed = False
if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

st.title("PDF Translator App")
api_key = st.text_input("Enter your OpenAI API Key:", type="password")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None and api_key:
    # Save the uploaded file only if it's new or hasn't been processed yet.
    if uploaded_file.name != st.session_state.pdf_name:
        st.session_state.pdf_name = uploaded_file.name
        st.session_state.processed = False

    pdf_path = os.path.join("temp", uploaded_file.name)
    Path("temp").mkdir(exist_ok=True)

    # Save file to temp directory if it hasn't been saved yet
    if not os.path.exists(pdf_path):
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("PDF uploaded successfully!")

    # Process PDF only if not already processed
    if not st.session_state.processed:
        process_pdf(api_key, pdf_path)
        st.session_state.processed = True
    else:
        st.info("PDF already processed. To process a new file, please upload a different PDF.")

    # Provide download link
    if os.path.exists("output.pdf"):
        with open("output.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="output.pdf")
