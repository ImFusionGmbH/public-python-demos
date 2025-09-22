"""
This file contains a custom Algorithm written in Python.
To add this Algorithm to the ImFusion Suite you need to open this file in the Suite.
You can either drag and drop it into the Suite window or use the file import dialog ("Open" Button in the top bar)
To run the Algorithm you will then need to select an image in the Data widget and open the controller for this Algorithm from the right-click context menu.
It will be located under `Python` -> `MonaiSobel`.
You can find more information about writing your own Algorithms in Python at https://docs.imfusion.com/python/algorithms.html.
"""

from pathlib import Path

import imfusion as imf
import numpy as np
import monai


class MonaiSobel(imf.Algorithm):
    """Example algorithm that thresholds an image."""

    def __init__(self, imageset: imf.SharedImageSet):
        super().__init__()
        self.imageset = imageset
        self.imageset_out = imf.SharedImageSet()
        self.padding_options = imf.Properties.EnumStringParam(
            value="zeros",
            admitted_values={"zeros", "reflect", "replicate", "circular"},
        )

        # We can add parameters to the algorithm that auto-generate GUI elements in the Suite
        # The GUI element created depends on the type of the value we pass in
        self.add_param('kernel_size', 3,
                       attributes='min: 1, max: 15, withSlider: True, suffix: px'
        )
        self.add_param("normalize_kernel", True)
        self.add_param("padding", self.padding_options)

    @classmethod
    def convert_input(cls, data: imf.DataList) -> imf.DataList:
        if len(data) != 1:
            raise imf.IncompatibleError("Requires one dataset")
        images = [i for i in data if isinstance(i, imf.SharedImageSet)]
        if len(images) != 1:
            raise imf.IncompatibleError("Only works on images")
        return images

    def compute(self) -> None:

        sobel = monai.transforms.SobelGradients(
            self.kernel_size,
            normalize_kernels=self.normalize_kernel,
            padding_mode=self.padding.value,
        )

        filtered = sobel(self.imageset[0].astype(float).torch())
        self.imageset_out = imf.SharedImageSet.from_torch(filtered[None, ...], get_metadata_from=self.imageset)

    def output(self):
        return [self.imageset_out]


# The Algorithm needs to be manually registered in the Suite
imf.unregister_algorithm('Python;MonaiSobel')  # Remove potential previous versions of this algo
imf.register_algorithm("Python.MonaiSobel", 'Python;MonaiSobel', MyAlgorithm)
