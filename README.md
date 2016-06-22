# Image-Sorting-Script
<h2>Problem Statement</h2>
<p>I love clicking pics, and i click at lot of pics. Some times pics reaches 1k for 2 days trip. And obviously my friends aren't 
interested in those random clicks. They are more interested in group pics, selfies and single pictures of their's. So its a tedious job
for me sitting and segregating those 1000 pics and send them only what they are more interested. And its also becomes easy to search in cloud
if its segregated, i mostly upload nature pics to my instagram (https://instagram.com/SkyTreasure) so am trying to write a small python 
script to do the job for me. </p>


<h2>How to Run? </h2>
<p>I have created nel.sh shell script. Give permission chmod 777 nel.sh, before executing. Place nel.sh, facedetect.py, detect.py, haarcascade_frontalface_default.xml in the folder where you have image folder. Run ./nel.sh <Image Folder Name> in my case its ./nel.sh images. </p><br/>
<p>It creates 2 folders people and others and segregates accordingly. Accuracy is 70-80%. </p>
