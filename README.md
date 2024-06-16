<h3>Introduction</h3>
This app leverages YOLOv8 to detect vulnerable groups, 
such as individuals with wheelchairs, crutches, and prams, enhancing accessibility and safety at crosswalks.
<br>
<br>
<br>

**Working Mechanism** <br>
When a vulnerable group is detected, the app extends the red light and decreases the green light duration for cars , 
ensuring safer and more accessible crossings for these individuals.
<br>
<br>

<h3>Configuration</h3>
1. To incorporate cvzone alongside YOLOv8, make sure you have the requirements installed.<br>
<br>

```
pip install Pillow
pip install ultralytics
pip install cvzone
pip install opencv-python
```
<br>
If you encounter any issues where pandas or numpy are missing, you can install them separately:
<br>

```
pip install pandas
pip install numpy
```
<br>
<br>

2. Select 'Select File' for video detection or 'Live Detection' for live detection.
<br>
<img width="999" alt="Screenshot 2024-06-16 at 5 46 41 PM" src="https://github.com/Omskka/Wheelchair_detection/assets/92455486/5ffc1a0e-3297-4536-8a9f-0eef7d5905d8">

<p align="center">Only mp4, avi, mov, mkv formats are supported!</p>



<br>
<br>
<br>
<br>
   
4. Click on 'Zone Configuration' to set the zone area's coordinates for the video. <br>If you choose not to configure any values, the default settings will be used.<br>
    Additionally, utilize the toggle button to enable or disable traffic light visualization. 
<br>
<img width="999" alt="Screenshot 2024-06-16 at 5 46 55 PM" src="https://github.com/Omskka/Wheelchair_detection/assets/92455486/9f9eb4ac-3530-45bc-94f5-a652c2b90633">

<br>
<br>

<h3>Try It Yourself: Executable and Example Videos</h3>

<br>
<br>

<img width="1275" alt="Screenshot 2024-06-16 at 6 25 13 PM" src="https://github.com/Omskka/Wheelchair_detection/assets/92455486/49ff1672-c7b1-4531-990c-e368a0c28354">






