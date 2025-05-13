
import os
import streamlit as st

def rename_files(path):
    if not os.path.exists(path):
        return "❌ Path does not exist."

    files = os.listdir(path)
    if not files:
        return "⚠️ No files found in the directory."

    for i, filename in enumerate(files):
        old_path = os.path.join(path, filename)
        new_filename = f"img{i}.jpg"
        new_path = os.path.join(path, new_filename)

        # Rename the file
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            return f"❌ Error renaming {filename}: {e}"

    return f"✅ Renamed {len(files)} files in '{path}'"

# Streamlit UI
st.title("📝 Batch Image Renamer")
st.write("Rename all files in a folder to the format `img0.jpg`, `img1.jpg`, etc.")

folder_path = st.text_input("Enter the folder path:", value="/Users/maeydahmasroor/Desktop/04_assignment/test/")

if st.button("Rename Files"):
    result = rename_files(folder_path)
    st.write(result)