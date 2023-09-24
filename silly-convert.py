import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))

# Function to convert GIF to WebM with higher quality
def convert_to_webm(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.gif'):
                gif_file = os.path.join(root, file)
                webm_file = os.path.splitext(gif_file)[0] + '.webm'
                try:
                    clip = VideoFileClip(gif_file)
                    clip.write_videofile(
                        webm_file,
                        codec='libvpx',
                        preset='ultrafast',  # Adjust the preset for higher quality
                        threads=4,
                        bitrate='5000k',  # Increase the bitrate for better quality
                        audio=False,  # Disable audio (if not needed)
                    )
                    clip.close()
                    os.remove(gif_file)
                except Exception as e:
                    print(f"Error converting {gif_file} to WebM: {e}")

# Function to select a folder
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_to_webm(folder_path)
        result_label.config(text="Conversion complete! ^_^")

# Create the main window
window = tk.Tk()
window.title("silly-convert")

# Load the logo image from the same folder as the script
logo_image_path = os.path.join(script_directory, "logo.png")
logo_image = tk.PhotoImage(file=logo_image_path)

# Create a label to display the logo at the top center
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()

# Create and configure a label
label = tk.Label(window, text="Select a folder containing GIFs to convert to high-quality WebM:")
label.pack(pady=10)

# Create a button to select a folder
select_button = tk.Button(window, text="Select Folder", command=select_folder)
select_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Set the application icon from the same folder as the script
icon_path = os.path.join(script_directory, "icon.ico")
window.iconbitmap(default=icon_path)

# Run the application
window.mainloop()