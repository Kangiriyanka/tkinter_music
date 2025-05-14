import tkinter as tk
from tkinter import  ttk
from package.src.key import Key
from package.src.chord import Chord
from package.src.harmonica import Harmonica
from package.src.constants import NOTES, GUITAR_STRINGS, COLORED_NOTES, SCALES, GUITAR_TO_PIANO, CHORDS
import customtkinter
import mss, mss.tools
import os
import secrets


X_PADDING_BUTTONS = 15
Y_PADDING_BUTTONS = 15
X_PADDING_FRAMES = 30
Y_PADDING_FRAMES = 10
X_IPAD_FRAMES = 20
Y_FRETLABEL_PADDING = 20
FRET_BUTTON_WIDTH = 50
FRET_BUTTON_HEIGHT = 50
COLUMNSPAN = 2
BUTTON_COLOR = "#B35900"
BUTTON_HOVER_COLOR = "#6B3500"
BUTTON_BORDER_COLOR = "gray23"
BUTTON_FONT_SIZE = 20
GENERAL_FONT_SIZE = 30
UNCLICKED_COLOR = "gray18"



class GuitarFretboard:
    def __init__(self, root):
        self.root = root
        self.key = "C"
        self.scale_name = "Major"
        self.chord_name = "Major"
        self.root.title("Guitar Fretboard")
        root.overrideredirect(True)
        root.overrideredirect(False)
        root.attributes('-fullscreen',True)

        
        self.buttons = {}
        self.fretboardRootFrame = tk.Frame(
            root, relief=tk.SUNKEN, highlightbackground="black", highlightthickness=3
        )
        self.fretboardRootFrame.grid(
            row=0, column=0, padx=X_PADDING_FRAMES, sticky="nw", pady=Y_PADDING_FRAMES
        )
        self.fretboardFrame = tk.Frame(root)

        self.fretboardFrame.grid(row=0, column=1, pady=Y_PADDING_FRAMES)
        self.first_separator = ttk.Separator(orient="horizontal")
        self.first_separator.grid(row=1, column=0, columnspan=COLUMNSPAN, sticky="ew")
        self.second_separator = ttk.Separator(orient="horizontal")
        self.second_separator.grid(row=4, column=0, columnspan=COLUMNSPAN, sticky="ew")
        self.scalePickerFrame = tk.Frame(root)
        self.chordPickerFrame= tk.Frame(root)
        self.scalePickerFrame.grid(
            row=3, column=0, columnspan=COLUMNSPAN, padx=X_PADDING_FRAMES, sticky="w"
        )
       
        self.scaleInformationFrame = tk.Frame(root)
        self.scaleInformationFrame.grid(row=3, column=1, padx=X_PADDING_FRAMES)

        self.fretboard = self.setup_fretboard()
        self.setup_fretNumbers()
        self.setup_scaleSelector()
        self.setup_scaleInformation()

       
        self.snap_scale_button = customtkinter.CTkButton(
            self.root, text="Snap the scale", 
            font= ("Roboto", 20, "bold"), 
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            command=self.snapshot, width = 50, height = 25
            )
        self.snap_chord_button = customtkinter.CTkButton(
            self.root, text="Snap the chord", 
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            font= ("Roboto", 20, "bold"), 
            command=lambda is_chord= True :self.snapshot(is_chord= True), 
            width = 50, height = 25
        )

        self.screenshot_button = customtkinter.CTkButton(
            self.root, text="Simple screenshot", 
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            font= ("Roboto", 20, "bold"), 
            command=self.simple_snapshot, 
            width = 50, height = 25
        )


        self.screenshot_button.grid(row=1, column=1 , sticky= "e", padx= 5 )
        self.snap_scale_button.grid(row=1, column=2, sticky= "e",  padx = 5)
        self.snap_chord_button.grid(row=1, column=3 , sticky= "e", padx= 5)
        

    def simple_snapshot(self):
  

        screenshot_directory = f"./screenshots/"
        os.makedirs(screenshot_directory, exist_ok=True)
        filename = "screenshot_" + secrets.token_hex(4) + ".png"
      
       
    

        with mss.mss() as sct:
          
            # Use the 1st monitor
            # From the API: Each monitor is a dict with left-top-width-height 
            # left is the x coordinate of the upper-left corner and top is the y coordinate of the upper-left corner
            monitor = sct.monitors[1]

            left = monitor["left"] 
            top = monitor["top"] 
            width = monitor["width"]
            height = monitor["height"]
            bbox = (top,left,width,height)

        
            im = sct.grab(bbox)
            mss.tools.to_png(im.rgb, im.size, output= os.path.join(screenshot_directory, filename))

    def snapshot(self, is_chord = False):
        """
        Takes a screenshot of the current application window and saves it as a PNG file.

        The screenshot is saved in a directory based on the key and whether the capture 
        is for a scale or a chord.
        Directories created (if they don't exist):
            - scales/<key>/ for scale images
            - chords/<key>/ for chord images

        Filenames are automatically generated using the key and the scale/chord name.

        Args:
            is_chord (bool): If True, saves the image to the chords directory using 
                            the chord name. If False, saves to scales directory 
                            using the scale name.
    """
        key = self.key
        if "/" in self.key:
            key = self.key.replace("/", "|")
        scale_directory = f"./scales/{key}"
    
        chord_directory = f"./chords/{key}"
        
        os.makedirs(scale_directory, exist_ok=True)
        os.makedirs(chord_directory, exist_ok=True)

        filename = f"{key}_{"_".join(self.scale_name.split(" "))}.png"
        output_path = os.path.join(scale_directory, filename)


        if is_chord: 
         filename = f"{key}_{"_".join(self.chord_name.split(" "))}.png"
         output_path = os.path.join(chord_directory, filename)
    

        with mss.mss() as sct:
           
            # Use the 1st monitor
            # From the API: Each monitor is a dict with left-top-width-height 
            # left is the x coordinate of the upper-left corner and top is the y coordinate of the upper-left corner
            monitor = sct.monitors[1]

            left = monitor["left"] 
            top = monitor["top"] 
            width = monitor["width"]
            height = monitor["height"]
            bbox = (top,left,width,height)

        
            im = sct.grab(bbox)
            mss.tools.to_png(im.rgb, im.size, output=output_path)



    def setup_fretboard(self):
        fretboard = []
        for guitarString in GUITAR_STRINGS:

            notes = (
                NOTES[NOTES.index(guitarString) :]
                + NOTES[: NOTES.index(guitarString) + 1]
                + [
                    NOTES[(NOTES.index(guitarString) + i) % len(NOTES)]
                    for i in range(1, 4)
                ]
            )
            fretboard.append(notes)

        for i, guitarString in enumerate(fretboard):
            for j, fret in enumerate(guitarString):
                # Unfretted Strings
                if j == 0:
                    button = customtkinter.CTkButton(
                        self.fretboardRootFrame,
                        text=fret,
                        font=("Roboto", 20, "bold"),
                        border_spacing=10,
                        corner_radius=15,
                        fg_color=COLORED_NOTES[guitarString[0]],
                    
                        text_color=("white", "black"),
                        height=FRET_BUTTON_HEIGHT,
                        width=FRET_BUTTON_WIDTH,
                        command= lambda i=i, j=j ,a_color= COLORED_NOTES[guitarString[0]] : self.color_button(i,j, a_color)
                    )
                    self.buttons[(i, j)] = button
                    button.grid(
                        row=i, column=j, padx=X_PADDING_BUTTONS, pady=Y_PADDING_BUTTONS
                    )
                # Fretted Strings
                else:
                    button = customtkinter.CTkButton(
                        self.fretboardFrame,
                        text=fret if len(fret) == 1 else fret.split("/")[1],
                        font=("Roboto", 20, "bold"),
                        border_spacing=10,
                        corner_radius=15,
                        fg_color=COLORED_NOTES[fret],
                        text_color=("white", "black"),
                        height=FRET_BUTTON_HEIGHT,
                        width=FRET_BUTTON_WIDTH,
                        command =lambda i=i, j=j, a_color= COLORED_NOTES[fret]: self.color_button(i,j, a_color)
                    )
                    self.buttons[(i, j)] = button

                    button.grid(
                        row=i, column=j, padx=X_PADDING_BUTTONS, pady=Y_PADDING_BUTTONS
                    )
        return fretboard

    def setup_fretNumbers(self):
        fret_numbers = ["3", "5", "7", "9", "12", "15"]
        columns = [3, 5, 7, 9, 12, 15]

        for fret_number, column in zip(fret_numbers, columns):
            label = tk.Label(
                self.fretboardFrame,
                text=fret_number,
                font="Helvetica 30",
                borderwidth=1,
                relief=tk.SUNKEN,
                fg="white",
                bg="black",
                padx=10,
            )
            # There 6 strings, the fret numbers will go on row 7
            label.grid(row=7, column=column, pady=Y_FRETLABEL_PADDING)

    def setup_scaleInformation(self):
        self.scale_label = customtkinter.CTkLabel(
            self.scaleInformationFrame,
            text=f"Select a key and scale",
            font=("Roboto", GENERAL_FONT_SIZE, "bold"),
            text_color="#ff8000",
        )
        self.scale_label.grid(row=0, column=1, sticky="w", pady=50)

        self.degree_label = customtkinter.CTkLabel(
            self.scaleInformationFrame, text=f"", font=("Roboto", 40, "bold")
        )
        self.degree_label.grid(row=1, column=1, sticky="w")

    def setup_scaleSelector(self):
        label = customtkinter.CTkLabel(
            self.scalePickerFrame, text="Choose a scale or chord", font=("Roboto", 30, "bold")
        )
        label.grid(row=0, column=0,columnspan = 2 ,pady=(20, 50), sticky="w")

        keyPicker = customtkinter.CTkComboBox(
            self.scalePickerFrame,
            values=NOTES,
            command=self.change_key,
            font=("Roboto", GENERAL_FONT_SIZE),
        )
        keyPicker.grid(row=1, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")

        scalePicker = customtkinter.CTkComboBox(
            self.scalePickerFrame,
            values=list(SCALES.keys()),
            command=self.change_scale,
            font=("Roboto", GENERAL_FONT_SIZE),
        )

        chordPicker = customtkinter.CTkComboBox(
            self.scalePickerFrame,
            values= list(CHORDS.keys()),
            command=self.change_chord,
            font=("Roboto", 30),
        )


        scalePicker.grid(row=2, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")
        chordPicker.grid(row=2, column=1, pady=Y_PADDING_FRAMES, sticky="nsew")
    

        generateScaleButton = customtkinter.CTkButton(
            self.scalePickerFrame,
            font=("Roboto", BUTTON_FONT_SIZE, "bold"),
            text="Generate Scale",
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            border_spacing=10,
            border_width=2,
            command=self.scale_color_mapper,
        )


        generateChordButton = customtkinter.CTkButton(
            self.scalePickerFrame,
            font=("Roboto", BUTTON_FONT_SIZE, "bold"),
            text="Generate Chord",
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            border_spacing=10,
            border_width=3,
            command=self.chord_color_mapper,
        )
        generateScaleButton.grid(row=3, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")
        generateChordButton.grid(row=3, column=1, columnspan = COLUMNSPAN, pady=Y_PADDING_FRAMES, sticky="nsew")

        resetButton = customtkinter.CTkButton(
            self.scalePickerFrame,
            font=("Roboto", BUTTON_FONT_SIZE, "bold"),
            text="Reset",
            fg_color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            border_spacing=10,
            border_width=1,
            command=self.reset_colors,
        )

        visualizeButton = customtkinter.CTkButton(
            self.scalePickerFrame,
            font=("Roboto", BUTTON_FONT_SIZE, "bold"),
            text="Visualize",
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            border_spacing=10,
            border_width=1,
            command=self.visualize_piano,
        )

        colorButton = customtkinter.CTkButton(
            self.scalePickerFrame,
            font=("Roboto", BUTTON_FONT_SIZE, "bold"),
            text="Color",
            hover_color=BUTTON_HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            border_color=BUTTON_BORDER_COLOR,
            border_spacing=10,
            border_width=1,
            command=self.color_fretboard,
        )
        visualizeButton.grid(row=5, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")
        colorButton.grid(row=6, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")
        resetButton.grid(row=7, column=0, pady=Y_PADDING_FRAMES, sticky="nsew")


    def update_scale_labels(self, new_label):
        # Keep only flats in the list
        new_label = [x.split("/")[1] if len(x) > 2 else x for x in new_label]
        key = Key(self.key)
        scale_name = self.get_scale()
        intervals = key.scale_to_intervalNames(scale_name, True)
        degrees = key.get_degrees_from_intervals(intervals)

        self.scale_label.configure(text=(" " * 5).join(new_label))
        self.degree_label.configure(text=(" " * 5).join(degrees))

    def update_chord_labels(self, chord_intervals, new_label):
        # Keep only flats in the list
      
        key = Key(self.key)

        degrees = key.get_degrees_from_intervals(chord_intervals)
        
        self.scale_label.configure(text=(" " * 5).join(new_label))
        self.degree_label.configure(text=(" " * 5).join(degrees))


    


    def scale_color_mapper(self):
        scale_key = Key(self.key)
        scale = scale_key.generate_scale(self.scale_name)
        self.update_scale_labels(scale)

        for i, guitarString in enumerate(self.fretboard):
            for j, fret in enumerate(guitarString):
                # Check if the fret matches the tonic (root note of the scale)
                if fret == self.key:
                    self.update_color(self.buttons[(i, j)], "turquoise")
                # Check if the fret is in the scale and color based on the degree
                elif fret in scale:
                    # Find its position in the scale
                    self.update_color(self.buttons[(i, j)], COLORED_NOTES[fret])
                else:
                    self.update_color(self.buttons[(i, j)], UNCLICKED_COLOR)
    def chord_color_mapper(self):
        scale_key = Key(self.key)
        chord = Chord(scale_key).generate_chord(CHORDS[self.chord_name])
     
        self.update_chord_labels( ["Perfect Unison"] + CHORDS[self.chord_name], chord)

        for i, guitarString in enumerate(self.fretboard):
            for j, fret in enumerate(guitarString):
                # Check if the fret matches the tonic (root note of the scale)
                if fret == self.key:
                    self.update_color(self.buttons[(i, j)], "turquoise")
                # Check if the fret is in the scale and color based on the degree
                elif fret in chord:
                    # Find its position in the scale
                    self.update_color(self.buttons[(i, j)], COLORED_NOTES[fret])
                else:
                    self.update_color(self.buttons[(i, j)], UNCLICKED_COLOR)


    def color_button(self,x,y,a_color):

      
        
        if self.buttons[(x,y)].cget("fg_color") == UNCLICKED_COLOR:
        
            self.update_color(self.buttons[(x,y)], a_color)
        else:
            self.update_color(self.buttons[(x,y)], UNCLICKED_COLOR)


        
        self.scale_label.configure(text= f"String {x}  Fret {y} ")
        self.degree_label.configure(text= "")
        

    def color_fretboard(self):

      
        # Make every button colorless 
        self.scale_label.configure(text= f"Click the notes")
        for button in self.buttons.values():
            
            button.configure(fg_color=UNCLICKED_COLOR)
        

  

    
        
    def visualize_piano(self):

        start_colors = [4, 3, 3, 3, 2, 2]
        pianoColors = []
        self.scale_label.configure(text=f"E4  B3  G3  D3  A2  E2")
        self.degree_label.configure(text=f"")

        for color, guitarString in zip(start_colors, self.fretboard):
            temp = []
            for fret in guitarString:
                if fret == "C":
                    color += 1
                    temp.append(GUITAR_TO_PIANO[color])
                else:
                    temp.append(GUITAR_TO_PIANO[color])
            pianoColors.append(temp)

        for i, guitarString in enumerate(pianoColors):
            for j, color in enumerate(guitarString):
                self.update_color(self.buttons[(i, j)], color)

    def change_key(self, a_key):
        self.key = a_key

    def get_scale(self):
        return self.scale_name

    def change_scale(self, a_scale_name):
 
        self.scale_name = a_scale_name
      
    def change_chord(self,a_chord_name):
        self.chord_name = a_chord_name
        

    def update_color(self, a_button, a_color):
        a_button.configure(fg_color=a_color)

    def reset_colors(self):
        # Initialize a key to have access to our match note
        scale_key = Key(self.key)
        self.scale_label.configure(text=f"Select a key and scale")
        self.degree_label.configure(text=f"")

        for button in self.buttons.values():
            note = scale_key.match_note(button.cget("text"))
            
            button.configure(fg_color=COLORED_NOTES[note])


# Initialize the main window

root = tk.Tk()
GuitarFretboard(root)



root.mainloop()