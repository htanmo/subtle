import ffmpeg


def burn_subtitles_into_video(video_path, srt_path, output_path):
    try:
        (
            ffmpeg.input(video_path)
            .output(output_path, vf=f"subtitles={srt_path}")
            .run(overwrite_output=True)
        )
        print(f"Subtitled video saved to {output_path}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
