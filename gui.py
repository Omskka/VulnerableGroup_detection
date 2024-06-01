from imports import *

# Define base directory
BASE_DIR = Path(__file__).resolve().parent

# Define paths
ASSETS_PATH = BASE_DIR / "assets" / "frame0"  # assets directory path
MODEL_PATH = BASE_DIR / "best.pt"  # YOLOv8 model path
CLASSES_PATH = BASE_DIR / "classes.txt"  # 'classes' file path


def relative_to_assets(path: str) -> Path:
    return BASE_DIR / "assets" / "frame0" / path


def select_video_file():
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return file_path

def store_video_path():
    global video_path
    video_path = select_video_file()
    if not video_path:
        messagebox.showerror("Error", "No video file selected.")
        return

    train_model_and_play(video_path)

def store_live_video_path():
    global video_path
    video_path = "live"
    train_model_and_play(video_path)


# count the number of resets
reset_counter = 0


def reset_entries():
    global reset_counter, X1, Y1, X2, Y2, X3, Y3, X4, Y4
    # Default coordinates for zoning(Area1)
    X1 = 0  # 400
    Y1 = 0  # 140
    X2 = 0  # 24
    Y2 = 600  # 477
    X3 = 1500  # 950
    Y3 = 600  # 477
    X4 = 1500  # 650
    Y4 = 0  # 140
    reset_counter += 1
    # Show info messsage when reset button is pressed(counter > 1)
    if reset_counter > 1:
        messagebox.showinfo("info", "The entry values have been reverted to their default settings.")


# Initialise default values at program startup
reset_entries()

# Create window
window = Tk()
window.title("Vulnerable Group Detection App")
window.geometry("1000x600")
window.configure(bg="#F5F4F4")

# set default toggle to 'off'
toggle_state = False

canvas = Canvas(
    window,
    bg="#F5F4F4",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
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
    text="Vulnerable Group Detection",
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
    text="Discover a groundbreaking solution for\n enhanced accessibility through our app,\n harnessing the "
         "cutting-edge YOLOV\n technology.\n\n By accurately detecting pedestrians,\n including wheelchair users, "
         "it redefines\n safety and inclusivity, revolutionizing\n navigation experiences for all.",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    625.0,
    180.0,
    anchor="nw",
    text="Enter The Details",
    fill="#625F80",
    font=("Inter ExtraBold", 32 * -1)
)

canvas.create_text(
    623.0,
    245.0,
    anchor="nw",
    text="Transform Any Video By Simply\n"
    "         Selecting a Video File",
    fill="#625F80",
    font=("Inter", 16 * -1)
)

# Button for file selection
button_image_1 = PhotoImage(
    # Change "button_1.png" to "button_2.png" for a rectangle button
    file=relative_to_assets("button_2.png"))

# Update the button command to call play_video function
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=store_video_path,  # Call store_video_path function when button is clicked
    relief="flat",
    text="Select File",
    compound="center",
    fg="#FFFFFF",
    font=("Inter Bold", 12)
)

button_1.place(
    x=665.0,
    y=325.0,
    width=144.0,
    height=55.0
)

# Button for live detection
button_image_2 = PhotoImage(
    # Change "button_1.png" to "button_2.png" for a rectangle button
    file=relative_to_assets("button_2.png"))

# Update the button command to call play_video function
button_2 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=store_live_video_path,  # Call store_video_path function when button is clicked
    relief="flat",
    text="Live Detection",
    compound="center",
    fg="#FFFFFF",
    font=("Inter Bold", 12)
)

button_2.place(
    x=665.0,
    y=400.0,
    width=144.0,
    height=55.0
)


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


# Create a label for the hyperlink
info_label = Label(
    window,
    text="For configuration, click here",
    fg="white",  # Set text color to blue
    bg="#387EF5",  # Set background color to the same as the blue background
    cursor="hand2",  # Change cursor to a hand when hovering over the label
    font=("Inter", 12, "underline")  # Set font and underline the text
)
info_label.place(x=38, y=460)


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
    global conf_window, entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, toggle_state, toggle_var
    conf_window = Toplevel(window)
    conf_window.geometry("1000x600")
    conf_window.configure(bg="#F5F4F4")

    canvas2 = Canvas(
        conf_window,
        bg="#F5F4F4",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas2.place(x=0, y=0)
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
        command=validate_entries,
        bg="#F5F4F4",  # Set background color
        width=15,  # Set width (in characters)
        height=2  # Set height (in lines)
    )
    done_button.place(x=660, y=300)

    # Back button
    back_button = Button(
        conf_window,
        text="Back",
        command=go_back,
        bg="#F5F4F4",  # Set background color
        width=15,  # Set width (in characters)
        height=2  # Set height (in lines)
    )
    back_button.place(x=660, y=360)

    # Reset button
    back_button = Button(
        conf_window,
        text="Reset",
        command=reset_entries,
        bg="#F5F4F4",  # Set background color
        width=15,  # Set width (in characters)
        height=2  # Set height (in lines)
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

    # Entries
    entry_x = 200
    entry_y = 40
    spacing = 60

    entry1 = Entry(conf_window)
    entry1.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry2 = Entry(conf_window)
    entry2.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry3 = Entry(conf_window)
    entry3.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry4 = Entry(conf_window)
    entry4.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry5 = Entry(conf_window)
    entry5.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry6 = Entry(conf_window)
    entry6.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry7 = Entry(conf_window)
    entry7.place(x=entry_x, y=entry_y)
    entry_y += spacing
    entry8 = Entry(conf_window)
    entry8.place(x=entry_x, y=entry_y)

    # Toggle button
    toggle_var = BooleanVar(value=toggle_state)
    toggle_button = Checkbutton(conf_window, text="", variable=toggle_var, bg="#F5F4F4",
                                font=("Inter", 16))
    toggle_button.place(x=850, y=550)

    canvas2.create_text(
        660.0,
        553.0,
        anchor="nw",
        text="Traffic light visualization",
        fill="#625F80",
        font=("Inter ExtraBold", 15 * -1)
    )

    # Calculate the center coordinates of the screen
    screen_width = conf_window.winfo_screenwidth()
    screen_height = conf_window.winfo_screenheight()
    x_coordinate = (screen_width - 1000) // 2
    y_coordinate = (screen_height - 600) // 2

    # Set the window geometry to center it on the screen
    conf_window.geometry(f"1000x600+{x_coordinate}+{y_coordinate}")

    conf_window.resizable(False, False)
    conf_window.mainloop()


# Function to go back from config to main window
def go_back():
    # Retain toggle state upon reopening
    global toggle_state, toggle_var
    toggle_state = toggle_var.get()

    # Destroy the conf_window
    conf_window.destroy()

    # Restore the window
    window.deiconify()


# Global variables to track time and traffic light state
duration = 2
green_time = duration
yellow_time = duration
red_time = duration
extra_red_duration = 10
extra_green_duration = 10
total_time = green_time + yellow_time + red_time


def draw_traffic_light(current_phase):
    # Define colors
    GREY = (127, 127, 127)
    RED = (0, 0, 255)
    YELLOW = (0, 255, 255)
    GREEN = (0, 255, 0)

    # OpenCV window for the traffic light
    cv2.namedWindow('Traffic Light', cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_NORMAL)

    global object_detected

    # Coordinates for circles
    red_light = (50, 70)
    yellow_light = (50, 150)
    green_light = (50, 230)

    # Radius for circles
    radius = 30

    # Create a black image
    traffic_light = np.zeros((300, 100, 3), dtype=np.uint8)

    if current_phase < green_time:
        # Green phase
        cv2.circle(traffic_light, red_light, radius, GREY, -1)
        cv2.circle(traffic_light, yellow_light, radius, GREY, -1)
        cv2.circle(traffic_light, green_light, radius, GREEN, -1)

    elif current_phase < green_time + yellow_time:
        # Yellow phase
        cv2.circle(traffic_light, red_light, radius, GREY, -1)
        cv2.circle(traffic_light, yellow_light, radius, YELLOW, -1)
        cv2.circle(traffic_light, green_light, radius, GREY, -1)
    elif current_phase < green_time + yellow_time + red_time:
        # Red phase
        cv2.circle(traffic_light, red_light, radius, RED, -1)
        cv2.circle(traffic_light, yellow_light, radius, GREY, -1)
        cv2.circle(traffic_light, green_light, radius, GREY, -1)
        if object_detected:
            cv2.putText(traffic_light, "+10 secs", (10, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    x_coordinate = 1220
    y_coordinate = 150

    # Show the traffic light
    cv2.imshow('Traffic Light', traffic_light)
    # Move the window 
    cv2.moveWindow('Traffic Light', x_coordinate, y_coordinate)
    # Resize the window to 100x300
    cv2.resizeWindow('Traffic Light', 100, 300)


# Bind <Button-1> event to open_link function
info_label.bind("<Button-1>", config_window)


def train_model_and_play(video_path):
    global green_time, extra_green_duration, red_time, extra_red_duration, total_time, duration, red_time, green_time

    model = YOLO(MODEL_PATH)

    # Reset light duration
    red_time = duration

    # Read from webcam 
    if video_path == "live":
        cap = cv2.VideoCapture(0)

    # Read from videopath
    else:
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            messagebox.showerror("error",
                                 "Error: Could not open video file.")
            return

    my_file = open(CLASSES_PATH, "r")
    data = my_file.read()
    class_list = data.split("\n")

    tracker = Tracker()
    area1 = [(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4)]

    global object_detected
    object_detected = False
    paused = False

    # Minimize the window
    window.iconify()

    # ID arrays
    wheelchairs_in_zone = []
    prams_in_zone = []
    crutches_in_zone = []

    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        # Update total_time for when red/green light duration is changed
        total_time = green_time + yellow_time + red_time

        if not paused:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (1020, 500))

            results = model.predict(frame, conf=0.52)
            a = results[0].boxes.data
            px = pd.DataFrame(a).astype("float")

            list = []
            # Extract confidence scores
            confidence_scores = results[0].boxes.conf.cpu().numpy()
            for index, row in px.iterrows():
                x1 = int(row[0])
                y1 = int(row[1])
                x2 = int(row[2])
                y2 = int(row[3])
                d = int(row[5])
                # Get the corresponding confidence score
                confidence_score = confidence_scores[index]

                c = class_list[d]
                if ('wheelchair' in c or 'crutches' in c or 'prams' in c):
                    list.append([x1, y1, x2, y2])

            bbox_idx = tracker.update(list)

            wheelchairs_in_zone = []
            crutches_in_zone = []
            prams_in_zone = []

            # Zip bbox_idx with confidence_scores
            bbox_confidence_pairs = zip(bbox_idx, confidence_scores)

            for bbox, confidence_score in bbox_confidence_pairs:
                x3, y3, x4, y4, id = bbox
                result = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)

                if result >= 0:
                    # Increment counters based on object type
                    for r in results:
                        for c in r.boxes.cls:
                            class_label = model.names[int(c)]
                            # Increment counter based on class label
                            if class_label == "wheelchair":
                                wheelchairs_in_zone.append(id)
                            elif class_label == "crutches":
                                crutches_in_zone.append(id)
                            elif class_label == "prams":
                                prams_in_zone.append(id)

                    cv2.circle(frame, (x4, y4), 5, (0, 0, 255), -1)
                    cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 255, 255), 2)

                    # Draw confidence score on the rectangle
                    confidence_str = f"{confidence_score:.3f}"  # Convert confidence score to string
                    cvzone.putTextRect(frame, confidence_str, (x3, y3), 1, 1)

                    # If a wheelchair is detected(once), extend the duration of the red light.
                    if not object_detected:
                        # print("RED LIGHT EXTENDED FOR 10 SECS")
                        red_time += extra_red_duration
                    object_detected = True

            cv2.polylines(frame, [np.array(area1, np.int32)], True, (0, 255, 0), 2)

            frame = cv2.resize(frame, (800, 600))

            # counter bar
            count_image = np.zeros((600, 200, 3), dtype=np.uint8)
            count_image[:] = (245, 126, 56)

            cv2.putText(count_image, f"Wheelchairs : {len(wheelchairs_in_zone)}", (13, 150), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 2)

            cv2.putText(count_image, f"Crutches : {len(crutches_in_zone)}", (13, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 255, 255), 2)

            cv2.putText(count_image, f"Prams : {len(prams_in_zone)}", (13, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 255, 255), 2)

            display_frame = np.hstack((count_image, frame))
            cv2.imshow('Detection Window', display_frame)

            # Draw traffic lights if button is toggled
            current_phase = elapsed_time % total_time
            if toggle_state:
                draw_traffic_light(current_phase)

            frame_height, frame_width, _ = display_frame.shape
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x_coordinate = int((screen_width - frame_width) / 2)
            y_coordinate = int((screen_height - frame_height) / 2)

            cv2.moveWindow('Detection Window', x_coordinate, y_coordinate)

        key = cv2.waitKey(1)
        if key == ord('q') or not ret:
            break
        elif key == ord(' '):
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
