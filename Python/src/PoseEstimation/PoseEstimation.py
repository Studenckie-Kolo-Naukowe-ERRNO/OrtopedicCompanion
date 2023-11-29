from ultralytics import YOLO
import torch
import warnings

device = 'cuda' if torch.cuda.is_available() else 'cpu'
if device == 'cpu':
    warnings.warn("The model will be using the *CPU*, instead of the CUDA.")

model = YOLO('yolov8m-pose.pt')
model.to(device)

results = model(source="sample.jpg", show=True, conf=0.3, save=True)

print(results)
