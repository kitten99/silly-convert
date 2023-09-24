import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

script_directory = os.path.dirname(os.path.realpath(__file__))

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
                        preset='ultrafast',
                        threads=4,
                        bitrate='5000k',
                        audio=False,
                    )
                    clip.close()
                    os.remove(gif_file)
                except Exception as e:
                    print(f"Error converting {gif_file} to WebM: {e}")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_to_webm(folder_path)
        result_label.config(text="Conversion complete! ^_^")

window = tk.Tk()
window.title("silly-convert")

window.resizable(0, 0)

logo_image_path = os.path.join(script_directory, "logo.png")
logo_image = tk.PhotoImage(file=logo_image_path)

logo_label = tk.Label(window, image=logo_image)
logo_label.pack()

label = tk.Label(window, text="Select a folder containing GIFs to convert to WebM:")
label.pack(pady=10)

select_button = tk.Button(window, text="Select Folder", command=select_folder)
select_button.pack()

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
