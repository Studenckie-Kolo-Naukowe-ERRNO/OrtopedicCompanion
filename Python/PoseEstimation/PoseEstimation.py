from ultralytics import YOLO
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# pytest assert pd.__versio__
#  ensure that your CUDA and CuDNN versions are compatible with your PyTorch installation,
#  and PyTorch is properly configured to use CUDA. Additionally, you can set the GPU device using torch.
#torch.cuda.set_device(0)  # Set to your desired GPU number
# To run YOLOv8 on GPU, you need to ensure that your CUDA and CuDNN versions are compatible with your PyTorch installation, and PyTorch is properly configured to use CUDA. Additionally, you can set the GPU device using torch.cuda.set_device(0) before initializing the YOLOv8 model.
model = YOLO('yolov8m-pose.pt')
print(model.device.type)
#results = model(source="sample.jpg", show=True, conf=0.3, save=True)

