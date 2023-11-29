from ultralytics import YOLO
import torch

model_name = 'yolov8m-pose.pt'


def test_if_model_works():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = YOLO(model_name)
    model.to(device)
    print(model.device.type)
    results = model(source="sample.jpg", show=False, conf=0.3, save=False)
    assert(results is not None)


def test_if_model_uses_cuda():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = YOLO(model_name)
    model.to(device)
    device = model.device.type
    assert(device == 'cuda')

