# DurationSense-NG

Unlock the power of video insights with DurationSense - your ultimate tool for analyzing and understanding video durations effortlessly. Whether you're managing a collection of videos or need precise duration data for your projects, DurationSense-NG empowers you with powerful insights to make informed decisions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributions](#contributions)
- [Credits](#credits)
- [License](#license)

## Features

- **Efficient Video Analysis:** Utilizes MoviePy library for fast and reliable video duration calculation.
- **Multi-format Support:** Works seamlessly with popular video formats including MP4, AVI, MKV, MOV, WMV, FLV, and more.
- **Recursive Scanning**: Option to scan subdirectories recursively for comprehensive video duration analysis.
- **Multiprocessing:** Harnesses the power of multiprocessing to process multiple videos simultaneously, optimizing performance.

## Installation

### PyPl

I have recently made a PyPl account to make you life easier!

```bash
pip install durationsense
```

### Clone

1 - Clone this repository to your local machine.

```bash
git clone https://github.com/hack505/DurationSense-NG.git

```

2 - Navigate to the project directory.

```bash
cd DurationSense-NG
```

3 - Install the required dependencies.

```bash
pip install -r requirements.txt

```

## Usage

DurationSense-NG offers flexible options through command-line arguments for customizing your video duration analysis:

**-d, --directory:** Specify the directory containing video files. Default is the current working directory.

```bash
python duration_sense_ng.py -d /path/to/videos/directory
```

**-f, --formats:** Define the video formats/extensions to consider during duration calculation. Default includes common formats like MP4, AVI, MKV, MOV, WMV, FLV, and more.

```bash
python duration_sense_ng.py -f .mp4 .avi .mkv -d /path/to/videos/directory
```

**-e, --exclude:** Exclude specific file extensions from duration calculation. Useful for skipping irrelevant files.

```bash
python duration_sense_ng.py -e .wmv .flv -d /path/to/videos/directory
```

**-l, --log-level:** Set the logging level for detailed output. Options include DEBUG, INFO, WARNING, ERROR, CRITICAL. Default is INFO.

```bash
python duration_sense_ng.py -l DEBUG -d /path/to/videos/directory
```

Customize these arguments based on your specific requirements to get precise video duration information and detailed logs.

## Contributions

Contributions to DurationSense-NG are welcome! Feel free to fork the repository, make improvements, and submit pull requests to enhance its functionality.

## Credits

- **MoviePy:** Used for video duration calculation and processing.
- **tqdm:** Provides a progress bar for visual feedback during video processing.
- **multiprocessing**: Utilized for parallel processing of video files, improving performance.

## License

This project is licensed under the [MIT](https://github.com/hack505/Python-Video-Duration-Analyzer-Multi-threaded/blob/main/LICENSE) License - see the LICENSE file for details.
