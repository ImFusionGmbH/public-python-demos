import warnings
import zipfile
from pathlib import Path

import imfusion as imf
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from typing import Tuple

def unzip_folder(path_to_zip_folder: str):
    # if not path_to_zip_folder.endswith('.zip'):
    #     raise ValueError('Can only unzip zip folders')
    path_extracted = Path(path_to_zip_folder).parent
    with zipfile.ZipFile(path_to_zip_folder, 'r') as zip_ref:
        zip_ref.extractall(path_extracted)
    return path_extracted


def _label_mappable():
    cmap = matplotlib.colormaps["tab10"]
    cmap = matplotlib.colors.ListedColormap(np.vstack(([0, 0, 0], cmap.colors)))
    norm = matplotlib.colors.BoundaryNorm(np.arange(cmap.N), ncolors=cmap.N)
    return cmap, norm


def mpr_plot(
        image: imf.SharedImage,
        *,
        labels: imf.SharedImage | None = None,
        x: int | None = None,
        y: int | None = None,
        z: int | None = None,
        label_alpha: float = 0.3,
        vmin: float | None = None,
        vmax: float | None = None,
):
    got_label = labels is not None
    arr = imf.machinelearning.BakeTransformationOperation()(imf.SharedImageSet(image))[0].numpy()[::-1, ...]
    if got_label:
        labels = imf.machinelearning.BakeTransformationOperation()(imf.SharedImageSet(labels))[0].numpy()[::-1, ...]
        if not arr.shape == labels.shape:
            warnings.warn("Incompatible labelmap will be ignored when plotting")
            labels = None

    slice_selection = tuple(dim if dim is not None else size // 2 for size, dim in zip(arr.shape[:-1], [z, y, x]))
    mprs = [None] * 3
    label_mprs = [None] * 3
    for i, size in enumerate(arr.shape[:-1]):
        mpr_selection = tuple(slice_selection[j] if j == i else slice(None, None, None) for j in range(3))
        mprs[i] = arr[*mpr_selection]
        if got_label:
            label_mprs[i] = labels[*mpr_selection]

    vmin = vmin if vmin is not None else image.min()[0]
    vmax = vmax if vmax is not None else image.max()[0]
    cmap = "gray"
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    if image.modality == imf.Data.Modality.NM:
        cmap = "magma"
    if image.modality == imf.Data.Modality.LABEL:
        cmap, norm = _label_mappable()
    fig, plots = plt.subplots(1, 3, figsize=(12, 8))
    for mpr, label_mpr, ax in zip(mprs[::-1], label_mprs[::-1], plots):
        ax.imshow(mpr, cmap=cmap, vmin=vmin, vmax=vmax,
                  interpolation="nearest" if image.modality == imf.Data.Modality.LABEL else "antialiased")
        if label_mpr is not None:
            ax.imshow(label_mpr, cmap=_label_mappable()[0], interpolation="nearest", alpha=label_alpha)
        ax.axis("off")

    plt.tight_layout()
    if image.modality != imf.Data.Modality.LABEL:
        cbar_ax = fig.add_axes([
            ax.get_position().x1 + 0.01,
            ax.get_position().y0, 0.02,
            ax.get_position().height
        ])
        fig.colorbar(matplotlib.cm.ScalarMappable(norm, cmap), cax=cbar_ax, orientation='vertical')
    fig.patch.set_facecolor('gray')
    plt.show()


def display_images(*images: Tuple[imf.SharedImage, ...], figsize=(10, 3), vmin=0, vmax=5):
    num_images = len(images)
    fig, axes = plt.subplots(1, num_images, figsize=figsize)   
    if num_images == 1:
        axes = [axes]

    for i, image in enumerate(images):
        image_arr = np.array(image).squeeze()
        axes[i].imshow(image_arr, vmin=vmin, vmax=vmax, cmap='gray')
        if num_images == 2:
            axes[i].set_title("Input Image" if i != num_images - 1 else "Output Image")
        else:
            axes[i].set_title(f"Input Image #{i + 1}" if i != num_images - 1 else "Output Image") 
        axes[i].axis('off')
    
    fig.colorbar(axes[-1].images[0], ax=axes, orientation='vertical', pad=0.1)
    plt.show()
    