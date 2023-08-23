# Adaptation of the Official YOLOv7 repository for field hockey in the netherlands

so far only able to use 2 models on shorts .mp4 clips of hockeymatches
in the process of mapping images to 2d coordinates for vizualization 

# instructions

create virtual env in python and activate
pip install -r requirements.txt
python detect.py --weights yolov7-tiny.pt --conf 0.25 --img-size 640 --source <file_location_of_sports_video> --view-img 



# Todo 
add GIT LFS or other filesystem to facilitate testing code by running on pulic field hockey games
start on projection matrices to map coordinates to coordinates for vizualization
retrain model on more public high resolution field hockey games to increase confidence
investigate whether it is possible to train on recognizing field hockey bal
