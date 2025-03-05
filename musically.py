import streamlit as st
import os
import pydub
from pydub import AudioSegment

# Streamlit App Title
st.title("🎵musically")
st.write("Upload and play your favorite songs!")

# File Uploader
uploaded_file = st.file_uploader("Upload a song (MP3, WAV, etc.)", type=["mp3", "wav"])

if uploaded_file is not None:
    # Save uploaded file to a temp location
    file_path = os.path.join("temp_audio." + uploaded_file.name.split(".")[-1])
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the file name
    st.success(f"Uploaded: {uploaded_file.name}")

    # Convert audio file to playable format (if needed)
    audio = AudioSegment.from_file(file_path)
    audio.export("temp_audio.wav", format="wav")

    # Display audio player
    st.audio("temp_audio.wav", format="audio/wav")

    # Remove temporary files
    os.remove(file_path)
