# SYSTEM_UPTIME

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output](#output)
- [Tasks](#tasks)

## Introduction

The SYSTEM_UPTIME script is a Python tool designed to generate an image displaying the system's uptime in a readable format. By leveraging the Python Imaging Library (Pillow) for image manipulation and psutil to retrieve system uptime information, this script provides a visual representation of how long the system has been running.

### Project Purpose

The main goal of this project is to:

- Demonstrate how to use Python for retrieving and displaying system information.
- Show how to create and customize images using dynamic text overlays.
- Provide a simple, visual way to display system uptime.
- Provide examples and exercises that users can follow to build their own projects.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.x
- Pillow (PIL Fork) - Python Imaging Library
- `psutil` - Python library for system and process utilities
- A TrueType font file for text rendering (e.g., `neon.ttf`)

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course.git
2. Navigate to the cloned repository:

	```
	cd SYSTEM_UPTIME
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```

## Configuration

### Key Fields

1. Specify the path to the TrueType font file used for text rendering. Adjust the font_path in the script to point to your desired font file. Example: `D:\neon.ttf.`
2. Size of the text displaying the uptime information. Example: `35`.
3. RGB values defining the text color. Example: `(0, 0, 0)` for black text.
4. Background Color: RGB values defining the background color of the image. Example: `(255, 255, 255)` for a white background.
5. Output File Path: The path where the generated image will be saved. Example: `D:\uptime_image.png.`



## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python system_uptime.py
```
2. **Script Execution Flow:**

• The script retrieves the system's uptime using `psutil`.

• It formats the uptime into a readable string, breaking it down into days, hours, minutes, and seconds.

• It generates an image with the formatted uptime text centered on a specified background.

3. **Viewing the Output:**

• The generated image (`uptime_image.png`) will be saved in the specified directory on the `D:` drive.

• Open the image to view the system's uptime in a visually pleasing format.

## Output

The script creates a PNG image displaying the system's uptime with the following specifications:

• **Image Dimensions:** 240 pixels wide by 280 pixels high.
   
• **Text:** Displayed in the center of the image with each time unit on a new line.
   
• **Background and Text Color:** Configurable through the script parameters.
	
## Tasks

### Task 1: Retrieve and Display System Uptime

• **Objective:** Learn how to run the script and view the generated image displaying the system's uptime.

• **Instructions:**

1. Ensure you have Python, Pillow, and `psutil` installed on your system:
	
	```
	pip install pillow psutil
	```
2. Clone the repository and navigate to the directory:
	
	```
	git clone https://github.com/busy-tag/Learning-Course.git
	cd SYSTEM_UPTIME
	```
3. Run the script from the command line:

	```
	python system_uptime.py
	```
4. Locate the generated image (`uptime_image.png`) in the specified directory.
5. Open the image to see your system's uptime displayed in a clear, readable format.

### Task 2: Customize Text and Background Colors

• **Objective:** Modify the script to change the text and background colors of the uptime image.

• **Instructions:**

1. Open the `system_uptime.py` script in a text editor.
2. Find the lines where the text color and background color are defined:

	```
	text_color = (0, 0, 0)  # Default black text
	background_color = (255, 255, 255)  # Default white background
	```
3. Change these values to customize the colors. For example, to use blue text on a light grey background, update the values as follows:

	```
	text_color = (0, 0, 255)  # Blue text
	background_color = (200, 200, 200)  # Light grey background
	```
4. Save the changes and re-run the script:
	
	```
	python system_uptime.py
	```
5. Check the new `uptime_image.png` to see the updated colors.

### Task 3: Change the Font and Text Size

• **Objective:** Learn how to use a different font and adjust the text size in the generated image.

• **Instructions:**

1. Download a TrueType font file (`.ttf`) that you want to use and place it in the script directory. Rename it to `custom_font.ttf` or update the path in the script accordingly.
2. Open the `system_uptime.py` script in a text editor.
3. Locate the line where the font path is set and update it to point to your new font file:

	```
	font_path = "custom_font.ttf"  # Path to your custom font
	```
4. Find the line where the font size is defined and change it to a new size (e.g., from 35 to 50):
	
	```
	font_size = 50  # New font size
	```
5. Save the changes and re-run the script:

	```
	python system_uptime.py
	```
6. Open the `uptime_image.png` to see the uptime displayed with your chosen font and size.