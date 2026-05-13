# app.py

import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="Document Scanner", layout="centered")

st.title("📄 Document Scanner")
st.write("Upload a document image, convert it to black & white PDF, and download it.")

# Upload image
uploaded_file = st.file_uploader(
    "Upload Document Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Show original image
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    # Convert button
    if st.button("Convert to Black & White PDF"):

        # Convert to grayscale
        gray_image = ImageOps.grayscale(image)

        # Increase contrast for document-like scan effect
        bw_image = gray_image.point(lambda x: 0 if x < 140 else 255, '1')

        # Preview converted image
        st.subheader("Scanned Black & White Preview")
        st.image(bw_image, use_container_width=True)

        # Convert to PDF
        pdf_bytes = io.BytesIO()

        # Convert image mode for PDF saving
        pdf_image = bw_image.convert("RGB")

        pdf_image.save(pdf_bytes, format="PDF")

        pdf_bytes.seek(0)

        # Download button
        st.download_button(
            label="⬇ Download PDF",
            data=pdf_bytes,
            file_name="scanned_document.pdf",
            mime="application/pdf"
        )
