"""
This file contains a custom Algorithm written in Python.
To add this Algorithm to the ImFusion Suite you need to open this file in the Suite.
You can either drag and drop it into the Suite window or use the file import dialog ("Open" Button in the top bar)
To run the Algorithm you will then need to select an image in the Data widget and open the controller for this Algorithm from the right-click context menu.
It will be located under `Python` -> `My Amazing Algorithm`.
The Algorithm is registered through the `imfusion.algorithm.register` decorator.
You can find more information about writing your own Algorithms in Python at `https://docs.imfusion.com/python/algorithms.html.`
"""

import imfusion as imf
import numpy as np
from imfusion.algorithm import Input, ParamInt


@imf.algorithm.register(display_name="My Amazing Algorithm")
class MyAlgorithm:
    """Example algorithm that thresholds an image."""

    imageset = Input(imf.SharedImageSet)
    threshold = ParamInt("Threshold", default=0, min=0)

    def __call__(self) -> imf.SharedImageSet:
        imageset_out = imf.SharedImageSet()

        for imageset in self.imageset:
            arr = np.array(imageset, copy=True)
            arr = (arr - imageset.shift) / imageset.scale

            # modify the data of the SharedImage
            arr[arr < self.threshold] = 0
            arr[arr >= self.threshold] = 1

            out = imf.SharedImage(arr).astype(np.uint8)
            out.world_to_image_matrix = imageset.world_to_image_matrix
            out.spacing = imageset.spacing
            out.modality = imf.Data.Modality.LABEL

            imageset_out.add(out)

        # adjust the windowing to the new range
        dop = imageset_out.components.display_options_2d
        if not dop:
            if imageset_out[0].dimension() == 2:
                dop = imageset_out.components.add(imf.data.components.DisplayOptions2d(imageset_out))
            else:
                dop = imageset_out.components.add(imf.data.components.DisplayOptions3d(imageset_out))
        dop.window = 1.0
        dop.level = 0.5

        return imageset_out

    @imf.algorithm.action("My action")
    def my_action(self):
        print(f"{self.__class__.__name__}: Input imageset is {self.imageset}")
