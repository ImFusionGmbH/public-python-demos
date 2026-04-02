# Working with stand-alone `imfusion-sdk` Python package

This demo highlights the usage of `imfusion-sdk` for a variety of medical imaging tasks.
The `imfusion-sdk` package contains Python bindings for a subset of the ImFusion C++ SDK.
It is available for the currently supported Python versions. You can check the currently available Python wheels on [our package index](https://pypi.imfusion.com/simple).
This repository assumes you're on python 3.11 (otherwise the pinned versions in `requirements.txt` might not be available).
We recommend using an official python interpreter. The latest stable releases can be found on [python.org](https://www.python.org/downloads/).
To run the notebooks in this demo you need to follow the steps detailed below.

### 1. Set up a python environment

```Bash
$ cd <path-to-this-repositories-root>
$ python3 -m venv demo-env
$ demo-env\Scripts\activate.bat # (Windows) 
$ source demo-env/bin/activate  # (Unix and MacOS)
$ (demo-env) pip install -r imfusion_sdk/requirements.txt
```

### 2. Activating `imfusion-sdk`

Activate the package with the license key.
If you don't yet have one, please visit our [webshop](https://imfusion.com/sdk-pricing/), where you can get a free key for non-commercial use.


Linux and MacOS:
```Bash
(demo-env) IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX python -c "import imfusion" 
```

Windows:
```Bash
(demo-env) set IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX
(demo-env) python -c "import imfusion" 
```

After successful activation you can verify the installation with the command

```Bash
$ python -c "import imfusion;print(imfusion.info())"
```

### 3. Start a Jupyter Server
Now that everything is set up you can start going through the notebooks. For this you have to start jupyter using:

```bash
(demo-env) cd imfusion_sdk/
(demo-env) jupyter notebook
```

This should open up a browser with a running jupyter session, where you can browse the notebooks.

## Acknowledgements

Data for this tutorial is taken from:
	
National Cancer Institute Clinical Proteomic Tumor Analysis Consortium (CPTAC). (2019).  
The Clinical Proteomic Tumor Analysis Consortium Uterine Corpus Endometrial Carcinoma Collection (CPTAC-UCEC) (Version 12) [Data set].  
The Cancer Imaging Archive.  
https://doi.org/10.7937/K9/TCIA.2018.3R3JUISW
