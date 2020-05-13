# ad.value
TAMU Datathon 2019 ML Project ad.value()
Inspiration
Our team member, Romeo, really likes Formula1 Racing. Race cars in F1 are covered in logos of companies. F1 recently released their pricing for advertisements and we thought it would be cool if companies were able to pay for advertisements based on the actual screen time their ads got.

What it does
We trained a convolutional neural network to identify logos such as Coca-Cola, Nike, Adidas, Shell, Facebook, etc. and analyze videos for metrics such as the time a certain company's logo is shown, with what frequency it is shown, and how many advertisements are shown.

How I built it
We gathered thousands of images of billboard ads and inputted them into a pre-trained YOLOv3 (You Only Look Once) machine learning model. We taught the YOLOv3 model using python libraries such as tensorflow, keras, numpy, and imageAI. imageAI is a python library that runs mostly tensorflow under the hood in order to train neural networks for object detection and prediction. We used imageAI because it makes training easier, as it uses novel sub-sampling techniques to more efficiently train for features in images.

Challenges I ran into
We had three main challenges:

imageAI is an outdated library that doesn't yet support TensorFlow 2.0. Because of this, we had to go under imageAI's hood and fix some compatibility issues. This took us a while.
Gathering large amounts of non-redundant data from webscraping was difficult. As you can imagine, top Google image-search results are often redundant.
The final constraint was the hardest: We were limited to training a complex convolutional neural network overnight on a laptop. Because of this, we were only able to train the network 5% of what it should have been trained at (200 epochs was recommended, and we were able to train to 10 epochs). Because of this, we were only able to train our model on Coca-Cola and weren't able to use the thousands of images we scraped, cleaned, and annotated. However, even training for 10 epochs took us 4 hours!
Accomplishments that I'm proud of:
We're proud that we were able to create our first image analyzing CNN within hours and understood how it work. We're proud that we were able to fix legacy code instead of scrapping the project all together. Lastly, we're proud of the teamwork that we demonstrated. We definitely made some good friendships and were able to collaborate to execute a complex task efficiently.

What I learned
We learned the importance of good data in training ML models, and how long it takes to gather data.

What's next for ad.value()
We want to figure out how to distribute the earnings from advertisements among TV networks, stadium owners, and athletes. It's a tricky problem! After all, what is fair?
