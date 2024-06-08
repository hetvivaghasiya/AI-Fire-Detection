import gradio as gr
import torch
from PIL import Image
import pathlib
import os

os.chdir("./demo")
temp = pathlib.PosixPath
pathlib.PosixPath  = pathlib.WindowsPath

model = torch.hub.load("ultralytics/yolov5", "custom", path="E:\presentation\Hetvi_Vaghasiya\fire-detection-from-images-master\pytorch\object-detection\yolov5\deepstack\demo\best.pt" , force_reload=True)


def yolo(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.LANCZOS)  # resize
    results = model(im)
    results.render()
    return Image.fromarray(results.ims[0])


inputs = gr.inputs.Image(type='pil', label="Original Image")
outputs = gr.outputs.Image(type="pil", label="Output Image")

title = "YOLOv5"
description = "YOLOv5 demo for fire detection. Upload an image or click an example image to use."
article = ""
examples = [['pan-fire.jpg'], ['fire-basket.jpg']]
gr.Interface(yolo, inputs, outputs, title=title, description=description, article=article, examples=examples).launch(
    debug=True)

pathlib.PosixPath = temp