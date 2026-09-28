# ImFusion Public Python Demos

The [ImFusion SDK](https://www.imfusion.com/products-overview/software-development-kit/) is a high-performance computing platform for custom medical imaging solutions.
This repository contains tutorial notebooks and examples for selected Python integrations around ImFusion products.

## ImFusion SDK Bindings

The ImFusion SDK Python packages provide modular access to the powerful ImFusion C++ SDK, ranging from the standalone base package to specialized extension modules for domain-specific workflows.

The base package and selected extension modules are available in the Free plan for non-commercial research use, while additional extension modules are part of our ["Starter" and "Professional" SDK offerings](https://imfusion.com/sdk-pricing/).

> **Note:** The lists below cover the packages demonstrated in this repository. Additional packages and modules are available outside this tutorial collection.

- Free plan:
  - [imfusion-sdk](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk) provides the core ImFusion C++ SDK functionalities.
  - [imfusion-sdk-dicom](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-dicom) shows how to work with DICOM images, RT Structure Sets, and DICOM Segmentation I/O.
  - [imfusion-sdk-machinelearning](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-machinelearning) contains demo notebooks for data pipelines and model inference.
  - [imfusion-sdk-registration](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-registration) contains demo notebooks for image registration.

- Starter and Professional SDK offerings:
  - [imfusion-sdk-computed_tomography](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-computed_tomography) demonstrates CT geometry, simulation, reconstruction, and registration workflows.
  - [imfusion-sdk-vision](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-vision) demonstrates computer vision workflows such as camera calibration, stereo reconstruction, and image processing.

## ImFusion Labels Bindings

[imfusion-sdk-labels](https://github.com/ImFusionGmbH/public-python-demos/tree/master/imfusion-sdk-labels) demonstrates how to create, inspect, and modify ImFusion Labels projects from Python. The package is available through our [ImFusion Labels plans](https://imfusion.com/labels-pricing/).

## ImFusion Suite Integration

The `PythonPlugin` embeds a Python interpreter into the ImFusion Suite, enabling you to extend the Suite's functionality with Python code. The [PythonPlugin examples](https://github.com/ImFusionGmbH/public-python-demos/tree/master/PythonPlugin) show how to write custom Suite algorithms and integrate Python-based processing into ImFusion workflows:

- `python_algorithm_demo.py` shows how you can write your own algorithm in Python and run it from the ImFusion Suite.
- `python_algorithm_monai_filter.py` demonstrates how third-party Python libraries can be integrated into ImFusion Suite workflows, using MONAI as an example.
- `python_operation_demo.py` demonstrates how to implement a Python-based ML operation that can be used as a reusable processing step in ImFusion data pipelines.

## Further Information

You can find more details about our Python integrations in our [documentation](https://docs.imfusion.com/python/index.html).
For product information and company news, visit the [ImFusion website](https://www.imfusion.com/).

## Acknowledgements

Some tutorials use shared demo data stored in `shared/data/`. The data is taken from:

National Cancer Institute Clinical Proteomic Tumor Analysis Consortium (CPTAC). (2019).  
The Clinical Proteomic Tumor Analysis Consortium Uterine Corpus Endometrial Carcinoma Collection (CPTAC-UCEC) (Version 12) [Data set].  
The Cancer Imaging Archive.  
https://doi.org/10.7937/K9/TCIA.2018.3R3JUISW
