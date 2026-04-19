import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np

# Page config (modern UI setup)
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="🧠",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 AI Background Remover")
st.write("Upload an image and remove its background instantly.")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open image
    input_image = Image.open(uploaded_file)

    st.subheader("📸 Original Image")
    st.image(input_image, use_column_width=True)

    # Convert to bytes
    img_bytes = io.BytesIO()
    input_image.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # Process button
    if st.button("✨ Remove Background"):
        with st.spinner("Processing with AI..."):
            output_bytes = remove(img_bytes)

            # Convert output to image
            output_image = Image.open(io.BytesIO(output_bytes))

        st.subheader("🪄 Result (Background Removed)")
        st.image(output_image, use_column_width=True)

        # Download button
        buf = io.BytesIO()
        output_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Download Image",
            data=byte_im,
            file_name="removed_background.png",
            mime="image/png"
        )

# Footer
st.markdown("---")
st.caption("Built with Streamlit + AI (rembg)")