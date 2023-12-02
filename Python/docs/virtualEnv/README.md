
# Setting up the virtual envoirement
------
### Use Python 3.11.x
https://www.python.org/downloads/release/python-3115/
</br>*Note:* You need to download also the developer tool from microsoft store in order to use it as a cli.
### Install pip and virtualenv
```
python -m pip install -U pip
pip install virtualenv
```
How to create a virtual environment?
```
virtualenv virtualenv_name
python -m venv virtualenv_name // alternative
myenv\Scripts\activate  // to activate *Note:* it's not a .bat extension
```
after all u can close the venv by typing 
```
deactivate
```

# Good version of CUDA
*Based on thread: https://stackoverflow.com/questions/60987997/why-torch-cuda-is-available-returns-false-even-after-installing-pytorch-with*
</br>In order to use CUDA you need to have an NVIDIA graphics card.
1. Check your graphics driver and gpu model.
2. Search the compute capability on the link below:
https://en.wikipedia.org/wiki/CUDA#GPUs_supported
3. On the same link check the newest CUDA your graphics card can use.
</br>Best case scenario --> CUDA 1.12.
4. Install the correct version with the command generated in the link below:
</br>https://pytorch.org/get-started/locally/
</br>In my case it looks like this:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Conclusion

After all, all other packages need should be installed properly for this project.
The Pose Estimator class will send a warning if the CUDA won't work.

You can check it on your own like this:
```
>>> import torch
>>> torch.zeros(1).cuda()
```
If there will be an error, it means something went wrong.
You can check if it's working on cuda like below:
```
>>> 'cuda' if torch.cuda.is_available() else 'cpu'
```
