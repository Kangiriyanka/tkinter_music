import tkinter as tk
from tkinter import ttk
from package.src.key import Key
from package.src.harmonica import *
from package.src.constants import NOTES, HARMONICA_DEGREES
import customtkinter

class HarmonicaSimulator:

    
    def __init__(self, root):
        # Initialize the harmonica in the key of C
        self.key = Key("C")
        self.scale = "Major"
        self.position = "1"
        self.harmonica = Harmonica(self.key)
        self.scale_result = ""
        
        # Main window setup
        self.root = root
        self.root.title("Harmonica Simulator")
        self.buttons = {}
        self.root.state("zoomed")
        self.lick= []
        self.isRecording = False
        self.accidentals_var = tk.BooleanVar(value=False)
        
        
        
        # Create frame for harmonica buttons
        self.harmonica_frame = tk.Frame(self.root, highlightbackground="goldenrod4", highlightthickness=0.5)
        
        self.harmonica_frame.grid(pady=10,padx= 10, row=0, column=0, sticky="nsew", ipadx= 20, ipady= 20)

         # Create frame for scales & positions 
        self.scale_frame = tk.Frame(self.root,)
        self.scale_frame.grid(row=2, column=0,  padx= 1,sticky="ew", columnspan= 2,pady= 20)
        self.radio_flats = ttk.Radiobutton(self.scale_frame, text="Flats", variable=self.accidentals_var, value=False, command = self.scale_color_mapper)
        self.radio_sharps = ttk.Radiobutton(self.scale_frame, text="Sharps", variable=self.accidentals_var, value=True, command = self.scale_color_mapper)
        self.radio_flats.grid(row=1, column = 3, padx= 10, sticky="w")
        self.radio_sharps.grid(row=1, column = 4,padx= 10, sticky="w")
   

        self.note_frame = tk.Frame(self.root)
        self.note_frame.grid(row=4, column=0 , padx= 10)
        
        self.setup_buttons()
        self.setup_labels()
        self.setup_scale_frame()
        # The area where the user can change the key
        self.key_box = customtkinter.CTkComboBox(self.harmonica_frame,
                 values=NOTES,
                 font= ("Roboto", 30),
                 command=  self.change_key)
        
        self.key_box.grid(row=5,column=0,padx=30 )

        
   
        
       
        
    def change_key(self, new_key):

    
       new_key = Key(new_key)
       self.harmonica = Harmonica(new_key)

    def change_scale(self, new_scale):

       self.scale = new_scale
    def change_position(self, new_position):
        self.position = new_position

        match self.position:
            case "1":
                self.scale_combo_box.configure(values=list(FIRST_POSITION_SCALES.keys()))
                self.scale_combo_box.set(list(FIRST_POSITION_SCALES.keys())[0])
                self.scale = list(FIRST_POSITION_SCALES.keys())[0]
            case "2":
                self.scale_combo_box.configure(values=list(SECOND_POSITION_SCALES.keys()))
                self.scale_combo_box.set(list(SECOND_POSITION_SCALES.keys())[0])
                self.scale = list(SECOND_POSITION_SCALES.keys())[0]
            
            case "3":
                self.scale_combo_box.configure(values=list(THIRD_POSITION_SCALES.keys()))
                self.scale_combo_box.set(list(THIRD_POSITION_SCALES.keys())[0])
                self.scale = list(THIRD_POSITION_SCALES.keys())[0]

    def scale_color_mapper(self):
        # Reset the colors to prevent notes/colors from other scales to overlap
        self.reset_colors()
        match self.position:
            case "1":

               scale = self.harmonica.generate_1st_position_scale(self.scale)
               if self.accidentals_var.get():
                    scale= [note.split("/")[0] if "/" in note else note for note in scale]
               
               else: 
                    scale= [note.split("/")[1] if "/" in note else note for note in scale]

               self.scale_label.configure(text=(" " * 5).join(scale))
               for entry in FIRST_POSITION_SCALES[self.scale]:
                    if entry in self.buttons:
                        self.buttons[entry].configure(fg_color="black")
               return scale
                 
                
               

            case "2":
               scale = self.harmonica.generate_2nd_position_scale(self.scale)
              
          
               if self.accidentals_var.get():
                    scale= [note.split("/")[0] if "/" in note else note for note in scale]
                   
               else: 
                    scale= [note.split("/")[1] if "/" in note else note for note in scale]

               self.scale_label.configure(text=(" " * 5).join(scale))
               for entry in SECOND_POSITION_SCALES[self.scale]:
                    if entry in self.buttons:
                        self.buttons[entry].configure(fg_color="black")
               return scale
            
            case "3":
               scale = self.harmonica.generate_3rd_position_scale(self.scale)
               if self.accidentals_var.get():
                    scale= [note.split("/")[0] if "/" in note else note for note in scale]
               else: 
                    scale= [note.split("/")[1] if "/" in note else note for note in scale]

               self.scale_label.configure(text=(" " * 5).join(scale))
               for entry in THIRD_POSITION_SCALES[self.scale]:
                    if entry in self.buttons:
                        self.buttons[entry].configure(fg_color="black")
               return scale
            case _: 
                return "There's another position?"
    
    def reset_colors(self):
       
        self.result_note_label.configure(text="")
        self.result_descriptive_label.configure(text="")
        self.scale_label.configure(text="Select a position & scale")
        for key, button in self.buttons.items():
            if len(key) == 2:
                button.configure(fg_color=COLORED_HARMONICA_NOTES[key[1]])
            else:
            
                button.configure(fg_color=COLORED_HARMONICA_NOTES[f"{key[1]}_{key[2]}"])
            
           
            

    
    def record_licks(self,note):
        self.lick.append(note)

    def write_lick(self):
        f = open("licks.txt", "a")
    
    

        for entry in self.lick:
          for key in entry:
              combo=  str(key) + ": " +  entry[key] + "\n"
              f.write(combo)

        if len(self.lick) != 0:
         f.write("-------------------------------- \n" )
       
         
        
        self.lick= []
        f.close()

    
    def toggle_recording(self):

        self.isRecording = not self.isRecording
       

        if self.isRecording:
            self.recording_button.configure(text= "Stop")
            self.recording_button.configure(width=100, height=50)
            self.recording_button.configure( fg_color="red")
            
        else: 
            self.recording_button.configure(text="Record")
            self.recording_button.configure( fg_color="green")
            self.write_lick()

        

        
    def setup_buttons(self):
        # Add blow buttons for 10 holes
        for i in range(1, 11):
            blow_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}", 
                a_command=lambda i=i: self.play_blow(i), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["blow"],
                a_font=("Roboto", 20)
            )
            self.buttons[(i,"blow")] = blow_button
            blow_button.grid(row=3, column=i, pady=5, padx=5)
        
        # Add draw buttons for 10 holes
        for i in range(1, 11):
            draw_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{-i}", 
                a_command=lambda i=i: self.play_draw(abs(-i)), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["draw"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i,"draw")] = draw_button
           
            draw_button.grid(row=5, column=i)
        
        
        # Add bend buttons for holes that support bending
        self.setup_bend_buttons()

        # Add blow bend buttons for holes that support blow bending
        self.setup_blowbend_buttons()

        # Add overblow and overdraw buttons
        self.setup_overblow_overdraw_buttons()

        self.setup_record_button()

    def create_ctkbutton(self, a_frame, a_width, a_height, a_font, a_fgColor, a_command, a_text):
        return customtkinter.CTkButton(
            a_frame,
            text=a_text,
            width=a_width,
            height=a_height,
            font=a_font,
            fg_color=a_fgColor,
            command=a_command,
           
        )
    
    def create_CTkComboBox(self, a_frame, some_values, a_command):
        return customtkinter.CTkComboBox(
            a_frame,
            values = some_values,
            command=a_command,
           
        )

    def setup_labels(self):
        # Add labels to display result
        self.result_descriptive_label = tk.Label(self.note_frame, text="", font=("Arial italic", 20))
        self.key_label = tk.Label(self.harmonica_frame, text= "Key", font= ("Roboto 20"))
        self.result_note_label = tk.Label(self.note_frame, text="", font=("Arial", 40))
        self.result_descriptive_label.grid(row=0, column=0, columnspan= 2 )
        self.result_note_label.grid(row=1, column= 0, columnspan= 2)
        self.key_label.grid(row=3, column= 0)
        self.current_lick_label= tk.Label(self.root, text= self.lick)
        self.key_label.grid(row=3,column=0)
        self.scale_label = tk.Label(self.root, text= "Select a position & scale", font=("Arial italic", 20), padx= 10, pady= 10, highlightbackground="goldenrod4", highlightthickness=0.5)
        self.scale_label.grid(row=3, column=0, columnspan= 2, padx= 10, pady= 10, sticky= "ew")
        self.scale_result_label = customtkinter.CTkLabel(
            self.root,
            text="",
            text_color="#ff8000",

        )
        self.scale_result_label.grid(row=4, column=1, columnspan= 2, pady= 20)
        
        

    

    def setup_record_button(self):

        self.recording_button = self.create_ctkbutton(self.harmonica_frame,100,50,("Arial",20, "bold"), "green",self.toggle_recording, "Record")
        self.recording_button.grid(row=7 , column=0,)

  

        
    def setup_scale_frame(self):
        self.options_label = tk.Label(self.scale_frame, text="Options", font=("Arial italic", 20))
        self.options_label.grid(row= 0, column=0, sticky= "w",padx= 10, pady= 10)
        self.position_combo_box = self.create_CTkComboBox(self.scale_frame, some_values= ["1","2","3"], a_command= self.change_position)
        self.position_combo_box.grid(row=1 , column=0,padx=10)
        self.scale_combo_box = self.create_CTkComboBox(self.scale_frame, some_values= list(FIRST_POSITION_SCALES.keys()), a_command= self.change_scale)
        self.scale_combo_box.grid(row=1 , column=1,)
        self.generate_scale_button = self.create_ctkbutton(self.scale_frame,100,50,("Arial",20, "bold"), "#B35900",self.scale_color_mapper, "Generate")
        self.generate_scale_button.grid(row=2 , column=0,  padx= 10, pady = 20 ,sticky= "ew",  )
        self.generate_reset_button = self.create_ctkbutton(self.scale_frame,100,50,("Arial",20, "bold"), "#B35900",self.reset_colors, "Reset")
        self.generate_reset_button.grid(row=2 , column=1,  pady = 20, sticky ="ew" )




    def setup_bend_buttons(self):
        for i in [1, 2, 3, 4, 6]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'", 
                a_command=lambda i=i: self.play_bend(i, 1), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["bend_1"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "bend", 1)] = bend_button
            bend_button.grid(row=7, column=i, pady=(20, 5))

        for i in [2, 3]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}''", 
                a_command=lambda i=i: self.play_bend(i, 2), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["bend_2"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "bend", 2)] = bend_button
            bend_button.grid(row=8, column=i)

        for i in [3]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'''", 
                a_command=lambda i=i: self.play_bend(i, 3), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["bend_3"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "bend", 3)] = bend_button
            bend_button.grid(row=9, column=i, pady=5)

    def setup_blowbend_buttons(self):
        for i in [8, 9, 10]:
            blowbend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'", 
                a_command=lambda i=i: self.play_blowbend(i, 1), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["blowbend_1"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "blowbend", 1)] = blowbend_button
            blowbend_button.grid(row=2, column=i, pady=(0, 20))

        for i in [10]:
            blowbend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}''", 
                a_command=lambda i=i: self.play_blowbend(i, 2), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["blowbend_2"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "blowbend", 2)] = blowbend_button
            blowbend_button.grid(row=1, column=i, pady=5)

    def setup_overblow_overdraw_buttons(self):
        for i in [1, 4, 5, 6]:
            overblow_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}ob", 
                a_command=lambda i=i: self.play_overblow(i), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["overblow_1"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "overblow", 1)] = overblow_button
            overblow_button.grid(row=2, column=i, pady=(5, 20))

        for i in [7, 9, 10]:
            overdraw_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}od", 
                a_command=lambda i=i: self.play_overdraw(i), 
                a_width=50, 
                a_height=50,
                a_fgColor=COLORED_HARMONICA_NOTES["overdraw_1"],
                a_font=("Roboto", 18)
            )
            self.buttons[(i, "overdraw", 1)] = overdraw_button
            overdraw_button.grid(row=7, column=i, pady=(20, 5))

    def play_blow(self, hole):
        try:
            note = self.harmonica.blow(hole)
            self.result_descriptive_label.config(text=f"Blow note on hole {hole}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append({hole: note}) if self.isRecording else None
        except ValueError as e:
            self.result_descriptive_label.config(text=str(e))

    def play_draw(self, hole):
        try:
            note = self.harmonica.draw(hole)
            self.result_descriptive_label.config(text=f"Draw note on hole {hole}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append({"-" + str(hole): note}) if self.isRecording else None
        except ValueError as e:
            self.result_descriptive_label.config(text=str(e))

    def play_bend(self, hole, degree):
        try:
            note = self.harmonica.bend(hole, degree)
            self.result_descriptive_label.config(text=f"Bend note on hole {hole}, degree {degree}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append( {str(hole) + HARMONICA_DEGREES[degree]: note}) if self.isRecording else None
        except (ValueError, IndexError, KeyError) as e:
            self.result_descriptive_label.config(text=str(e))

    def play_blowbend(self, hole, degree):
        try:
            note = self.harmonica.blowbend(hole, degree)
            self.result_descriptive_label.config(text=f"Blow bend on hole {hole}, degree {degree}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append( {str(hole) + HARMONICA_DEGREES[degree]: note}) if self.isRecording else None
        except (ValueError, IndexError, KeyError) as e:
            self.result_descriptive_label.config(text=str(e))

    def play_overblow(self, hole):
        try:
            note = self.harmonica.overblow(hole)
            self.result_descriptive_label.config(text=f"Overblow on hole {hole}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append( {str(hole) + "ob": note}) if self.isRecording else None
        except ValueError as e:
            self.result_descriptive_label.config(text=str(e))

    def play_overdraw(self, hole):
        try:
            note = self.harmonica.overdraw(hole)
            self.result_descriptive_label.config(text=f"Overdraw on hole {hole}")
            self.result_note_label.config(text=f"{note}")
            self.lick.append( {str(hole) + "od": note}) if self.isRecording else None
        except ValueError as e:
            self.result_descriptive_label.config(text=str(e))


# Initialize the main window
root = tk.Tk()
harmonica_simulator = HarmonicaSimulator(root)
root.mainloop()