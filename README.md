# ImFusion Public Python Demos

[ImFusion SDK](https://www.imfusion.com/products-overview/software-development-kit/) is a high-performance computing platform for custom medical imaging solutions.
This repository demonstrates the capabilities of the Python integrations of the ImFusion SDK.
These come in two flavors:

- `imfusion-sdk` is a standalone Python package that provides bindings to a subset of the powerful ImFusion C++ SDK. You can obtain it directly from our package index (https://pypi.imfusion.com/simple) using `pip` and it can be used in without any other ImFusion software through a regular Python interpreter.
  - This repository contains demo material for the `imfusion` module in the [imfusion-sdk](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk) folder in the form of interactive Jupyter notebooks.
  - The notebooks demonstrate basic usage of the package and how to manipulate images, invoke algorithms, build data pipelines, perform ML model inference, perform image registration and interact with ImFusion Labels projects.
  - Beyond the base capabilites of the `imfusion-sdk` package, our ["Starter" and "Professional" SDK offerings](https://imfusion.com/sdk-pricing/) also include specialized, modality-specific modules:
    - [imfusion-sdk-computed_tomography](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-computed_tomography) contains demo notebooks for the `imfusion.computed_tomography` submodule.
    - [imfusion-sdk-vision](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-vision) contains demo notebooks for the `imfusion.vision` submodule.
- `PythonPlugin` is a plugin for the ImFusion Suite that allows the use of the Python programming language in the Suite. Through the `PythonPlugin` we can integrate a Python interpreter into the Suite, which allows for extending its functionality through Python code. The folder [PythonPlugin](https://github.com/ImFusionGmbH/public-python-demos/tree/master/PythonPlugin) contains two such examples:
  - `python_algorithm_demo.py` shows how you can write your own algorithm and Python and call it from the ImFusion Suite.
  - `python_algorithm_monai_filter.py` contains another demonstration of the Python Algorithm mechanism using the third-party `monai` package.
  - `python_operation_demo.py` is similar to the one above but shows how to create an ML Operation, which is often used as part of data pipelines, instead.

You can find more details about our Python integrations in our [documentation](https://docs.imfusion.com/python/index.html).
For more information and news regarding our company, please visit our [website](https://www.imfusion.com/).
