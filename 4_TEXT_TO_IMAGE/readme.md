# TEXT_TO_IMAGE

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

The TEXT_TO_IMAGE script allows you to create an image with custom text. You can specify the background color, text color, and font size interactively through prompts. This tool is useful for generating images for banners or any graphical text display purposes. The script uses Python's PIL (Pillow) library for image creation and manipulation.

### Project Purpose

The main goal of this project is to:

- Provide a simple tool to create images with custom text.
- Demonstrate the combination of Python’s image processing capabilities with text rendering.
- Show how to center text on an image and save the output.
- Offer a starting point for more advanced image manipulation projects in Python.

## Prerequisites

To run this script, ensure you have the following installed:

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
	cd TEXT_TO_IMAGE
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```

## Configuration

The script provides several customizable parameters:
 
• **Text:** You can set any string to be displayed on the image.

• **Background Color:** Input the desired background color in RGB format during the prompt.

• **Text Color:** Input the desired text color in RGB format during the prompt.

• **Font Size:** Specify the font size during the prompt.

• **Font Path:** You can change the `font_path` in the script to use a custom font file.

• **Output File:** The image will be saved as `text_to_image.png`, but you can modify the `output_file` variable in the script to change the file name or path.


## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python text_to_image.py
```
2. **Follow the prompts:**
   
      ▪ **Enter the text to display:** Input the text you want to show on the image. 
      
      ▪ **Enter the background color:** Provide the background color in RGB format (e.g., `255, 255, 255` for white).
      
      ▪ **Enter the text color:** Specify the text color in RGB format (e.g., `0, 0, 0` for black).
      
      ▪ **Enter the font size:** Input the font size (e.g., `40`).
         
3. **Check Output:**
	The generated image will be saved at the specified output_file path. Open the image to verify the text is centered and rendered as expected.
	
## Tasks

### Task 1: Create Your First Text Image

• **Objective:** Learn how to create a simple image with custom text and colors.

• **Instructions:**

1. Run the `text_to_image` script from the command line:

	```
	python text_to_image.py
	```
2. When prompted, enter the text you want to display on the image. For example, type "Hello World".
3. Enter the background color in RGB format. For instance, type `255, 255, 255` for a white background.
4. Enter the text color in RGB format. For instance, type `0, 0, 0` for black text.
5. Specify the font size. For example, type `40`.
6. After the script runs, check the text_to_image.png file created in the script directory. Open this image to see your text centered on a white background.

### Task 2: Experiment with Different Text and Colors

• **Objective:** Try different text messages and color combinations to see how they appear on the generated image.

• **Instructions:**

1. Run the `text_to_image` script from the command line:

	```
	python text_to_image.py
	```

2. Enter a new text message. For example, type "Good Morning".
3. Choose a different background color in RGB format. For example, type `173, 216, 230` for a light blue background.
4. Choose a new text color in RGB format. For example, type `255, 69, 0` for red-orange text.
5. Try a different font size. For instance, type `50`.
6. Check the newly generated `text_to_image.png` file to see how your text and color choices are displayed.

### Task 3: Customize the Font and Output File Name

• **Objective:** Modify the script to use a custom font and change the output file name.

• **Instructions:**

1. Download a TrueType font (.ttf) file that you like and save it to a known location on your computer. You can find free fonts online or use one you already have.
2. Open the `text_to_image.py` script in a text editor.
3. Find the line in the script where the font_path is set. Change this to the path of your downloaded font file. For example:
	
	```
	font_path = r"C:\path\to\your\custom_font.ttf"
	```
4. Also, change the `output_file` variable to save the image with a different name or in a different location. For example:
   
	 ```
	output_file = r"C:\path\to\your\custom_image.png
	```
5. Save the changes to the script and run it again:

	```
	python text_to_image.py
	```

6. Enter your desired text, background color, text color, and font size as prompted.
7. Check the new output file to see the image generated with your custom font and saved under the new file name.