from ultralytics import YOLO

import sys
import torch


def test_python_version():
    py_ver = sys.version[0:3]
    assert(py_ver == '3.1')
    # python >= 3.10


def test_cuda_version():
    assert(torch.version.cuda == "12.1")


def test_pytorch_version():
    assert(torch.__version__ == "2.1.1+cu121")

