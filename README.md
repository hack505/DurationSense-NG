# Multi-threaded Video Length Calculator

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/github/license/hack505/multi-threaded-video-calculator)

Efficiently calculate the total length of video files in a directory and its subfolders using Python. This multi-threaded script leverages the moviepy library for video analysis, providing faster processing times for collections of video files. Enhance your video management tasks with this utility.

## Table of Contents

- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Script](#running-the-script)
- [Configuration](#configuration)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Usage

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

You'll need to install the `moviepy` library if you haven't already. You can install it using the following command:

```bash
pip install moviepy
  ```


## Running the Script

Clone the project

```bash
  git clone https://github.com/hack505/Python-Video-Duration-Analyzer-Multi-threaded.git
```

Go to the project directory

```bash
  cd Python-Video-Duration-Analyzer-Multi-threaded
```
__*before Running*__

Navigate to the repository's directory.
Replace `"/path/to/your/course/folder"` in the script with the actual path to the folder containing your videos.



Run the code

```bash
  python video_length_calculator.py
```


## Configuration

__Supported video formats (add or remove formats as needed)__

video_formats = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".ogg"]

You can modify the video_formats list in the script to include additional formats if needed.

## Notes

- Multi-threading allows the script to utilize your CPU's cores more efficiently, providing faster processing times for video length calculations.
- Keep in mind that the script's execution time depends on the number and length of video files in the specified folder.
- Make sure not to include sensitive paths or information in your code or repository.




## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to [open an issue](https://github.com/hack505/multi-threaded-video-calculator/issues) or [submit a pull request](https://github.com/hack505/multi-threaded-video-calculator/pulls).





## License

[MIT](https://github.com/hack505/Python-Video-Duration-Analyzer-Multi-threaded/blob/main/LICENSE)

