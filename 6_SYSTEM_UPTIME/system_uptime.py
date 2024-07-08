import psutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def get_system_uptime():
    # Get boot time using psutil
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    
    # Calculate the uptime
    now = datetime.now()
    uptime = now - boot_time
    
    return uptime

def format_timedelta(delta):
    # Helper function to format the timedelta object into a human-readable format
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Create a formatted string with each time unit on a new line
    formatted_string = (f"System Uptime:\n"
                        f"{days} days,\n"
                        f"{hours} hours,\n"
                        f"{minutes} minutes,\n"
                        f"{seconds} seconds")
    
    return formatted_string

def draw_text_on_image(width, height, background_color, text, font_path, font_size, text_color, output_file):
    # Create a new image with the given background color
    image = Image.new("RGB", (width, height), color=background_color)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Load the specified font
    font = ImageFont.truetype(font_path, font_size)
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Calculate the total height required for all lines of text
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in lines)
    
    # Calculate the initial y position to start drawing the text, so it will be centered vertically
    current_y = (height - total_text_height) // 2
    
    # Draw each line of text
    for line in lines:
        text_bbox = draw.textbbox((0, 0), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        
        # Calculate the x position to center the text horizontally
        text_x = (width - text_width) // 2
        
        # Draw the text on the image
        draw.text((text_x, current_y), line, font=font, fill=text_color)
        
        # Move to the next line position
        line_height = text_bbox[3] - text_bbox[1]
        current_y += line_height
    
    # Save the image
    image.save(output_file)
    print(f"New image created and saved as {output_file}")

def main():
    uptime = get_system_uptime()
    formatted_uptime = format_timedelta(uptime)
    print(f"Formatted Uptime:\n{formatted_uptime}")
    
    # Define image size, colors, font, and output file
    width = 240
    height = 280
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text
    font_size = 35  # Adjust the font size as needed
    font_path = r"D:\neon.ttf"  # Specify the path to your .ttf font file
    output_file = r"D:\uptime_image.png"  # Save the output image in the D: drive
    
    # Draw the formatted uptime on the image
    draw_text_on_image(width, height, background_color, formatted_uptime, font_path, font_size, text_color, output_file)

if __name__ == "__main__":
    main()