"""
This file contains a custom Algorithm written in Python.
To add this Algorithm to the ImFusion Suite you need to open this file in the Suite.
You can either drag and drop it into the Suite window or use the file import dialog ("Open" Button in the top bar)
To run the Algorithm you will then need to select an image in the Data widget and open the controller for this Algorithm from the right-click context menu.
It will be located under `Python` -> `MonaiSobel`.
The Algorithm is registered through the `imfusion.algorithm.register` decorator.
You can find more information about writing your own Algorithms in Python at https://docs.imfusion.com/python/algorithms.html.
"""

from enum import Enum

import imfusion as imf
import monai
from imfusion.algorithm import Input, ParamBool, ParamChoice, ParamInt


class PaddingMode(Enum):
    ZEROS = "zeros"
    REFLECT = "reflect"
    REPLICATE = "replicate"
    CIRCULAR = "circular"


@imf.algorithm.register(display_name="MonaiSobel")
class MonaiSobel:
    """Example algorithm that applies MONAI Sobel gradients to an image."""

    image = Input(imf.SharedImageSet)
    kernel_size = ParamInt("Kernel Size", default=3, min=3, max=15, step=2, with_slider=True, unit="px")
    normalize_kernel = ParamBool("Normalize Kernel", default=True)
    padding = ParamChoice("Padding", default=PaddingMode.ZEROS)

    def __call__(self) -> imf.SharedImageSet:
        sobel = monai.transforms.SobelGradients(
            self.kernel_size,
            normalize_kernels=self.normalize_kernel,
            padding_mode=self.padding.value,
        )

        filtered = sobel(self.image[0].astype(float).torch())
        return imf.SharedImageSet.from_torch(filtered[None, ...], get_metadata_from=self.image)
