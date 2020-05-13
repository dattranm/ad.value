# ad.value
TAMU Datathon 2019 ML Project ad.value()

This project is a ML-based project built by Dat Tran, Furkan Toprak, and Romeo Rivara for the submission in Texas A&M Datathon 2019.

We trained a convolutional neural network to identify logos such as Coca-Cola, Nike, Adidas, Shell, Facebook, etc. and analyze videos for metrics such as the time a certain company's logo is shown, with what frequency it is shown, and how many advertisements are shown.

We gathered thousands of images of billboard ads and inputted them into a pre-trained YOLOv3 (You Only Look Once) machine learning model. We taught the YOLOv3 model using python libraries such as tensorflow, keras, numpy, and imageAI. imageAI is a python library that runs mostly tensorflow under the hood in order to train neural networks for object detection and prediction. We used imageAI because it makes training easier, as it uses novel sub-sampling techniques to more efficiently train for features in images.

For the full project and models, please visit our Google Drive link: https://drive.google.com/drive/folders/1iKS8TZFa_TArT_YiEYzDvsQBTOrN3r0M?usp=sharing
