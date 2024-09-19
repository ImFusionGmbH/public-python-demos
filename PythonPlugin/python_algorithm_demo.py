"""
This file contains a custom Algorithm written in Python.
To add this Algorithm to the ImFusion Suite you need to open this file in the Suite.
You can either drag and drop it into the Suite window or use the file import dialog ("Open" Button in the top bar)
To run the Algorithm you will then need to select an image in the Data widget and open the controller for this Algorithm from the right-click context menu.
It will be located under `Python` -> `My Amazing Algorithm`.
You can find more information about writing your own Algorithms in Python at https://docs.imfusion.com/python/algorithms.html.
"""

from pathlib import Path

import imfusion as imf
import numpy as np


class MyAlgorithm(imf.Algorithm):
    """Example algorithm that thresholds an image."""
    def __init__(self, imageset: imf.SharedImageSet):
        super().__init__()
        self.imageset = imageset
        self.imageset_out = imf.SharedImageSet()

        # We can add parameters to the algorithm that auto-generate GUI elements in the Suite
        # The GUI element created depends on the type of the value we pass in
        self.add_param('threshold', 0, attributes='min: 0')
        self.add_param("save_output", False)
        self.add_param("path", Path(""))

    @classmethod
    def convert_input(cls, data: imf.DataList) -> imf.DataList:
        if len(data) != 1:
            raise imf.IncompatibleError("Requires one dataset")
        images = [i for i in data if isinstance(i, imf.SharedImageSet)]
        if len(images) != 1:
            raise imf.IncompatibleError("Only works on images")
        return images

    def compute(self) -> None:

        # clear previous results
        self.imageset_out.clear()

        for image in self.imageset:
            arr = np.array(image, copy=False)
            arr = (arr - image.shift) / image.scale

            # modify the data of the SharedImage
            arr[arr < self.threshold] = 0
            arr[arr >= self.threshold] = 1

            out = imf.SharedImage(arr).astype(np.uint8)
            out.matrix = image.matrix
            out.spacing = image.spacing
            out.modality = imf.Data.Modality.LABEL

            self.imageset_out.add(out)

        # adjust the windowing to the new range
        dop = self.imageset_out.components.display_options_2d
        if not dop:
            if self.imageset_out[0].dimension() == 2:
                dop = self.imageset_out.components.add(imf.DisplayOptions2d(self.imageset_out))
            else:
                dop = self.imageset_out.components.add(imf.DisplayOptions3d(self.imageset_out))
        dop.window = 1.0
        dop.level = 0.5

    def output(self):
        return [self.imageset_out]

# The Algorithm needs to be manually registered in the Suite
imf.unregister_algorithm('Python;My amazing algorithm')  # Remove potential previous versions of this algo
imf.register_algorithm("Python.MyAmazingAlgorithm", 'Python;My amazing algorithm', MyAlgorithm)
