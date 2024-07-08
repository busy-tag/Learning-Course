# SYSTEM_USAGE

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

The SYSTEM_USAGE script is a Python tool designed to dynamically overlay real-time system resource usage statistics (CPU, RAM, and GPU) onto a background image. By utilizing the Python Imaging Library (PIL) to render text and the psutil library to retrieve system metrics, this script provides a visual representation of your system’s performance. Ideal for creating a continuous visual monitor, it updates the image at regular intervals to reflect the current system usage.

### Project Purpose

The main goal of this project is to:

- Demonstrate the combination of Python’s image processing capabilities with system performance monitoring.
- Show how to dynamically update images with real-time data.
- Provide an engaging and visual way to monitor system resources.
- Provide examples and exercises that users can follow to build their own projects.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.x
- Pillow (PIL Fork) - Python Imaging Library
- `psutil` - Python library for system and process utilities
- An NVIDIA GPU with nvidia-smi for GPU usage statistics (optional)
- A TrueType font file for text rendering (e.g., neon.ttf)

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course/SYSTEM_USAGE.git
2. Navigate to the cloned repository:

	```
	cd SYSTEM_USAGE
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```

## Configuration

• Background Image: The script uses a background image (background.png) to overlay the system metrics. Ensure this file is available and correctly referenced in the script.

• Font File: The text overlay is drawn using a specified TrueType font (neon.ttf). Adjust the path in the script to point to your preferred font file.

### Key Fields

1. Font Size: Size of the text displaying the metrics.
2. X and Y Coordinates: Starting position of the text on the image.
3. Text Color: RGB values defining the text color.


## Usage
1. **Execute the script**:
You can run the script from the command line:
```
python system_usage.py
```
2. **Configure text parameters**:
   Input the font size, X and Y coordinates for text placement, and the text color in RGB format when prompted. These settings define how and where the usage statistics are displayed on the image.
3. **Monitor updates**:
	The script will create and update an image (current_usage.png) every five seconds with the latest CPU, RAM, and GPU usage data. The text is drawn at the specified position and color.
	
## Tasks

### Task 1: Display System Usage with Default Settings

• **Objective:** Learn how to run the script and view the generated image displaying system resource usage with the default settings.

• **Instructions:**

1. Ensure you have Python, Pillow, and `psutil` installed on your system.

	
	```
	pip install pillow psutil
	```
2. Clone the repository and navigate to the directory:
	
	```
	git clone https://github.com/busy-tag/Learning-Course.git
	cd SYSTEM_USAGE
	```
3. Run the script from the command line

	```
	python system_usage.py
	```
4. Locate the generated image (`current_usage.png`) in the script directory.
5. Open the image to see the real-time system CPU, RAM, and (if available) GPU usage overlaid on the background image.

### Task 2: Customize Text Position and Color

• **Objective:** Change the position and color of the text displaying the system usage statistics.

• **Instructions:**

1. Open the system_usage.py script in a text editor.
2. Find the lines where the text position (X and Y coordinates) and color are defined. These settings might look like this:

	```
	text_x = 50  # X coordinate for text
	text_y = 50  # Y coordinate for text
	text_color = (0, 255, 0)  # Green text
	```
3. Modify these values to change the text position and color. For example, to move the text down and to the right and make it blue, you might change them to:
	
	```
	text_x = 150  # New X coordinate
	text_y = 200  # New Y coordinate
	text_color = (0, 0, 255)  # Blue text
	```
4. Save the changes and re-run the script
	
	```
	python system_usage.py
	```
5. Check the updated `current_usage.png` to see the new text position and color.

### Task 3: Use a Custom Font and Adjust Text Size

• **Objective:** Learn how to use a different font and adjust the size of the text displaying the system usage statistics.

• **Instructions:**

1. Download a TrueType font file (`.ttf`) that you want to use and place it in the script directory. Rename it to `custom_font.ttf` or update the path in the script accordingly.
2. Open the `system_usage.py` script in a text editor.
3. Locate the line where the font path is set and update it to point to your new font file:
	```
	font_path = "custom_font.ttf"  # Path to your custom fon
	```
4. Find the line where the font size is defined and change it to a new size (e.g., from `20` to `40`):
	
	```
	font_size = 40  # New font size
	```

5. Save the changes and re-run the script
	
	```
	python system_usage.py
	```

6. Open the `current_usage.png` to see the system usage statistics displayed with your chosen font and size.