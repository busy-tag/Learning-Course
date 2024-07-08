from PIL import Image, ImageDraw, ImageFont

def create_text_to_image(width, height, background_color, text, font_path=None, font_size=60, text_color=(255, 255, 255), output_file="text_to_image.png"):
    # Create a new image with the given background color
    image = Image.new("RGB", (width, height), color=background_color)
    
    # Initialize the drawing context
    draw = ImageDraw.Draw(image)
    
    # Load a font or use the default one
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    # Calculate the bounding box of the text to be drawn
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate the position to center the text
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw the text on the image at the calculated position
    draw.text((text_x, text_y), text, font=font, fill=text_color)
    
    # Save the image to the specified file
    image.save(output_file)
    print(f"New image created and saved as {output_file}")

def get_color_input(prompt):
    while True:
        try:
            color = input(prompt).strip().strip('()')
            r, g, b = map(int, color.split(','))
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return (r, g, b)
            else:
                print("Each value must be between 0 and 255.")
        except ValueError:
            print("Please enter the color as three comma-separated values (e.g., 255, 0, 0).")

def get_font_size_input(prompt):
    while True:
        try:
            font_size = int(input(prompt).strip())
            if font_size > 0:
                return font_size
            else:
                print("Please enter a positive number for the font size.")
        except ValueError:
            print("Please enter a valid number for the font size.")

def main():
    # Prompt the user for the text to display
    text = input("Enter the text to display on the image: ").strip()
    
    # If no text is provided, use a default text
    if not text:
        text = "Hello, World!"

    # Prompt the user for the background color
    background_color = get_color_input("Enter the background color as RGB (e.g., 255, 255, 255): ")

    # Prompt the user for the text color
    text_color = get_color_input("Enter the text color as RGB (e.g., 0, 0, 0): ")

    # Prompt the user for the font size
    font_size = get_font_size_input("Enter the font size (e.g., 40): ")

    # Set other parameters for the image
    width = 240                   
    height = 280                  
    font_path = r"D:\neon.ttf"  # Optional path to font file
    output_file = r"D:\text_to_image.png"  # Output file name

    # Call the function to create the image
    create_text_to_image(width, height, background_color, text, font_path, font_size, text_color, output_file)

if __name__ == "__main__":
    main()