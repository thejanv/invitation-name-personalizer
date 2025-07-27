# Personalized Name Addition Tool - Setup Guide

## What This Tool Does

This name addition tool automatically personalizes your invitations by taking your template invitation (PDF file) and adding individual guest names to create unique copies for each person. Instead of manually writing or typing each person's name on separate invitations, you can personalize hundreds of invitations in seconds!

## Step 1: Install Python on Your Computer

Python is the programming language that runs this tool. Don't worry - you won't need to learn programming!

### For Windows Users:
1. Go to [python.org](https://python.org)
2. Click "Download Python" (get version 3.8 or newer)
3. **IMPORTANT**: When installing, check the box that says "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete

### For Mac Users:
1. Go to [python.org](https://python.org)
2. Click "Download Python" (get version 3.8 or newer)
3. Open the downloaded file and follow installation steps
4. Python should be ready to use

### To Check If Python Installed Correctly:
1. **Windows**: Press `Windows key + R`, type `cmd`, press Enter
2. **Mac**: Press `Cmd + Space`, type `terminal`, press Enter
3. Type: `python --version` and press Enter
4. You should see something like "Python 3.11.0" (numbers may vary)

## Step 2: Install Required Tools

The name addition tool needs special tools to work with PDFs and images. These are listed in a file called `requirements.txt`.

### Install the Tools:
1. Open Command Prompt (Windows) or Terminal (Mac) as described above
2. Navigate to the folder where you saved the invitation generator files:
   - Type: `cd ` (with a space after cd)
   - Drag the folder from your file explorer into the command window
   - Press Enter
3. Install the required tools by typing: `pip install -r requirements.txt`
4. Press Enter and wait for installation to complete (may take a few minutes)

## Step 3: Prepare Your Files

### Create Your Template (base_invitation.pdf)
- Design your invitation in any program (Canva, Word, Photoshop, etc.)
- Leave space where you want the guest's name to appear
- Save it as a PDF file named exactly: `base_invitation.pdf`

### Create Your Guest List (invitees.csv)
- Open Excel, Google Sheets, or any spreadsheet program
- Create a column with the header "Name" (exactly like that)
- List all your guests' names below, one per row
- Save as CSV format with filename: `invitees.csv`

**Example spreadsheet:**
```
Name
John Smith
Sarah Johnson
Mike Davis
Lisa Brown
```

## Step 4: Organize Your Files

Create a folder for your project and put these files inside:
```
Your Invitation Project/
├── base_invitation.pdf (your template)
├── invitees.csv (your guest list)
├── generate_invites.py (the script)
└── requirements.txt (list of tools needed)
```

## Step 5: Run the Invitation Generator

1. Open Command Prompt (Windows) or Terminal (Mac)
2. Navigate to your project folder:
   - Type: `cd ` (with space)
   - Drag your project folder into the command window
   - Press Enter
3. Run the name adder by typing: `python generate_invites.py`
4. Press Enter and watch the magic happen!

## What You'll See When Running

The program will display messages like:
```
Using font: /System/Library/Fonts/Georgia Bold.ttf
Saved: output_invites/invite_John_Smith.png
Saved: output_invites/invite_Sarah_Johnson.png
Saved: output_invites/invite_Mike_Davis.png
```

## Your Results

After running, you'll find a new folder called `output_invites` containing:
- Individual PNG image files for each guest
- High-resolution files perfect for printing
- Files named clearly: `invite_John_Smith.png`, `invite_Sarah_Johnson.png`, etc.

## Customizing Your Invitations

You can adjust these settings by editing the script (ask someone tech-savvy to help):

### Text Appearance
- **FONT_SIZE = 48** - Make this number smaller for smaller text, larger for bigger text
- **TEXT_Y_POSITION = 1500** - Change this to move names up (smaller) or down (larger)
- **COLOR = (0, 0, 0)** - This is black; change to (255, 255, 255) for white text

## Troubleshooting Common Issues

### "Python is not recognized" (Windows)
- You need to reinstall Python and check "Add Python to PATH"

### "No module named 'pdf2image'" 
- Run the pip install command again: `pip install -r requirements.txt`

### "No suitable font found"
- The program will try to find a bold font automatically
- If this fails, install a bold font on your computer

### Names don't fit or look wrong
- Try changing FONT_SIZE to 36 or 24
- Adjust TEXT_Y_POSITION to move names up or down

### PDF won't convert
- Make sure your PDF file is named exactly `base_invitation.pdf`
- Try saving your PDF from a different program

## Tips for Success

### Template Design
- Use simple, clear fonts in your original design
- Leave plenty of white space where names will appear
- Test with your longest guest name to ensure it fits

### Guest List
- Double-check all spelling before running
- Avoid special characters in names (they might cause file issues)
- Use the exact name format you want on invitations

### File Management
- Keep all files in the same folder
- Don't change the exact filenames the script expects
- Make backup copies of your original files

## Perfect For

- Wedding invitations
- Birthday party invites  
- Corporate events
- Graduation parties
- Holiday cards
- Any event needing personalized invitations

## Getting Help

If you run into issues:
1. Double-check all filenames match exactly
2. Make sure Python installed correctly
3. Verify all files are in the same folder
4. Ask a tech-savvy friend to help with customization

This tool can save you hours of work and create professional-looking personalized invitations for any size event!
