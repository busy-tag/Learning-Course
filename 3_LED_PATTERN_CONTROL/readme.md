# LED_PATTERN_CONTROL

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

This script allows users to create, modify, and save LED lighting patterns dynamically. By providing an interactive interface for defining pattern units and their attributes, it updates a JSON configuration file with the desired LED settings and repeat patterns.

### Project Purpose

The main goal of this project is to:

- Simplify the process of creating and modifying LED lighting patterns.
- Provide a user-friendly interface for defining and saving pattern attributes.
- Automate the updating and confirmation of pattern configurations in a JSON file.
- Provide examples and exercises that users can follow to build their own projects.

## Prerequisites

To run this script, ensure you have the following requirements installed:

- Python 3.x
- `json` - JSON library for Python (typically included in the standard library)


## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course.git
2. Navigate to the cloned repository:

	```
	cd LED_PATTERN_CONTROL
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```

## Configuration

The script uses a JSON configuration file to store pattern settings. Ensure that this file is correctly referenced and formatted.

### Key Fields

1. `custom_pattern_arr` : An array of pattern units where each unit contains `led_bits`, `color, speed`, and `delay` attributes.
2. `pattern_repeat` : An integer specifying how many times the pattern should repeat.


## Usage
1. **Execute the script**:
You can run the script from the command line:
```
python led_pattern.py
```
2. **Define pattern units**:
      1- LED Bits (integer)
      2- Color (hex code, e.g., "00FF00")
      3- Speed (integer)
      4- Delay (integer in milliseconds)  	
  
3. **Add more pattern units**:
	After defining a pattern unit, you will be asked if you want to add another. You can continue to add as many units as needed.
4. **Specify Repeat Times**
	Specify how many times the defined pattern should repeat.
5. **Save and Confirm**
	The script will save the pattern units and repeat times to the JSON configuration file and read back to confirm the changes.
	
## Tasks

### Task 1: Creating a Simple LED Pattern

• **Objective:** Learn how to create and save a basic LED lighting pattern using the script.

• **Instructions:**

1. Run the `led_pattern_control` script from the command line:
	```
	python led_pattern_control.py
	```
	
2. Follow the prompts to define your first pattern unit:

   • Enter an LED Bits value (e.g., `132`).

   • Specify a color in hexadecimal format (e.g., `00FF00` for green).

   • Set a speed value (e.g., `10`).

   • Set a delay time in milliseconds (e.g., `500`).

3. When asked if you want to add another pattern unit, choose `no` to finish.
4. Specify how many times you want the pattern to repeat (e.g., 5).
5. The script will save the configuration to the JSON file and confirm the update. Check the JSON file to see your new pattern configuration.

### Task 2:  Adding Multiple Pattern Units

• **Objective:** Learn how to create and save a basic LED lighting pattern using the script.

• **Instructions:**

1. Run the `led_pattern_control` script from the command line:
	```
	python led_pattern_control.py
	```
	
2. Define the first pattern unit:

   • Enter an LED Bits value (e.g., `132`).

   • Specify a color in hexadecimal format (e.g., `0000FF` for blue).

   • Set a speed value (e.g., `10`).

   • Set a delay time in milliseconds (e.g., `500`).

3. When asked if you want to add another pattern unit, choose `yes`.
4. Define the next unit with different attributes:

   • Enter an LED Bits value (e.g., `129`).

   • Specify a color in hexadecimal format (e.g., `FF0000` for red).

   • Set a speed value (e.g., `10`).

   • Set a delay time in milliseconds (e.g., `500`).

5. Continue adding more units as desired.
6. Finally, specify how many times you want the entire pattern to repeat (e.g., 3).
7. Check the JSON configuration file to see how the pattern has been updated with multiple units.

### Task 3:  Modifying and Testing Existing Patterns

• **Objective:** Learn how to modify an existing pattern configuration and test the changes.

• **Instructions:**

1. Open the JSON configuration file created by the script in a text editor.
2. Manually change one of the pattern units attributes, such as altering the color from `FF0000` to `FFFF00` (yellow).
3. Save the changes to the JSON file.
4. Run the `led_pattern_control` script from the command line:

	```
	python led_pattern_control.py
	```
5. The script will prompt you to create new patterns or modify existing ones. Follow the instructions to either confirm the changes or make further adjustments.
6. Observe how the modifications are reflected in the LED pattern by checking the configuration file after running the script.