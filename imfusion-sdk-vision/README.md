# Working with stand-alone `imfusion-sdk` Python package

This demo highlights the usage of `vision` component of `imfusion-sdk` for a variety of computer vision tasks.
The `imfusion-sdk` package contains Python bindings for a subset of the ImFusion C++ SDK.
It is available for the currently supported Python versions. You can check the currently available Python wheels on [PyPI](https://pypi.org/project/imfusion-sdk/).
This repository assumes you're on python 3.11 (Otherwise the pinned versions in `requirements.txt` might not be available).
We recommend using a official python interpreter. The latest stable releases can be found on [python.org](https://www.python.org/downloads/).
To run the notebooks in this demo you need to follow the steps detailed below.

**Note:** The `vision` module is only available in the "Professional" offering of our SDK. 

### 1. Set up a python environment

```Bash
$ python3 -m venv demo-env-vision
$ demo-env-vision\Scripts\activate.bat # (Windows) 
$ source demo-env-vision/bin/activate  # (Unix and MacOS)
$ (demo-env-vision) pip install -r imfusion_sdk_vision/requirements.txt  # assuming your working directory is the root of this repo  
```

### 2. Activating `imfusion-sdk`

Activate the package with the license key.
If you don't yet have one, please visit our [webshop](https://shop.imfusion.com/collections/demo-versions/products/imfusion-python-sdk), where you can get a free key during our beta release.


Linux and MacOS:
```Bash
(demo-env-vision) IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX python -c "from imfusion import vision" 
```

Windows:
```Bash
(demo-env-vision) set IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
(demo-env-vision) python -c "from imfusion import vision" 
```

After successful activation you can verify the installation with the command

```Bash
$ python -c "import imfusion;print(imfusion.info())"
```

### 3. Start a Jupyter Server
Now that everything is set up you can start going through the notebooks. For this you have to start jupyter using:

```bash
(demo-env-vision) cd imfusion_sdk_vision/
(demo-env-vision) jupyter notebook
```

This should open up a browser with a running jupyter session, where you can browse the notebooks.

## Acknowledgements

Data for this tutorial is taken from:
	
- [D. Scharstein, H. Hirschmüller, Y. Kitajima, G. Krathwohl, N. Nesic, X. Wang, and P. Westling. High-resolution stereo datasets with subpixel-accurate ground truth.
In German Conference on Pattern Recognition (GCPR 2014), Münster, Germany, September 2014.](https://www.cs.middlebury.edu/~schar/papers/datasets-gcpr2014.pdf)
