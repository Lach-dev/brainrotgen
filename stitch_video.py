from moviepy.editor import VideoFileClip, AudioFileClip, clips_array
from moviepy.video.fx.resize import resize
import random

# Load the audio file
def generate_base_videos(audio_path: str) -> str:
    audio = AudioFileClip("audio/audio_test_a.mp3").subclip(0, 10)  # Trim the audio to 2 seconds

    # Load and trim eight arbitrary videos to the same length as the audio
    start_times = [random.randint(0, 10 * 60) for _ in range(8)]
    clips = [VideoFileClip("base_videos/minecraft_parkour_a.mp4").subclip(start_time, start_time + audio.duration) for start_time in start_times]

    # Resize each video to fit into a 1080x1920 (9:16) frame with 4 rows and 2 columns.
    # Each video should take up half the width (540px) and a quarter of the height (480px).
    resized_clips = [resize(clip, width=540, height=480) for clip in clips]

    # Arrange the videos into a 4x2 grid
    final_video = clips_array([[resized_clips[0], resized_clips[1]],
                               [resized_clips[2], resized_clips[3]],
                               [resized_clips[4], resized_clips[5]],
                               [resized_clips[6], resized_clips[7]]])

    # Ensure the final video fits exactly the 9:16 aspect ratio (1080x1920)
    final_video_resized = final_video.resize((1080, 1920))

    # Set the audio to the final video
    final_video_with_audio = final_video_resized.set_audio(audio)

    # Save the output video with audio
    final_video_with_audio.write_videofile("stitched_videos/stitched_video_with_audio.mp4", fps=24,
                                           codec='libx264',
                                           audio_codec='aac',
                                           temp_audiofile='temp-audio.m4a',
                                           remove_temp=True
                                           )
