import os
import streamlit as st
from extract_audio import extract_audio_from_video
from generate_srt import generate_srt, transcribe_audio
from burn_subtitles import burn_subtitles_into_video


def main():
    st.title("Subtle - Video Subtitle Generator")
    os.makedirs("videos", exist_ok=True)
    os.makedirs("audio", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("subtitle", exist_ok=True)

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
    if uploaded_file is not None:
        st.video(uploaded_file)
        video_path = "videos/" + uploaded_file.name
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        audio_path = "audio/" + os.path.splitext(uploaded_file.name)[0] + ".wav"
        output_video_path = "output/subtitled_" + uploaded_file.name
        srt_path = "subtitle/" + os.path.splitext(uploaded_file.name)[0] + ".srt"

        if st.button("Process Video"):
            with st.spinner("Extracting audio..."):
                extract_audio_from_video(video_path, audio_path)
                st.success("Audio extracted successfully!")
            with st.spinner("Transcribing audio..."):
                transcription = transcribe_audio(audio_path)
                generate_srt(transcription, srt_path)
                st.success("Transcription completed!")
            with st.spinner("Burning subtitles into video..."):
                output_video_path = burn_subtitles_into_video(
                    video_path, srt_path, output_video_path
                )
                st.success("Subtitles burned into video successfully!")
            st.video(output_video_path)


if __name__ == "__main__":
    main()
