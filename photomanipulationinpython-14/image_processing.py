import streamlit as st
from PIL import Image, ImageFilter, ImageOps

st.set_page_config(page_title="Image Manipulation App", layout="centered")
st.title(" Python Image Manipulation App")
st.write("Upload an image and apply basic transformations.")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    st.sidebar.header("Manipulation Options")

    # Option 1: Convert to grayscale
    if st.sidebar.checkbox("Convert to Grayscale"):
        image = ImageOps.grayscale(image)

    # Option 2: Rotate
    angle = st.sidebar.slider("Rotate", 0, 360, 0, 5)
    if angle:
        image = image.rotate(angle)

    # Option 3: Apply blur
    blur_radius = st.sidebar.slider("Blur Radius", 0.0, 10.0, 0.0, 0.5)
    if blur_radius > 0:
        image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Option 4: Flip image
    if st.sidebar.checkbox("Flip Horizontally"):
        image = ImageOps.mirror(image)

    if st.sidebar.checkbox("Flip Vertically"):
        image = ImageOps.flip(image)

    st.subheader("Modified Image")
    st.image(image, use_column_width=True)

    # Option to download
    st.sidebar.markdown("### Download Image")
    if st.sidebar.button("Generate Download Link"):
        from io import BytesIO
        import base64

        buf = BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        b64 = base64.b64encode(byte_im).decode()
        href = f'<a href="data:file/png;base64,{b64}" download="modified_image.png">Download Image</a>'
        st.markdown(href, unsafe_allow_html=True)
