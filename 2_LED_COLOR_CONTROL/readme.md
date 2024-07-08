# LED_COLOR_CONTROL
## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

The LED_COLOR_CONTROL is a Python script designed to dynamically update the color configuration of a Busy Tag device. It reads RGB values from each pixel across a specified image and updates the device's configuration file to reflect these colors. Created using the Python Imaging Library (PIL) and standard JSON handling, this script allows for real-time, image-driven color changes, making it ideal for devices that display visual data or need to adapt their appearance based on image input.

### Project Purpose

The main goal of this project is to:

- Offer an educational resource for learning how to interact with hardware devices through Python.
- Demonstrate how to read and manipulate JSON configuration files.
- Showcase the extraction of RGB values from image pixels using the PIL library.
- Provide hands-on experience through interactive examples and tutorials.
- Supply examples and exercises that users can follow to build their own projects.

## Prerequisites

Before running this script, ensure that you have the following requirements installed:

- Python 3.x 
- Pillow (PIL Fork) - Python Imaging Library

## Installation
 
 To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course.git
2. Navigate to the cloned repository:

	```
	cd LED_COLOR_CONTROL
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```
4. Edit the script:
	Customize the `config_file` and `image_file` paths in the script to match your local file paths or use the provided default values.

## Usage
1. Execute the script:
You can run the script from the command line:
```
python led_color_control.py
```
2. Set the delay:
   The script will prompt you to enter the delay time between updates in milliseconds. This determines how frequently the script updates the device's color based on the image.
3. View the updates:
	The script will read the image, extract the RGB values from each pixel across the width of the image, and update the solid_color field in the device's configuration file with the new color. The process repeats with the specified delay between each update.

## Configuration
**Image File**:
The script uses a specified image file (`custom.png`) from which it extracts the RGB values. Ensure this image file is accessible and correctly specified in the script.

**Configuration File**:
The configuration file (`config.json`) contains the settings for the hardware device. The script reads this file, updates the `solid_color` field with new RGB values, and writes the updated configuration back to the file.

**Key Configuration Field**:
**solid_color.color**: This field is dynamically updated by the script to reflect the RGB color extracted from the image. The color is represented as a hexadecimal string (e.g., `"FF0000"` for red).

## Tasks

### Task 1: Selecting and Testing Different Images

• **Objective:** Learn how the script reads and applies colors from different image files.

• **Instructions:**

1. Prepare a few small images (280x240 pixels) with distinct colors and save them in the same directory as the script. You can use any image format supported by PIL, such as PNG or JPEG.
2. Run the `led_color_control` script.
3. When prompted to specify the image file, enter the name of one of your prepared images (e.g., `red.png`).
4. Observe how the RGB values are extracted from the image and applied to the `solid_color` field in the configuration file.
5. Repeat the process with different images and compare how the color updates differ based on the image content.

### Task 2: Changing the Delay Between Updates

• **Objective:** Explore how to control the update frequency by adjusting the delay time between updates.

• **Instructions:**

1. Run the `led_color_control` script.
2. When prompted to enter the delay time between updates, try different values such as 500, 1000, and 2000 milliseconds (0.5 seconds, 1 second, and 2 seconds, respectively).
3. Observe how changing the delay affects how quickly the colors are updated in the configuration file.
4. Note the differences and decide on the optimal delay time for your needs.