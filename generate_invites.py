from pdf2image import convert_from_path, exceptions as pdf2img_exceptions
from PIL import ImageDraw, ImageFont
import pandas as pd
import os
import sys

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
    "C:/Windows/Fonts/palab.ttf",                            # Windows bold
    "/System/Library/Fonts/Georgia Bold.ttf",                # Mac fallback
    "C:/Windows/Fonts/georgiab.ttf",                         # Windows fallback
]

# Validate input files
def check_file_exists(path, description):
    if not os.path.exists(path):
        print(f"\n❌ ERROR: Cannot find the {description} file: '{path}'")
        print("Please make sure the file is placed in this folder and the name is correct (including the extension).")
        sys.exit(1)

check_file_exists(PDF_PATH, "PDF template")
check_file_exists(NAMES_CSV, "CSV with invitee names")

# Load bold font
font = None
for path in FONT_PATHS:
    try:
        font = ImageFont.truetype(path, FONT_SIZE)
        print(f"✅ Using font: {path}")
        break
    except:
        continue

if font is None:
    print("❌ ERROR: No bold font found on your system.")
    print("Please install a bold font like Palatino Bold or Georgia Bold.")
    sys.exit(1)

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Convert PDF to image
try:
    pages = convert_from_path(PDF_PATH, dpi=300)
except pdf2img_exceptions.PDFPageCountError:
    print(f"\n❌ ERROR: The PDF file '{PDF_PATH}' cannot be opened or read.")
    print("Possible reasons:")
    print("- The file is corrupted or not a valid PDF.")
    print("- The file is open in another program.")
    print("- The path is incorrect.")
    sys.exit(1)

base_img = pages[0]

# Load invitee names
try:
    df = pd.read_csv(NAMES_CSV)
except Exception as e:
    print(f"\n❌ ERROR: Could not read the CSV file '{NAMES_CSV}'.")
    print("Please ensure the file is a valid CSV and has a column named 'Name'.")
    print(f"Details: {e}")
    sys.exit(1)

if 'Name' not in df.columns:
    print(f"\n❌ ERROR: The CSV file must contain a column named 'Name'.")
    sys.exit(1)

# Initialize counters and failed list
success_count = 0
failed = []

# Generate invites
for index, name in enumerate(df["Name"], start=1):
    try:
        img = base_img.copy()
        draw = ImageDraw.Draw(img)

        message = f"{name},"
        text_width = draw.textlength(message, font=font)
        x_position = (img.width - text_width) / 2

        draw.text((x_position, TEXT_Y_POSITION), message, fill=COLOR, font=font)

        filename = f"{OUTPUT_FOLDER}/invite_{name.replace(' ', '_')}.png"
        img.save(filename)
        print(f"✅ [{index}] Saved: {filename}")
        success_count += 1

    except Exception as e:
        print(f"❌ [{index}] Failed to generate invite for '{name}': {e}")
        failed.append(name)

# Final summary
print("\n📊 Generation Summary")
print(f"✅ Successfully generated: {success_count}")
print(f"❌ Failed: {len(failed)}")

if failed:
    print("⚠️ Failed entries:")
    for name in failed:
        print(f" - {name}")

print("\n🎉 Process complete!")
