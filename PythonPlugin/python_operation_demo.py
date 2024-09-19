"""
This file contains a custom machinelearning.Operation written in Python.
To add this Operation to the ImFusion Suite you need to open this file in the Suite.
You can either drag and drop it into the Suite window or use the file import dialog ("Open" Button in the top bar)
To run the Operation you will then need to select an image in the Data widget and open the OperationSequenceAlgorithm from the right-click context menu (Machine Learning -> Execute Operations).
From the combobox in the algorithm widget you can then select `PyNormalizeOperation`.
You can find more information about writing your own Operations in Python at https://docs.imfusion.com/python/ml_op_bindings.html.
"""

import imfusion
from imfusion import Properties, SharedImageSet, SharedImage
import imfusion.machinelearning as ml
import numpy as np


class PyNormalizeOperation(ml.Operation):
    """
    A dummy test operation to normalize the input image between [0;1] based on the image minimum/maximum values.
    """

    def __init__(self, verbose=False):
        super().__init__(name="PyNormalizeOperation", processing_policy=ml.Operation.EVERYTHING_BUT_LABELS)
        self.verbose = verbose

    def configure(self, properties: Properties) -> bool:
        self.verbose = properties.get("verbose", self.verbose)
        return super().configure(properties)

    def configuration(self) -> Properties:
        props = super().configuration()
        props["verbose"] = self.verbose
        return props

    def process(self, item: ml.DataItem) -> ml.DataItem:
        for name, element in item.items():

            if not isinstance(element, ml.SISBasedElement):
                continue
            if element.is_target and self.processing_policy is ml.Operation.EVERYTHING_BUT_LABELS:
                continue

            if self.verbose:
                imfusion.log_info(f"Processing field '{name}'")

            si = element.content[0]
            img = np.array(si, copy=False)

            image_norm = (img - img.min()) / (img.max() - img.min())

            out = SharedImage(image_norm)
            out.matrix = si.matrix
            out.spacing = si.spacing
            item[name] = SharedImageSet(out)
            return item
