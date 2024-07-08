import json
import time 
from PIL import Image, ImageDraw, ImageFont

def read_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def compare_led_bits(config):
    # Extract solid_color.led_bits value
    led_bits_value = config.get('solid_color', {}).get('led_bits', -1)
    return led_bits_value

def draw_on_image(background_image_path, text, coordinates, text_color=(255, 255, 255), font_path=None, font_size=40, output_file="output_image.png"):
    # Open the background image
    image = Image.open(background_image_path)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Load a font or use the default one
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    # Draw the text on the image at the specified coordinates with the specified color
    draw.text(coordinates, text, font=font, fill=text_color)
    
    # Save the image to the specified file
    image.save(output_file)
    print(f"New image created and saved as {output_file}")

def get_sync_interval_from_user():
    while True:
        try:
            interval_ms = int(input("Enter the sync interval in milliseconds: "))
            if interval_ms <= 0:
                raise ValueError("Interval must be a positive number.")
            return interval_ms
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def main():
    # Define the path to the configuration file and other resources
    config_file = r'D:\config.json'
    background_image_path = r'D:\background.png'  # Path to the background image
    font_path = r'D:\neon.ttf'  # Optional path to font file, can be None
    output_file = r'D:\output_image.png'  # Output file name
    
    # Get the sync interval from the user
    sync_interval_ms = get_sync_interval_from_user()

    # Continuously update the image at the specified interval
    while True:
        # Read the configuration file
        config = read_config(config_file)

        # Get the led_bits and color values from the config
        led_bits_value = compare_led_bits(config)
        font_color = tuple(int(config.get('solid_color', {}).get('color', 'FFFFFF')[i:i+2], 16) for i in (0, 2, 4))  # Convert hex color to RGB tuple

        # Define the conditions and corresponding coordinates for drawing text
        coordinates_mapping = {
            129: (56, 148),
            130: (56, 88),
            132: (56, 27),
            136: (112, 27),
            144: (168, 27),
            160: (168, 88),
            192: (168, 148)  
        }

        # Text to draw on the image
        text = "o"

        # Check the led_bits value and draw the text accordingly
        if led_bits_value in coordinates_mapping:
            coordinates = coordinates_mapping[led_bits_value]
            draw_on_image(background_image_path, text, coordinates, font_color, font_path=font_path, font_size=40, output_file=output_file)
        else:
            print(f"led_bits value {led_bits_value} is not in the predefined list. No drawing performed.")
        
        # Wait for the specified interval before the next iteration
        time.sleep(sync_interval_ms / 1000.0)  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()