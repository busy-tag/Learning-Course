import psutil
import subprocess
import re
import time
from PIL import Image, ImageDraw, ImageFont

def get_gpu_usage():
    try:
        result = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader"], encoding='utf-8')
        gpu_usage = re.findall(r'\d+', result)[0] + '%'
    except Exception:
        gpu_usage = "N/A"
    return gpu_usage

def create_usage_image(font_size, x, y, text_color):
    background_path = 'D:\\background.png'
    img = Image.open(background_path)
    draw = ImageDraw.Draw(img)

    # Load the "Neon" font
    font_path = 'D:\\neon.ttf'
    font = ImageFont.truetype(font_path, font_size)

    # Get system data
    cpu = f"CPU: {psutil.cpu_percent()}%"
    ram = f"RAM: {psutil.virtual_memory().percent}%"
    gpu = f"GPU: {get_gpu_usage()}"

    # Prepare text to be drawn
    text = f"{cpu}\n{ram}\n{gpu}"

    # Use the provided X, Y coordinates and text color for text positioning and coloring
    lines = text.split('\n')
    for line in lines:
        draw.text((x, y), line, fill=text_color, font=font)
        y += font_size + 5  # Adjust Y position for the next line, adding a small gap

    # Save the modified image
    img.save('D:\\current_usage.png')

try:
    print("Choose and place your background image in folder.")
    print("Make sure the image dimensions are set to 280x240pixels (Height x Width).")
    font_size = int(input("Enter the font size (40 recomended for BUSY TAG): "))
    x = int(input("Enter X coordinate for text position (1-100) 50 to palce in center :"))
    y = int(input("Enter Y coordinate for text position (1-100) 50 to palce in center :"))
    # Ask for RGB color input in format: R,G,B
    rgb_input = input("Enter text color in RGB format (e.g., 255,255,255 for white): ")
    text_color = tuple(map(int, rgb_input.split(',')))  # Convert input to a tuple of integers

    while True:
        create_usage_image(font_size, x, y, text_color)
        time.sleep(5)
except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to close...")