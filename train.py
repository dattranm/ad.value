# import os
# img = os.listdir("validation/images")
# for i in range(len(img)):
#     img[i] = img[i].split(".")[0] + ".xml"
#
# ann = os.listdir("validation/annotations")
# for i in img:
#     if i not in ann:
#         print(i.split(".")[0] + ".jpg")
#         os.remove(i.split(".")[0] + ".jpg")

from imageai.Detection.Custom import DetectionModelTrainer
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory=".")
trainer.setTrainConfig(object_names_array=["coke"],  num_experiments=20, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()
