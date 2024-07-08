import json
import random  
from PIL import Image
import time

def read_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_config(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

def get_rgb_from_pixel(img, x, y):
    # Ensure the image is in RGB mode
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Get the RGB value from the pixel at (x, y)
    pixel = img.getpixel((x, y))
    # Print the RGB values for debugging
    print(f"Pixel RGB: {pixel}")
    
    # Convert RGB values to hexadecimal color code
    rgb_code = '%02x%02x%02x' % (pixel[0], pixel[1], pixel[2])
    return rgb_code
    
def get_delay_from_user():
    while True:
        try:
            delay_ms = int(input("Enter the delay time between updates (in milliseconds, 1000 milliseconds = 1 second): "))
            if delay_ms > 0:
                return delay_ms / 1000  # Convert milliseconds to seconds
            else:
                print("Please enter a positive delay value.")
        except ValueError:
            print("Please enter a valid number for the delay.")
            
def main(delay):
    config_file = r'D:\config.json'
    image_file = r'D:\custom.png'

    with Image.open(image_file) as img:
        img = img.convert('RGB')
        width, height = img.size  # Get both width and height of the image
        
        for _ in range(width):  # We can iterate the same number of times as the image width or choose a different number of iterations
            # Read the current configuration before updating
            config = read_config(config_file)
            
            # Print the current color before updating
            current_color = config['solid_color']['color']
            print(f"Current RGB code: {current_color}")
            
            # Choose random x and y coordinates
            random_x = random.randint(0, width - 1)
            random_y = random.randint(0, height - 1)
            
            # Get the RGB code from the randomly chosen pixel
            rgb_code = get_rgb_from_pixel(img, random_x, random_y)
            
            # Update the config with the new RGB code
            config['solid_color']['color'] = rgb_code
            write_config(config_file, config)
            print(f"RGB code updated to: {rgb_code}")
            time.sleep(delay)

if __name__ == "__main__":
    delay = get_delay_from_user()
    main(delay)