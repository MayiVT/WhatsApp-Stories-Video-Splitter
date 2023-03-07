from moviepy.video.io.VideoFileClip import VideoFileClip
import math
import os

# Set the input and output folder paths
root_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = "input"
output_folder = "output"

input_folder_path = os.path.join(root_dir, input_folder)
output_folder_path = os.path.join(root_dir, output_folder)

# Set the clip duration (in seconds)
clip_duration = 30

# Get a list of all the video files in the input folder
video_files = [os.path.join(input_folder_path, f) for f in os.listdir(input_folder_path) if f.endswith(".mp4")]

# Loop through each video file and generate clips
for video_file_path in video_files:
    # Open the input video file
    video = VideoFileClip(video_file_path)

    # Get the total duration of the video (in seconds)
    total_duration = video.duration

    # Calculate the number of clips to generate
    num_clips = math.ceil(total_duration / clip_duration)

    # Get the video name (without extension) for use in the output folder path
    video_name = os.path.splitext(os.path.basename(video_file_path))[0]

    # Create the output folder for the video
    video_output_folder_path = os.path.join(output_folder_path, video_name)
    os.makedirs(video_output_folder_path, exist_ok=True)

    # Loop through the number of clips and generate each clip
    for i in range(num_clips):
        # Calculate the start and end times of the clip
        start_time = i * clip_duration
        end_time = min(start_time + clip_duration, total_duration)

        # Extract the clip from the input video
        clip = video.subclip(start_time, end_time)

        # Set the output file path for the clip
        output_file_path = os.path.join(video_output_folder_path, f"clip_{i}.mp4")

        # Write the clip to the output file
        clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

    # Close the input video file
    video.close()