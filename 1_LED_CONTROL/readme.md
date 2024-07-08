# LED_CONTROL

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Tasks](#tasks)

## Introduction

This script is designed to simplify the process of updating LED configurations by allowing users to select an LED through a user-friendly interface. By interacting with a JSON configuration file, it ensures that the chosen LED's bit value is saved and can be used for further processing or system updates.

### Project Purpose

The main goal of this project is to:

- Provide a clear and interactive way for users to select and modify LED settings.
- Automate the process of saving and confirming changes to configuration files.
- Facilitate the updating of LED bit values in a configuration file.
- Provide examples and exercises that users can follow to build their own projects.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.x
- Pillow (PIL Fork) - Python Imaging Library
- `json` - JSON library for Python (typically included in the standard library)

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/busy-tag/Learning-Course.git
2. Navigate to the cloned repository:

	```
	cd LED_CONTROL
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install pillow
	```

## Configuration

The script uses a JSON configuration file to store LED settings. Ensure that this file is correctly referenced and formatted.

 **Key Fields in the Configuration File**
 
• `solid_color.led_bits` : This field stores the selected LED's bit value. The script updates this value based on user input.


## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python led_control.py
```
2. **Select an LED:**
   The script will display a visual layout of LED positions and their bit values. Follow the prompts to enter the desired LED's bit value.

3. **Confirm the update:**
	The chosen LED's bit value will be written to the configuration file. The script will read back the file to confirm the update and display the current configuration.
	
4. **Choose to continue or exit:**
	After selecting the LED, you can choose to select another LED or exit the script.
	
## Tasks

Task 1: Selecting Different LEDs

• **Objective:** Understand how to select and update different LEDs in the configuration file.

• **Instructions:** 

1. Run the `led_control` script.
2. When prompted, select different LEDs one after another.
3. Check the output to see how the script updates the configuration file with each selected LED.
4. Verify that the chosen LED's bit value is correctly reflected in the configuration file.