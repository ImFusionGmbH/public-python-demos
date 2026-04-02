import os
blacklist = os.environ.get("IMFUSION_PLUGIN_BLACKLIST", "")
addition = "Torch;Onnx"
if blacklist:
    blacklist += ";" + addition
else:
    blacklist = addition
os.environ["IMFUSION_PLUGIN_BLACKLIST"] = blacklist
