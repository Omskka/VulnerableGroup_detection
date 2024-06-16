<h3>Introduction</h3>
This app leverages YOLOv8 to detect vulnerable groups, 
such as individuals with wheelchairs, crutches, and prams, enhancing accessibility and safety at crosswalks.
<br>

**Working Mechanism** 
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
<img width="999" alt="Screenshot 2024-06-16 at 5 46 41 PM" src="https://github.com/Omskka/Wheelchair_detection/assets/92455486/5ffc1a0e-3297-4536-8a9f-0eef7d5905d8">


   

4. Click on 'zone configuration' to set the zone area's coordinates for the video. If you choose not to configure any values, the default values will be used.

<br>
<br>

<h3>Usage</h3>

Once you've set the zone values (defaults will be used if not configured), enter the video's name with the .mp4 extension into the textbox, then click 'generate'.<br><br>
**Warning** <br>
**ONLY .MP4 EXTENSION IS SUPPORTED**

<div style="display: flex;">
  <img src="https://i.imgur.com/js95pmy_d.jpg?maxwidth=520&shape=thumb&fidelity=high" alt="Page UI 1" width="360" height="225">
  <img src="https://i.imgur.com/aYwts8J_d.jpg?maxwidth=520&shape=thumb&fidelity=high" alt="Page UI 2" width="360" height="225">
</div>
