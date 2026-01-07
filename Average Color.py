from PIL import Image, ImageDraw, ImageFont
import random
import os


def average_color(image_path):
    try:
        # Open the image
        img = Image.open(image_path).convert("RGB")
        # Resize the image to 1x1 to get the average color
        img = img.resize((1, 1))
        # Get the pixel value
        avg_color = img.getpixel((0, 0))
        return avg_color
    except Exception as e:
        print(f"Error: {e}")
        return None


def generate_color_name(rgb):
    # Define color descriptors
    adjectives = [
        "Bright", "Soft", "Mellow", "Vivid", "Muted",
        "Radiant", "Dusky", "Dreamy", "Bold", "Gentle"
    ]
    base_colors = [
        "Red", "Blue", "Green", "Yellow", "Orange",
        "Purple", "Pink", "Gray", "Teal", "Coral"
    ]

    # Generate a random color name
    name = f"{random.choice(adjectives)} {random.choice(base_colors)}"
    return name


def display_color(rgb, color_name):
    # Create an image to represent the color
    color_image = Image.new("RGB", (200, 200), rgb)
    draw = ImageDraw.Draw(color_image)

    # Optionally, add text showing the color name and RGB value
    text = f"{color_name}\nRGB: {rgb}"
    try:
        # Load a font (ensure 'arial.ttf' exists or replace with another font)
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        # Default font
        font = ImageFont.load_default()

    # Calculate text size and center it
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((200 - text_width) // 2, (200 - text_height) // 2)

    # Add text to the image
    draw.text(text_position, text, fill=(255, 255, 255), font=font)

    # Save the image
    output_path = "average_color.png"
    color_image.save(output_path)
    print(f"Average color displayed and saved as '{output_path}'.")


# Main script
if __name__ == "__main__":
    # Replace 'your_image.jpg' with the path to your image
    image_path = ""
    avg_color = average_color(image_path)
    if avg_color:
        # Generate a human-readable name
        color_name = generate_color_name(avg_color)
        print(f"The average color of the image is {color_name}, with an RGB value of {avg_color}.")
        # Display the color visually
        display_color(avg_color, color_name)
