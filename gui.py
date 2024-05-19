from imports import *

# Define base directory
BASE_DIR = Path(__file__).resolve().parent


# Define paths
ASSETS_PATH = BASE_DIR / "assets"/"frame0"  # assets directory path
VIDEO_DIRECTORY = BASE_DIR /"videos"  # 'videos' directory path
MODEL_PATH = BASE_DIR / "best.pt"  # YOLOv8 model path
CLASSES_PATH = BASE_DIR / "classes.txt" # 'classes' file path


def relative_to_assets(path: str) -> Path:
    return BASE_DIR /"assets"/"frame0"/path


# Function to store video path
def store_video_path():
    global video_path
    video_path = VIDEO_DIRECTORY / entry_1.get()
    train_model_and_play(video_path)


# Default coordinates for zoning(Area1)
reset_counter = 0 # count the number of resets
def reset_entries():
    global reset_counter, X1, Y1, X2, Y2, X3, Y3, X4, Y4
    X1 = 400 #24
    Y1 = 140
    X2 = 24
    Y2 = 477
    X3 = 950 #900
    Y3 = 477
    X4 = 650 #900
    Y4 = 140
    reset_counter +=1
    # Show info messsage when reset button is pressed(counter > 1)
    if reset_counter > 1:
        messagebox.showinfo("info", "The entry values have been reverted to their default settings.")


# Initialise default values at program startup
reset_entries()


# Create window
window = Tk()
window.geometry("1000x600")
window.configure(bg = "#F5F4F4")

canvas = Canvas(
    window,
    bg = "#F5F4F4",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    600.0,
    fill="#387EF5",
    outline="")

canvas.create_text(
    39.0,
    128.0,
    anchor="nw",
    text="Wheelchair Detection",
    fill="#F5F4F4",
    font=("Inter Bold", 36 * -1)
)

canvas.create_rectangle(
    57.0,
    184.0,
    157.0,
    197.0,
    fill="#F5F4F4",
    outline="")

canvas.create_text(
    40.0,
    230.0,
    anchor="nw",
    text="Discover a groundbreaking solution for\n enhanced accessibility through our app,\n harnessing the cutting-edge YOLOV\n technology.\n\n By accurately detecting pedestrians,\n including wheelchair users, it redefines\n safety and inclusivity, revolutionizing\n navigation experiences for all.",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    625.0,
    114.0,
    anchor="nw",
    text="Enter The Details",
    fill="#625F80",
    font=("Inter ExtraBold", 32 * -1)
)

canvas.create_text(
    623.0,
    182.0,
    anchor="nw",
    text="Transform Any Video By Simply\nEntering The Name Of Your Video.",
    fill="#625F80",
    font=("Inter", 16 * -1)
)

# Button_1
button_image_1 = PhotoImage(
    file=relative_to_assets("button_2.png")) # Change "button_1.png" to "button_2.png" for a rectangle button

# Update the button command to call play_video function
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=store_video_path,  # Call store_video_path function when button is clicked
    relief="flat",
    text="Generate",
    compound="center",
    fg="#FFFFFF",
    font=("Inter Bold", 12)
)

button_1.place(
    x=677.0,
    y=395.0,
    width=144.0,
    height=55.0
)

# Textbox
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

entry_bg_1 = canvas.create_image(
    756.0,
    316.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#808080",
    highlightthickness=0
)
entry_1.place(
    x=593.0,
    y=292.0,
    width=326.0,
    height=47.0
)

# Insert default text into the Entry widget
default_text = "Ex. video.mp4"
entry_1.insert(0, default_text)


# Function to remove default text when Entry widget is clicked
def on_entry_click(event):
    if entry_1.get() == default_text:
        entry_1.delete(0, "end")


# Function to open the hyperlink in a web browser
def open_link(event):
    webbrowser.open("https://github.com/Omskka/Wheelchair_detection/blob/main/README.md")


# Create a label for the hyperlink
info_label = Label(
    window,
    text="Click here for instructions",
    fg="white",  # Set text color to blue
    bg="#387EF5",  # Set background color to the same as the blue background
    cursor="hand2",  # Change cursor to a hand when hovering over the label
    font=("Inter", 12, "underline")  # Set font and underline the text
)
info_label.place(x=25, y=560)

# Bind <Button-1> event to open_link function
info_label.bind("<Button-1>", open_link)

# Bind <FocusIn> event to Entry widget
entry_1.bind("<FocusIn>", on_entry_click)

# Create a label for the hyperlink
info_label = Label(
    window,
    text="For zone configuration, click here",
    fg="white",  # Set text color to blue
    bg="#387EF5",  # Set background color to the same as the blue background
    cursor="hand2",  # Change cursor to a hand when hovering over the label
    font=("Inter", 12, "underline")  # Set font and underline the text
)
info_label.place(x=38, y=460)


# Function to go back from config to main window
def go_back():
    # Destroy the conf_window
    conf_window.destroy()

    # Restore the window
    window.deiconify()


def validate_entries():
    global X1, Y1, X2, Y2, X3, Y3, X4, Y4

    # Get values from Entry widgets and convert them to integers
    try:
        X1 = int(entry1.get())
        Y1 = int(entry2.get())
        X2 = int(entry3.get())
        Y2 = int(entry4.get())
        X3 = int(entry5.get())
        Y3 = int(entry6.get())
        X4 = int(entry7.get())
        Y4 = int(entry8.get())
    except ValueError:
        # If conversion fails, show an error message and return
        messagebox.showwarning("Warning", "Please enter numerical values only.")
        return

    # If all entries are numerical, destroy the conf_window
    conf_window.destroy()
    # Restore the window after video ends
    window.deiconify()

def config_window(event):
    # Minimize the window
    window.iconify()

    # Create window
    global conf_window
    conf_window= Tk()
    conf_window.geometry("1000x600")
    conf_window.configure(bg = "#F5F4F4")

    canvas2 = Canvas(
        conf_window,
        bg = "#F5F4F4",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas2.place(x = 0, y = 0)
    canvas2.create_rectangle(
        0.0,
        0.0,
        500.0,
        600.0,
        fill="#387EF5",
        outline=""
    )

    canvas2.create_text(
        625.0,
        114.0,
        anchor="nw",
        text="Enter The Details",
        fill="#625F80",
        font=("Inter ExtraBold", 32 * -1)
    )

    canvas2.create_text(
        635.0,
        182.0,
        anchor="nw",
        text="Please input the coordinates\ncorresponding to the area you\nwant to outline on the video.",
        fill="#625F80",
        font=("Inter", 16 * -1)
    )

    # Done button
    done_button = Button(
        conf_window,
        text="Done",
        command = validate_entries,
        bg="#F5F4F4",  # Set background color
        width=15,      # Set width (in characters)
        height=2       # Set height (in lines)
    )
    done_button.place(x=650, y=300)

    # Back button
    back_button = Button(
        conf_window,
        text="Back",
        command=go_back,
        bg="#F5F4F4",  # Set background color
        width=15,      # Set width (in characters)
        height=2       # Set height (in lines)
    )
    back_button.place(x=650, y=360)

    # Reset button
    back_button = Button(
        conf_window,
        text="Reset",
        command=reset_entries,
        bg="#F5F4F4",  # Set background color
        width=15,      # Set width (in characters)
        height=2       # Set height (in lines)
    )
    back_button.place(x=210, y=525)

    # Labels
    label_x = 80
    label_y = 40
    label_spacing = 60
    Label(conf_window, text="X1", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="Y1", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="X2", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="Y2", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="X3", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="Y3", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="X4", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)
    label_y += label_spacing
    Label(conf_window, text="Y4", bg="#387EF5", fg="#FFFFFF", font=("Inter", 16, "bold")).place(x=label_x, y=label_y)

    #Entries
    entry_x = 200
    entry_y = 40
    spacing = 60

    global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8

    entry1 = Entry(conf_window)
    entry1.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry2 = Entry(conf_window)
    entry2.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry3 = Entry(conf_window)
    entry3.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry4 = Entry(conf_window)
    entry4.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry5 = Entry(conf_window)
    entry5.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry6 = Entry(conf_window)
    entry6.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry7 = Entry(conf_window)
    entry7.place(x = entry_x, y = entry_y)
    entry_y += spacing
    entry8 = Entry(conf_window)
    entry8.place(x = entry_x, y = entry_y)

    # Calculate the center coordinates of the screen
    screen_width = conf_window.winfo_screenwidth()
    screen_height = conf_window.winfo_screenheight()
    x_coordinate = (screen_width - 1000) // 2
    y_coordinate = (screen_height - 600) // 2

    # Set the window geometry to center it on the screen
    conf_window.geometry(f"1000x600+{x_coordinate}+{y_coordinate}")

    conf_window.resizable(False, False)
    conf_window.mainloop()

# Bind <Button-1> event to open_link function
info_label.bind("<Button-1>", config_window)

def train_model_and_play(video_path):
    model=YOLO(MODEL_PATH)

    def RGB(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :
            point = [x, y]
            #print(point)

    #cv2.namedWindow('RGB')
    #cv2.setMouseCallback('RGB', RGB)
    cap=cv2.VideoCapture(str(video_path))
    if not cap.isOpened():  # Check if the video file opened successfully
        # Print warning message
        messagebox.showerror("error", "Error: Could not open video file.\nPlease make sure the video is in the 'videos' directory.")
        return 

    my_file = open(CLASSES_PATH, "r")
    data = my_file.read()
    class_list = data.split("\n")
    #print(class_list)

    tracker = Tracker()
    area1=[(X1,Y1),(X2,Y2),(X3,Y3),(X4,Y4)] # Zone coordinates
    area2=[(548,290),(600,496),(637,493),(574,288)]

    paused = False

    # Minimize the window
    window.iconify()

    # Initialize the list to store IDs of detectables in the zone
    # PS: Current model doesn't detect prams and crutches
    wheelchairs_in_zone = []
    prams_in_zone = [] 
    crutches_in_zone = []

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame,(1020,500))

            results = model.predict(frame)
            a = results[0].boxes.data
            px = pd.DataFrame(a).astype("float")

            list = []
            for index,row in px.iterrows():
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                d = int(row[5])

                c = class_list[d]
                if 'Wheel-chairs' in c:
                    list.append([x1, y1, x2, y2])
            bbox_idx = tracker.update(list)
            wheelchairs_in_zone = []  # Clear the list before updating
            for bbox in bbox_idx:
                x3, y3, x4, y4, id = bbox
                result = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)
                
                # Convert confidence scores to Python floats with limited precision (3 decimal places)
                confidence_scores = [f"{score:.3f}" for score in results[0].boxes.conf.cpu().numpy()]

                # Green Light, Red Light
                #print(result)
                '''if result >= 0:
                    print("-----RED-----")
                else:
                    print("-----GREEN-----") '''
                
                # Draw rectangle when wheelchair is detected within the zone
                if result >= 0:
                    # Append the ID of the wheelchair detected in the zone to the list
                    wheelchairs_in_zone.append(id)
                    #cv2.circle(frame,(x4, y4), 5, (0, 0, 255), -1)
                    cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 255, 255), 2)

                    # Iterate over confidence scores and display each one
                    for confidence_score in confidence_scores:
                        # Use cvzone.putTextRect to draw the text on the frame
                        cvzone.putTextRect(frame, confidence_score, (x3, y3), 1, 1)

            cv2.polylines(frame, [np.array(area1,np.int32)], True, (0, 255, 0), 2)

            #Resize the frame to the desired size (600x1000)
            frame = cv2.resize(frame, (1000, 600))

            # Create a blank image for displaying wheelchair count
            count_image = np.zeros((600, 200, 3), dtype=np.uint8)
            count_image[:] = (245, 126, 56)  # Set background color (BRG) 
            # Wheelchairs
            cv2.putText(count_image, f"Wheelchairs : {len(wheelchairs_in_zone)}", (13, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            # Crutches
            cv2.putText(count_image, f"Crutches : {len(crutches_in_zone)}", (13, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            # Prams
            cv2.putText(count_image, f"Prams : {len(prams_in_zone)}", (13, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Concatenate the frame and count image horizontally
            display_frame = np.hstack((count_image, frame))

            cv2.imshow('Video Player', display_frame)  # Display the frame

            # Get the width and height of the resized frame
            frame_height, frame_width, _ = display_frame.shape

            # Calculate the position to center the window
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x_coordinate = int((screen_width - frame_width) / 2)
            y_coordinate = int((screen_height - frame_height) / 2)

            # Move the OpenCV window to the center of the screen
            cv2.moveWindow('Video Player', x_coordinate, y_coordinate)

        key = cv2.waitKey(1)
        if key == ord('q') or not ret:  # Quit if 'q' is pressed
            break
        elif key == ord(' '):  # Pause if spacebar is pressed
            paused = not paused

    cap.release()
    cv2.destroyAllWindows()
    window.deiconify()

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 1000) // 2
y_coordinate = (screen_height - 600) // 2

# Set the window geometry to center it on the screen
window.geometry(f"1000x600+{x_coordinate}+{y_coordinate}")

window.resizable(False, False)
window.mainloop()