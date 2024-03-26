import os
import argparse
from moviepy.editor import VideoFileClip
import logging
from tqdm import tqdm
import time
from multiprocessing import Pool, cpu_count

logging.basicConfig(level=logging.INFO)


def calculate_video_length(video_path):
    """
    Calculate the length of a video file using MoviePy.

    Args:
    - video_path: Path to the video file.

    Returns:
    - Length of the video in seconds.
    """
    try:
        video_clip = VideoFileClip(video_path)
        length = video_clip.duration
        video_clip.close()
        return length
    except Exception as e:
        logging.error(f"Error processing video {video_path}: {e}")
        return 0


def get_video_paths(folder_path, video_formats, exclude_formats):
    """
    Get a list of video file paths in a folder.

    Args:
    - folder_path: Path to the folder containing video files.
    - video_formats: List of video formats/extensions to consider.
    - exclude_formats: List of file extensions to exclude from length calculation.

    Returns:
    - List of video file paths.
    """
    return [os.path.join(root, file) for root, dirs, files in os.walk(folder_path) for file in files if
            any(file.endswith(format) for format in video_formats) and not any(file.endswith(exclude) for exclude in exclude_formats)]


def get_total_video_length(folder_path, video_formats, exclude_formats, recursive=False, sort_by_length=False):
    """
    Get the total length of all video files in a folder.

    Args:
    - folder_path: Path to the folder containing video files.
    - video_formats: List of video formats/extensions to consider.
    - exclude_formats: List of file extensions to exclude from length calculation.
    - recursive: Enable recursive scanning of subdirectories.
    - sort_by_length: Sort video files based on length.

    Returns:
    - Total length of all video files in seconds.
    """
    try:
        if recursive:
            video_paths = get_video_paths_recursive(
                folder_path, video_formats, exclude_formats)
        else:
            video_paths = get_video_paths(
                folder_path, video_formats, exclude_formats)

        if sort_by_length:
            video_paths.sort(key=lambda path: calculate_video_length(path))

        # Initialize multiprocessing Pool
        num_processes = min(cpu_count(), len(video_paths))
        with Pool(processes=num_processes) as pool:
            lengths = list(tqdm(pool.imap(calculate_video_length, video_paths), total=len(
                video_paths), desc='Processing videos', unit='file'))

        total_length_seconds = sum(lengths)
        return total_length_seconds
    except Exception as e:
        logging.error(f"Error calculating total video length: {e}")
        return 0


def get_video_paths_recursive(folder_path, video_formats, exclude_formats):
    """
    Get a list of video file paths in a folder and its subdirectories recursively.

    Args:
    - folder_path: Path to the folder containing video files.
    - video_formats: List of video formats/extensions to consider.
    - exclude_formats: List of file extensions to exclude from length calculation.

    Returns:
    - List of video file paths.
    """
    video_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(format) for format in video_formats) and not any(file.endswith(exclude) for exclude in exclude_formats):
                video_paths.append(os.path.join(root, file))
    return video_paths


def format_time(seconds):
    """
    Convert seconds to hours and minutes format.

    Args:
    - seconds: Total time in seconds.

    Returns:
    - Formatted string representing hours and minutes.
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} hours and {minutes} minutes"


def main():
    """
    Main function to calculate total video length and display results.
    """
    parser = argparse.ArgumentParser(
        description='Calculate total video length in a directory.')
    parser.add_argument('-d', '--directory', default=os.getcwd(),
                        help='Directory containing video files (default: current directory)')
    parser.add_argument('-f', '--formats', nargs='+', default=['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg',
                        '.3gp', '.ogg'], help='Video formats/extensions to consider (default: .mp4 .avi .mkv .mov .wmv .flv .webm .mpeg .3gp .ogg)')
    parser.add_argument('-e', '--exclude', nargs='+', default=[],
                        help='File extensions to exclude from length calculation')
    parser.add_argument('-l', '--log-level', default='INFO',
                        help='Logging level (default: INFO)')
    parser.add_argument('-t', '--total', action='store_true',
                        help='Calculate and display total length in seconds only (without converting to hours)')
    parser.add_argument('-s', '--seconds', action='store_true',
                        help='Calculate and display total length in seconds only')
    args = parser.parse_args()

    if args.log_level:
        logging.basicConfig(level=args.log_level.upper())

    start_time = time.time()  # Record start time

    total_length_seconds = get_total_video_length(
        args.directory, args.formats, args.exclude)

    end_time = time.time()  # Record end time
    total_time = end_time - start_time  # Calculate total time taken

    if args.seconds:
        total_length_info = f"Total video length: {total_length_seconds} seconds"
        logging.info(total_length_info)
        # print(total_length_info)  # Print total length in seconds only
    else:
        total_length_info = f"Total video length: {format_time(total_length_seconds)}"
        logging.info(total_length_info)
        # Print total length in hours and minutes format
        # print(total_length_info)

    # Print total time taken
    total_time_info = f"Total time taken: {total_time:.2f} seconds"
    logging.info(total_time_info)
    # print(total_time_info)


if __name__ == "__main__":
    main()
