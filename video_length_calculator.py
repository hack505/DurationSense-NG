import os
import concurrent.futures
from moviepy.editor import VideoFileClip

# List of video formats
video_formats = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.3gp', '.ogg']

def calculate_video_length(video_path):
    video_clip = VideoFileClip(video_path)
    length = video_clip.duration
    video_clip.close()
    return length

def get_total_video_length(folder_path):
    total_length = 0
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        video_paths = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if any(file.endswith(format) for format in video_formats):
                    video_paths.append(os.path.join(root, file))
        
        # Submit video processing tasks to the thread pool
        results = list(executor.map(calculate_video_length, video_paths))
        
        # Sum up the results to get the total length
        total_length = sum(results)
    
    return total_length

course_folder = "/path/to/your/course/folder"
total_length_seconds = get_total_video_length(course_folder)
total_length_hours = total_length_seconds / 3600
print(f"Total video length: {total_length_hours:.2f} hours")
