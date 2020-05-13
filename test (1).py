from imageai.Detection.Custom import CustomVideoObjectDetection
import os
from matplotlib import pyplot as plt


execution_path = os.getcwd()
color_index = {'coke': 'red'}
resized = False

def forFrame(frame_number, output_array, output_count, returned_frame):

    plt.clf()

    this_colors = []
    labels = []
    sizes = []

    counter = 0

    for eachItem in output_count:
        counter += 1
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        sizes.append(output_count[eachItem])
        this_colors.append(color_index[eachItem])

    global resized

    if (resized == False):
        manager = plt.get_current_fig_manager()
        manager.resize(width=1000, height=500)
        resized = True

    plt.subplot(1, 2, 1)
    plt.title("Frame : " + str(frame_number))
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")

    plt.subplot(1, 2, 2)
    plt.title("Analysis: " + str(frame_number))
    plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")

    plt.pause(0.01)


video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("./models/detection_model-ex-010--loss-0005.362.h5")
video_detector.setJsonPath("detection_config.json")
video_detector.loadModel()

plt.show()

ret = video_detector.detectObjectsFromVideo(input_file_path="benchmark.mp4",
                                          output_file_path=os.path.join(execution_path, "weirdtest"),
                                          frames_per_second=20,
                                          minimum_percentage_probability=10,
                                          log_progress=True, per_frame_function=forFrame,
                                            return_detected_frame=True)
print(ret)