import pytest
import torch

def test_gpu_is_working():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    assert(device == 'cuda')
