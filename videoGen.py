# from moviepy.editor import VideoFileClip
# import pysrt
# from moviepy.video.VideoClip import TextClip
# from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
# from moviepy.video.tools.subtitles import SubtitlesClip
#
#
# def generate_srt(script_text: str, video_path, output_srt_path):
#     # get video duration for mathing stufdf
#     asd = VideoFileClip(video_path)
#     total_duration = video.duration  # in seconds
#
#     # split into lines
#     lines = script_text.split('.')
#     lines = [line.strip() + '.' for line in lines if line.strip()]  # Cleaning up
#
#     # Estimate duration for each line
#     total_characters = sum(len(line) for line in lines)
#     durations = [(len(line) / total_characters) * total_duration for line in lines]
#
#     subs = pysrt.SubRipFile()
#
#     start_time = 0
#     for idx, (line, duration) in enumerate(zip(lines, durations)):
#         end_time = start_time + duration
#
#         # Create SRT timestamp (hours, minutes, seconds, milliseconds)
#         start_timestamp = pysrt.SubRipTime(seconds=start_time)
#         end_timestamp = pysrt.SubRipTime(seconds=end_time)
#
#         # Create subtitle object
#         sub = pysrt.SubRipItem(index=idx + 1, start=start_timestamp, end=end_timestamp, text=line)
#         subs.append(sub)
#
#         # Update start_time for the next line
#         start_time = end_time
#
#     # Write to SRT file
#     subs.save(output_srt_path, encoding='utf-8')
#
# def generate_video(srt_path, video_path, output_path):
#     generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
#     subs = SubtitlesClip(srt_path, generator)
#     subtitles = SubtitlesClip(subs, generator)
#
#     video = VideoFileClip(video_path)
#
#     # Overlay subtitles on video
#     result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])
#
#     # Write to file
#     result.write_videofile(output_path, codec='libx264', audio_codec='aac')