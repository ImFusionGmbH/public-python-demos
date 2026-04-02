# Computed Tomography demos with `imfusion-sdk`

This folder contains Jupyter notebooks demonstrating core CT concepts using the `imfusion-sdk` Python package:

- 1_ct_geometry.ipynb: CT geometry and coordinate systems
- 2_ct_simulation.ipynb: Simple projection/simulation concepts
- 3_ct_reconstruction.ipynb: Basic reconstruction workflow
- 4_ct_registration.ipynb: 2D/3D registration demo
 
**Note:** The `computed_tomography` module is only available in the "Starter" and "Professional" offerings of our SDK.
Visit our [webshop](https://imfusion.com/products-overview/software-development-kit/x-ray-and-ct/) for more details.

## Setup

1. Please follow the steps described in [imfusion-sdk README](../imfusion-sdk/README.md) for the initial environment setup.

2. Install dependencies for this demo:

```bash
(demo-env) pip install -r imfusion-sdk-computed_tomography/requirements.txt
```

3. Start Jupyter in this folder:

```bash
(demo-env) cd imfusion-sdk-computed_tomography/
(demo-env) jupyter notebook
```

## Data note

The two images in `data/` (`regdemo0.png`, `regdemo1.png`) are simulated DRRs (Digitally Reconstructed Radiographs) generated from CT data for demonstration purposes.
