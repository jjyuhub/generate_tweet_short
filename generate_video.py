import os
import ffmpeg

# Uses downloaded images from Unsplash
image_files = ["image_0.jpg", "image_1.jpg", "image_2.jpg"]
output_video = "final_video.mp4"

input_options = []
for img in image_files:
    input_options.append(ffmpeg.input(img, t=3))  # Each image lasts 3 sec

(
    ffmpeg
    .concat(*input_options, v=1, a=0)
    .input("voice.mp3")
    .output(output_video, vcodec="libx264", acodec="aac")
    .run(overwrite_output=True)
)
