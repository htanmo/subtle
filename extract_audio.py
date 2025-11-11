from moviepy import VideoFileClip


def extract_audio_from_video(video_path, audio_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        if audio_clip is None:
            print("No audio track found in the video.")
            return
        audio_clip.write_audiofile(audio_path)
        audio_clip.close()
        video_clip.close()
        print(f"Audio extracted and saved to {audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
