from __future__ import annotations

import warnings
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeAlias

import numpy as np
from numpy.typing import NDArray

import imfusion as imf

if TYPE_CHECKING:
    from matplotlib.colors import Colormap, Normalize

ImageArray: TypeAlias = NDArray[Any]


def unzip_folder(path_to_zip_folder: str | Path) -> Path:
    import zipfile

    zip_path = Path(path_to_zip_folder)
    if zip_path.suffix != ".zip":
        raise ValueError("Can only unzip zip files")

    path_extracted = zip_path.parent
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(path_extracted)
    return path_extracted


def _label_mappable() -> tuple[Colormap, Normalize]:
    from matplotlib import pyplot as plt
    from matplotlib.colors import BoundaryNorm, ListedColormap

    cmap = plt.get_cmap("tab10")
    colors = cmap.colors  # type: ignore[attr-defined]
    label_cmap = ListedColormap(np.vstack(([0, 0, 0], colors)))
    norm = BoundaryNorm(np.arange(label_cmap.N), ncolors=label_cmap.N)
    return label_cmap, norm


def _image_array(image: imf.SharedImage, *, bake_transformation: bool) -> ImageArray:
    if bake_transformation:
        from imfusion import machinelearning as ml
        arr = ml.BakeTransformationOperation()(imf.SharedImageSet(image))[0].numpy()
    else:
        arr = np.asarray(image)
    return arr[::-1, ...]


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
    bake_transformation: bool = False,
) -> None:
    from matplotlib import pyplot as plt
    from matplotlib.cm import ScalarMappable
    from matplotlib.colors import Normalize

    arr = _image_array(image, bake_transformation=bake_transformation)
    label_arr: ImageArray | None = None
    if labels is not None:
        label_arr = _image_array(labels, bake_transformation=bake_transformation)
        if arr.shape != label_arr.shape:
            warnings.warn("Incompatible labelmap will be ignored when plotting")
            label_arr = None

    slice_selection = tuple(
        dim if dim is not None else size // 2
        for size, dim in zip(arr.shape[:-1], [z, y, x])
    )
    mprs: list[ImageArray] = []
    label_mprs: list[ImageArray | None] = []
    for i, _ in enumerate(arr.shape[:-1]):
        mpr_selection = tuple(
            slice_selection[j] if j == i else slice(None, None, None) for j in range(3)
        )
        mprs.append(arr[mpr_selection])
        label_mprs.append(label_arr[mpr_selection] if label_arr is not None else None)

    vmin = vmin if vmin is not None else float(arr.min())
    vmax = vmax if vmax is not None else float(arr.max())
    cmap: str | Colormap = "gray"
    norm: Normalize = Normalize(vmin=vmin, vmax=vmax)
    if image.modality == imf.Data.Modality.NM:
        cmap = "inferno"
    if image.modality == imf.Data.Modality.LABEL:
        cmap, norm = _label_mappable()
    fig, plots = plt.subplots(1, 3, figsize=(12, 8))
    axes = np.atleast_1d(plots).ravel().tolist()
    fig.patch.set_alpha(0.0)
    for mpr, label_mpr, ax in zip(mprs[::-1], label_mprs[::-1], axes):
        ax.imshow(
            mpr,
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            interpolation=(
                "nearest"
                if image.modality == imf.Data.Modality.LABEL
                else "antialiased"
            ),
        )
        if label_mpr is not None:
            ax.imshow(
                label_mpr,
                cmap=_label_mappable()[0],
                interpolation="nearest",
                alpha=label_alpha,
            )
        ax.axis("off")

    plt.tight_layout()
    if image.modality != imf.Data.Modality.LABEL:
        colorbar_anchor = axes[-1]
        cbar_ax = fig.add_axes(
            (
                colorbar_anchor.get_position().x1 + 0.01,
                colorbar_anchor.get_position().y0,
                0.02,
                colorbar_anchor.get_position().height,
            )
        )
        fig.colorbar(
            ScalarMappable(norm=norm, cmap=cmap),
            cax=cbar_ax,
            orientation="vertical",
        )
    fig.patch.set_facecolor("gray")
    plt.show()
