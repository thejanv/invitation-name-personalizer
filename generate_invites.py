from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFont
import pandas as pd
import os

# CONFIGURATION
PDF_PATH = "base_invitation.pdf"
NAMES_CSV = "invitees.csv"
OUTPUT_FOLDER = "output_invites"

FONT_SIZE = 48
TEXT_Y_POSITION = 1500
COLOR = (0, 0, 0)

# Font settings (try these in order)
FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Palatino Bold.ttf",  # Mac bold
    "C:/Windows/Fonts/palab.ttf",                           # Windows bold
    "/System/Library/Fonts/Georgia Bold.ttf",               # Mac fallback
    "C:/Windows/Fonts/georgiab.ttf",                        # Windows fallback
    # Add other bold font paths here
]

# Find first available bold font
font = None
for path in FONT_PATHS:
    try:
        font = ImageFont.truetype(path, FONT_SIZE)
        print(f"Using font: {path}")
        break
    except:
        continue

if font is None:
    raise FileNotFoundError("No suitable bold font found - please install a bold variant")

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Convert PDF to image
pages = convert_from_path(PDF_PATH, dpi=300)
base_img = pages[0]

# Load invitee names
df = pd.read_csv(NAMES_CSV)

for name in df["Name"]:
    img = base_img.copy()
    draw = ImageDraw.Draw(img)
    
    message = f"{name},"
    
    # Center calculation
    text_width = draw.textlength(message, font=font)
    x_position = (img.width - text_width) / 2
    
    # Draw gold text with bold font
    draw.text((x_position, TEXT_Y_POSITION), message, fill=COLOR, font=font)
    
    filename = f"{OUTPUT_FOLDER}/invite_{name.replace(' ', '_')}.png"
    img.save(filename)
    print(f"Saved: {filename}")
