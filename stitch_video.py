from moviepy.editor import VideoFileClip, AudioFileClip, clips_array
from moviepy.video.fx.resize import resize
import random
import uuid
import pysrt
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def generate_base_video(video_path: str, audio_path: str, script_text: str, audio_trim_length: int = 0) -> str:
    if audio_trim_length == 0:
        audio = AudioFileClip(audio_path)
    elif audio_trim_length > 0:
        audio = AudioFileClip(audio_path).subclip(0, audio_trim_length)
    else:
        raise ValueError("Audio trim length must be a positive integer")

    duration = audio.duration
    # generate srt
    lines = script_text.split('.')
    lines = [line.strip() + '.' for line in lines if line.strip()]  # Cleaning up

    # Estimate duration for each line
    total_characters = sum(len(line) for line in lines)
    durations = [(len(line) / total_characters) * duration for line in lines]

    subs = pysrt.SubRipFile()

    start_time = 0
    for idx, (line, duration) in enumerate(zip(lines, durations)):
        end_time = start_time + duration

        # Create SRT timestamp (hours, minutes, seconds, milliseconds)
        start_timestamp = pysrt.SubRipTime(seconds=start_time)
        end_timestamp = pysrt.SubRipTime(seconds=end_time)

        # Create subtitle object
        sub = pysrt.SubRipItem(index=idx + 1, start=start_timestamp, end=end_timestamp, text=line)
        subs.append(sub)

        # Update start_time for the next line
        start_time = end_time

    # Write to SRT file
    srt_file_path = f"srt/{uuid.uuid4()}.srt"
    subs.save(srt_file_path, encoding='utf-8')

    # Load and trim eight arbitrary videos to the same length as the audio
    start_times = [random.randint(0, 10 * 60) for _ in range(8)]
    clips = [VideoFileClip(video_path).subclip(start_time, start_time + duration) for
             start_time in start_times]

    # Resize each video to fit into a 1080x1920 (9:16) frame with 4 rows and 2 columns.
    # Each video should take up half the width (540px) and a quarter of the height (480px).
    resized_clips = [resize(clip, width=540, height=480) for clip in clips]

    # Arrange the videos into a 4x2 grid
    final_video_array = clips_array([[resized_clips[0], resized_clips[1]],
                                     [resized_clips[2], resized_clips[3]],
                                     [resized_clips[4], resized_clips[5]],
                                     [resized_clips[6], resized_clips[7]]])

    # Ensure the final video fits exactly the 9:16 aspect ratio (1080x1920)
    final_video_resized = final_video_array.resize((1080, 1920))

    # Set the audio to the final video
    video_with_audio = final_video_resized.set_audio(audio)

    generator = lambda txt: TextClip(txt, font="arial", fontsize=50, color="white", method='caption',
                                     size=video_with_audio.size)

    # with open(srt_file_path, "r") as srt_file:
    #     # Read the entire content of the file into a string
    #     subtitles = srt_file.read()

    # Create SubtitlesClip with the correct list format (start time and text only)
    sub_clip = SubtitlesClip(srt_file_path, generator)

    final_video = CompositeVideoClip([video_with_audio, sub_clip], size=video_with_audio.size)

    file_path = f"stitched_videos/{uuid.uuid4()}.mp4"

    # Save the output video with audio
    final_video.write_videofile(file_path, fps=24,
                                codec='libx264',
                                audio_codec='aac',
                                temp_audiofile='temp-audio.m4a',
                                remove_temp=True
                                )

    return file_path
