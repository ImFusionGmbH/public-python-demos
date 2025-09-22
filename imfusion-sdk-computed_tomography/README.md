# Computed Tomography demos with `imfusion-sdk`

This folder contains Jupyter notebooks demonstrating core CT concepts using the `imfusion-sdk` Python package:

- 1_ct_geometry.ipynb: CT geometry and coordinate systems
- 2_ct_simulation.ipynb: Simple projection/simulation concepts
- 3_ct_reconstruction.ipynb: Basic reconstruction workflow
- 4_ct_registration.ipynb: 2D/3D registration demo
 
**Note:** The `vision` module is only available in the "Professional" offering of our SDK. 

## Setup

See the main [imfusion-sdk README](../imfusion-sdk/README.md) for full environment setup details.

1. Create and activate a Python virtual environment (Python 3.11 recommended):

```bash
python3 -m venv demo-env
# Windows
demo-env\Scripts\activate.bat
# macOS / Linux
source demo-env/bin/activate
```

2. Install dependencies (reusing the repo's requirements):

```bash
(demo-env) pip install -r imfusion-sdk/requirements.txt
```

3. Activate `imfusion-sdk` with your license key:

- macOS / Linux
```bash
(demo-env) IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX python -c "import imfusion"
```

- Windows
```bash
(demo-env) set IMFUSION_LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
(demo-env) python -c "import imfusion"
```

4. Start Jupyter in this folder:

```bash
(demo-env) cd imfusion-sdk-computed_tomography/
(demo-env) jupyter notebook
```

## Data note

The two images in `data/` (`regdemo0.png`, `regdemo1.png`) are simulated DRRs (Digitally Reconstructed Radiographs) generated from CT data for demonstration purposes.
