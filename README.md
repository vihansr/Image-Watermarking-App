# Image Watermarking App

## Overview
This is a simple Python-based GUI application that allows users to add multiple watermarks to an image using a grid pattern. It is built using **PIL (Pillow)** for image processing and **Tkinter** for the user interface.

## Features
- Select an image via a file dialog.
- Add a watermark text that repeats multiple times across the image.
- Uses a semi-transparent watermark for better visibility.
- User-friendly GUI with an entry box to input custom watermark text.

## Requirements
Make sure you have the following dependencies installed:
```sh
pip install pillow
```

## How to Run
1. Clone this repository or download the script.
2. Run the script using Python:
   ```sh
   python main.py
   ```
3. A GUI window will open.
4. Enter the watermark text and click **Convert**.
5. Select an image file from your system.
6. The image will be displayed with watermarks applied.

## File Structure
```
/your_project_directory
│── main.py         # Main script for the application
│── README.md       # Documentation (this file)
```

## Future Enhancements
- Option to adjust watermark opacity.
- Save the watermarked image instead of just displaying it.
- Allow users to choose different font styles and sizes.

## License
This project is open-source and free to use.

