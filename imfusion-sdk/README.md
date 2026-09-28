# Working with the standalone `imfusion-sdk` Python package

This demo highlights the usage of the `imfusion-sdk` for a variety of medical imaging tasks. The `imfusion-sdk` package provides Python bindings for the core functionality of the ImFusion C++ SDK.
Pre-built wheels are available for Python 3.10–3.14 on [our package index](https://pypi.imfusion.com/simple). We recommend using an official Python interpreter, which you can download from [python.org](https://www.python.org/downloads/).
To run the notebooks in this repository, follow the setup instructions below.

### 1. Set up a Python environment

```bash
$ cd <path-to-this-repository-root>
$ python3 -m venv demo-env # or `uv venv demo-env`
$ demo-env\Scripts\activate.bat # (Windows)
$ source demo-env/bin/activate  # (Unix and macOS)
$ (demo-env) pip install -r imfusion-sdk/requirements.txt # or `uv pip install -r imfusion-sdk/requirements.txt`
```

> **NOTE:**
> You may need to adjust the pinned dependency versions in `requirements.txt` depending on the Python version you are using.

### 2. Activate `imfusion-sdk`

Activate the package with the license key.
If you don't yet have one, please visit our [webshop](https://imfusion.com/sdk-pricing/), where you can get a free key for non-commercial use.

Linux and macOS:
```bash
(demo-env) IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX python -c "import imfusion"
```

Windows:
```bash
(demo-env) set IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX
(demo-env) python -c "import imfusion"
```

After successful activation, you can verify the installation with the command

```bash
$ python -c "import imfusion;print(imfusion.info())"
```

### 3. Start a Jupyter server
Now that everything is set up, you can start going through the notebooks. For this, you have to start Jupyter using:

```bash
(demo-env) cd imfusion-sdk/
(demo-env) jupyter notebook
```

This should open up a browser with a running Jupyter session, where you can run and interact with the notebooks.
