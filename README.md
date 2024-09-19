# ImFusion Public Python Demos

[ImFusion SDK](https://www.imfusion.com/solutions/technology-portfolio/340-sdk) is a high-performance computing platform for custom medical imaging solutions.
This repository demonstrates the capabilities of the Python integrations of the ImFusion SDK.
These come in two flavors:

- `imfusion-sdk` is a standalone Python package that provides bindings to a subset of the powerful ImFusion C++ SDK. You can obtain it directly from PyPI using `pip` and it can be used in without any other ImFusion software through a regular Python interpreter.
  - This repository contains demo material for `imfusion-sdk` in the [imfusion_sdk](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion_sdk) folder (changed `-` to `_` for compatibility with Python's import system) in the form of interactive Jupyter notebooks.
  - The notebooks demonstrate basic usage of the package and how to manipulate images, invoke algorithms, build data pipelines, perform ML model inference, perform image registration and interact with ImFusion Labels projects.
- `PythonPlugin` is a plugin for the ImFusion Suite that allows the use of the Python programming language in the Suite. Through the `PythonPlugin` we can integrate a Python interpreter into the Suite, which allows for extending its functionality through Python code. The folder [PythonPlugin](https://github.com/ImFusionGmbH/public-python-demos/tree/master/PythonPlugin) contains two such examples:
  - `python_algorithm_demo` shows how you can write your own algorithm and Python and call it from the ImFusion Suite
  - `python_operation_demo` is similar to the one above but shows how to create an ML Operation, which is often used as part of data pipelines, instead.

You find more details about our Python integrations in our [documentation](https://docs.imfusion.com/python/README.html).
For more information and news regarding our company, please visit our [website](https://www.imfusion.com/).
