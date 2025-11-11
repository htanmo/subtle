import whisper
import srt
from datetime import timedelta


def transcribe_audio(file_path, model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result


def generate_srt(transcription, srt_path):
    segments = transcription["segments"]
    srt_entries = []

    for i, segment in enumerate(segments):
        start = timedelta(seconds=segment["start"])
        end = timedelta(seconds=segment["end"])
        content = segment["text"].strip()

        srt_entry = srt.Subtitle(index=i + 1, start=start, end=end, content=content)
        srt_entries.append(srt_entry)

    srt_content = srt.compose(srt_entries)

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    print(f"SRT file generated at {srt_path}")
