# How To Setup "Show and Tell" for Jetson TX1

## Introduction

This is a collection of scripts and tutorials that are useful to to setup the [Jetson TX1](http://www.nvidia.com/object/embedded-systems-dev-kits-modules.html) development board from NVIDIA the first time. Furthermore it explains how to install important frameworks like [[Tensorflow|https://www.tensorflow.org/]] and [[OpenCV3|http://opencv.org/]], so the google [[im2txt|https://github.com/tensorflow/models/tree/master/im2txt]] ("show and tell") neural network ([[article|http://arxiv.org/abs/1609.06647]]) can operate on Jetson.

***Attention:*** This repository uses [[git-lfs|https://git-lfs.github.com/]] for large files. You need to install [[git-lfs|https://git-lfs.github.com/]] in order to download the large binary files.

A screen-shot from the im2txt application at this repository:

![im2txt application on jetson tx1](https://raw.githubusercontent.com/wiki/Netzeband/JetsonTX1_im2txt/Images/01_jetson_im2txt.png) 

## Index

* [[Install Jetpack on the Host PC|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/Jetpack]]
* [[Flash the Jetson TX1|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/FlashJetson]]
* [[Basic Jetson setup|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetup]]
    * [[Install Firefox on Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetupFirefox]]
    * [[Setup VNC for Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetupVNC]]
    * [[Setup git and git-lfs for Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetupGit]]
    * [[Remove Libre-Office from Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetupOffice]]
    * [[Setup a SSD drive as swap memory|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonBasicSetupSwap]]
* [[Install Tensorflow on Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonTensorflow]]
* [[Install OpenCV3 on Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonOpenCV3]]
* [[Install im2txt on Jetson|https://github.com/Netzeband/JetsonTX1_im2txt/wiki/JetsonIM2TXT]]

## Licenses

Since this is a collection of different tutorials and scripts from different sources, almost every single directory or file has it's own license. The following sources and licenses are used:
(`<reprository-root>` is the root directory of this repository)

* `<reprository-root>/post-flash-scripts/*`: [[Source|https://github.com/jetsonhacks/postFlashTX1]], [[License: MIT|https://github.com/jetsonhacks/postFlashTX1/blob/master/LICENSE]]
* `<reprository-root>/opencv3/*`: [[Source|http://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html]], [[License: BSD License|http://opencv.org/license.html]]
* `<reprository-root>/patches/`:
    * `bazel-patch.diff`: [[Source|http://www.yuthon.com/2016/12/04/Installation-of-TensorFlow-r0-11-on-TX1/]], License: unknown
    * `tensorflow-patch1.diff`: Source: my own, [[License: MIT|https://opensource.org/licenses/MIT]]
    * `tensorflow-patch2.diff`: [[Source|http://www.yuthon.com/2016/12/04/Installation-of-TensorFlow-r0-11-on-TX1/]], License: unknown
* `<reprository-root>/tensorflow-jetson/*`: [[Source|https://www.tensorflow.org/]], [[License: Apache License|https://github.com/tensorflow/models/blob/master/LICENSE]]
* `<reprository-root>/im2txt-app/im2txt/*`: [[Source|https://github.com/tensorflow/models/tree/master/im2txt]], [[License: Apache License|https://github.com/tensorflow/models/blob/master/LICENSE]]
* `<reprository-root>/im2txt-app/*.py`: Source: my own, [[License: MIT|https://opensource.org/licenses/MIT]]
* `<reprository-root>/im2txt-model/*`: [[Source|https://github.com/tensorflow/models/issues/466#issuecomment-251756098]], License: unknown
* `<reprository-root>/im2txt-images/*`: [[Source|http://mscoco.org/dataset/#overview]], [[License|http://mscoco.org/terms_of_use/]]
* `<reprository-root>/run-im2txt.sh`: Source: my own, [[License: MIT|https://opensource.org/licenses/MIT]]
