# Computed Tomography Demos with `imfusion-sdk-computed_tomography`

This folder contains Jupyter notebooks demonstrating core CT concepts using the `imfusion-sdk-computed_tomography` Python package:

- 1_ct_geometry.ipynb: CT geometry and coordinate systems
- 2_ct_simulation.ipynb: Simple projection/simulation concepts
- 3_ct_reconstruction.ipynb: Basic reconstruction workflow
- 4_ct_registration.ipynb: 2D/3D registration demo

**Note:** The `imfusion-sdk-computed_tomography` package is available in the "Starter" and "Professional" SDK offerings.
Visit our [SDK pricing page](https://imfusion.com/sdk-pricing/) for more details.

## Setup

1. Please follow the steps described in [imfusion-sdk/README.md](../imfusion-sdk/README.md) for the initial environment setup.

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
