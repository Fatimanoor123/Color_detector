# 🎨 Color Detection Using OpenCV


## 📝 Overview
This project is a real-time color detection system using OpenCV. It captures video from a webcam and detects a specific color (default: blue) by drawing a bounding box around the detected region.

---

## 🎯 Features
- 🔍 Real-time color detection using OpenCV.
- 🎥 Bounding box around detected color regions.
- 🎨 Adjustable color detection using HSV limits.

---

## 📦 Installation
Follow these steps to set up the project:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/color-detection.git
   cd color-detection

## 2️⃣ Install Dependencies
pip install opencv-python numpy pillow

## 🚀 Usage
To run the project, execute the following command
python color_detection.py
🖥️ The webcam will open, and it will detect the default color (blue).
🔹 Press q to exit the application.

## 🛠️ How It Works
1️⃣ Captures a frame from the webcam.
2️⃣ Converts the frame to the HSV color space.
3️⃣ Uses get_limits() function to define the HSV range of the target color.
4️⃣ Creates a mask and detects the region with the specified color.
5️⃣ Draws a bounding box around the detected color.
6️⃣ Displays the result in real-time.


## 🎨 Customization
You can modify the color detection settings by changing the blue variable in color_detection.py:
blue = [255, 0, 0]  # Change this to detect another color
📂 File Structure
📁 color_detection.py → Main script for capturing video & detecting colors.
📁 utils.py → Helper functions to determine HSV color limits.


## 📸 Example Output
![image](https://github.com/user-attachments/assets/9ff00200-7afe-41ce-951c-f1db7739b6df)
