# LED_TO_ASCII

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

This script dynamically updates an image by overlaying ASCII art on it based on a configuration file. The user can specify how frequently the script should check the configuration file for updates and apply changes. This script is useful for real-time monitoring or visualization applications where the image needs to be updated at regular intervals based on configuration changes.

### Project Purpose

The main goal of this project is to:

- Continuously sync and update an image based on real-time configuration changes.
- Display ASCII art overlays on an image in a visually structured manner.
- Provide examples and exercises that users can follow to build their own projects.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.x -  Ensure you have Python 3.x installed on your system. You can download it from python.org.
- Pillow (PIL Fork) - Python Imaging Library
- `json` - JSON library for Python (typically included in the standard library)

**Prepare Configuration and Resources:**

• Ensure you have a JSON configuration file (`config.json`).
      
• Prepare a background image file (`background.png`).	
      
• Optionally, have a TrueType font file (`neon.ttf`) if custom fonts are desired.
      
## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course.git
2. Navigate to the cloned repository:

	```
	cd LED_TO_ASCII
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```
4. Prepare Configuration and Resources.

## Configuration

The script uses a JSON configuration file to store LED settings. Ensure that this file is correctly referenced and formatted.

 **Key Fields in the Configuration File**
 
• `solid_color.led_bits` : The LED bit value used to determine the position of the overlay.

• `solid_color.color` : The color code for the text in hexadecimal format.


## Usage
1. **Execute the script**:
You can run the script from the command line:
```
python led_to_ascii.py
```
2. **Set Sync Interval**:
  When prompted, enter the desired interval for syncing with the configuration file in milliseconds (e.g., 1000 for 1 second).
3. **Image Update Process**:

	•  The script reads the configuration file and extracts the led_bits value to determine where to place the ASCII art on the image.
		              
	• It converts the hexadecimal color code to an RGB tuple for the text color.
		              
	• Based on the `led_bits` value, it positions the text on the image according to predefined coordinates.
		              
	• The image is saved and displayed with the updated overlay at the specified intervals.

	
## Tasks


### Task 1: Modify the Script to Ignore LED Color Settings

• **Objective:** Adjust the LED_TO_ASCII script so that the ASCII symbol's color remains constant, regardless of the LED color settings in the configuration file.

• **Instructions:**

1. Locate the Section for LED Color Adjustment:

    • Open the led_to_ascii.py script in your preferred text editor.
  
    • Find the part of the script where it reads the color value from the config.json file and uses it to set the text color.
  		Typically, this could look something like:
  			```
  			text_color = config["solid_color"]["color"]  # Gets color from config.json
  			```
  
2. Set a Constant Color for the ASCII Symbol:   

    • Instead of using the color from the configuration, modify the script to use a fixed color for the ASCII symbol.
  
    • For example, you can set the text color to always be white. Modify the relevant line to:
  			```
  			text_color = (0, 0, 0)  # Fixed color: black
  			```

3. Save and Test the Script:

    • Save your changes to the script.
  
    • Run the script using the command line
  			```
  			python led_to_ascii.py
  			```
    • Observe the generated image to ensure that the ASCII symbol's color remains constant (white in this case) regardless of any color changes in the config.json file.

4. Validate the Modification:

    • To confirm your changes, modify the color value in config.json to different colors and re-run the script. The ASCII symbol should not change color and should always appear in the fixed color (black).
  			```
  			{
  "solid_color": {
    "led_bits": 2,
    "color": "#FF0000"  # This change should not affect the ASCII symbol color
  }
}
			```