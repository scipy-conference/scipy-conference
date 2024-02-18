# A Geographers journey into AI: Mapping urban trees from scratch

Contributors:

- Stefanie Lumnitz
- Mahdi Shooshtari
- Verena Griess

# Short summary

We will share our experience and lessons learned in choosing, training and
deploying deep learning models for single urban tree detection, localization
and classification using street-level imagery. Drawing on our case study of
Canada-wide urban tree mapping, we provide guidance on questions such as: what
to think about when choosing a Deep Learning framework for your computer vision
use case? How can you be creative in acquiring your training data? How do you
train an instance segmentation model with limited labeled examples? Which open
source projects to choose to quickly get started?

# Abstract

The scientific Python stack has the power to bring the benefit of new
technological developments to everyone. Geographical Information Science, for
example, can greatly benefit from open source methods and developments in
Artificial Intelligence and Computer Vision. Convolutional Neural Networks
(CNNs), which are commonly applied to analyze visual data, now allow us to
extract information on a large scale from datasets that were historically
neglected in environmental science. Street-level imagery, for instance,
requires large amounts of time and human effort to process, but detailed
spatial information can now be gleaned from such imagery thanks to CNNs. We can
for example collect information on the location and characteristics of single
urban trees, rapidly, over large scale, through analyzing street-level imagery.
This information is to date primarily collected by hand or through expensive
remote sensing sensors and is crucial for many applications in science and
industry, like bio-surveillance, urban livability and human health assessments,
storm water runoff studies and urban planning and greenspace management.
However, embarking on a journey into deep learning without a strong programming
background can be a daunting task, so far limiting the use of these
technologies by environmental scientists.

In this presentation, we will share lessons learned in choosing, training and
deploying deep learning models for single urban tree detection, localization
and classification using street-level imagery. Drawing on our case study of
Canada-wide urban tree mapping, we provide guidance on questions such as: what
to think about when choosing a Deep Learning framework for your computer vision
use case? How can you be creative in acquiring your training data? How do you
train an instance segmentation model with limited labeled examples? Which open
source projects to choose to quickly get started?

Our deployed workflow for mapping single urban trees ranges from instance
segmentation, over object detection, to classification and monocular depth
estimation. We will examine models based on Keras, TensorFlow and fastai from a
user’s perspective. We first use Mask R-CNN for instance level classification
of single urban trees in street level imagery. We demonstrate the
transferability of our trained model to different imagery sources (e.g.
Mapillary, OpenStreetCam, Google Streetview) and the use, opportunities and
limits of training with a minimum of labeled data. We then geolocate detected
trees using only one or two street level images, relying on a novel method
based on monocular depth estimation and triangulation. Finally, we will show
how a training dataset can be generated to classify the genus and species of
trees using existing street tree inventories.

By sharing our experience and lessons learned on the application of deep
learning to urban tree mapping, we aim both at guiding first-time deep learning
practitioners and sharing insights with versed CNN experts, and thus to inspire
a broad audience.

Additional Material:

- Audio Record of a presentation at the BioSAFE symposium (November 2018): - begins at 1:28:00 https://pwgsc-nh.webex.com/pwgsc-nh/ldr.php?RCID=644b4f4ea1b99101946ad3fe8a38e2fc (Please do not disseminate further)
- Umbrella Project website: http://www.biosafegenomics.com
- Project code will be shared on GitHub after paper publication
