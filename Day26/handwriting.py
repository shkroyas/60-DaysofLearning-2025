from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output_path="handwriting.png"):
    # Load a handwriting-like font
    font = ImageFont.truetype("PatrickHand-Regular.ttf", 32)

    # Estimate size
    lines = text.split("\n")
    width = max([font.getlength(line) for line in lines]) + 20
    height = len(lines) * 40 + 20

    # Create image
    img = Image.new("RGB", (int(width), height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw each line
    y = 10
    for line in lines:
        draw.text((10, y), line, fill=(0, 0, 0), font=font)
        y += 40

    img.save(output_path)
    print(f"Handwriting saved as {output_path}")

# Example usage
text = """This is an example
of handwriting effect
generated."""
text_to_handwriting(text)
