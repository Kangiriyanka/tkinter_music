import tkinter as tk
from package.src.key import Key
from package.src.harmonica import Harmonica 
from package.src.constants import NOTES, HARMONICA_DEGREES
import customtkinter

class HarmonicaSimulator:

    
    def __init__(self, root):
        # Initialize the harmonica in the key of C
        self.key = Key("C")
        self.harmonica = Harmonica(self.key)
        
        # Main window setup
        self.root = root
        self.root.title("Harmonica Simulator")
        self.root.state("zoomed")
        self.lick= []
        self.isRecording = False
        
        
        
        # Create frame for harmonica buttons
        self.harmonica_frame = tk.Frame(self.root)
        self.harmonica_frame.grid(pady=30, row=0, column=1, sticky="nsew")
        
        self.setup_buttons()
        self.setup_labels()
        # The area where the user can change the key
        self.key_box = customtkinter.CTkComboBox(master=self.harmonica_frame,
                 values=NOTES,
                 font= ("Roboto", 30),
                 command=  self.change_key)
        
        self.key_box.grid(row=5,column=0,padx=30 )
        
       
        
    def change_key(self, new_key):

       print("Key updated to " + new_key)
       new_key = Key(new_key)
       self.harmonica = Harmonica(new_key)
    
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
                a_fgColor="Royal Blue",
                a_font=("Roboto", 20)
            )
            blow_button.grid(row=3, column=i, pady=5, padx=5)
        
        # Add draw buttons for 10 holes
        for i in range(1, 11):
            draw_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{-i}", 
                a_command=lambda i=i: self.play_draw(abs(-i)), 
                a_width=50, 
                a_height=50,
                a_fgColor="goldenrod4",
                a_font=("Roboto", 18)
            )
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

    def setup_labels(self):
        # Add labels to display result
        self.result_descriptive_label = tk.Label(self.root, text="Select a hole", font=("Arial italic", 20))
        self.key_label = tk.Label(self.harmonica_frame, text= "Key", font= ("Roboto 20"))
        self.result_note_label = tk.Label(self.root, text="", font=("Arial", 60))
        self.result_descriptive_label.grid(row=2, column=1, pady=20)
        self.result_note_label.grid(row=3, column= 1)
        self.key_label.grid(row=3, column= 0)
        self.current_lick_label= tk.Label(self.root, text= self.lick)
        self.key_label.grid(row=3,column=0)

    

    def setup_record_button(self):

        self.recording_button = self.create_ctkbutton(self.root,100,50,("Arial",20, "bold"), "green",self.toggle_recording, "Record")
        self.recording_button.grid(row=4 , column=2,)
        



    def setup_bend_buttons(self):
        for i in [1, 2, 3, 4, 6]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'", 
                a_command=lambda i=i: self.play_bend(i, 1), 
                a_width=50, 
                a_height=50,
                a_fgColor="green",
                a_font=("Roboto", 18)
            )
            bend_button.grid(row=7, column=i, pady=(20, 5))

        for i in [2, 3]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}''", 
                a_command=lambda i=i: self.play_bend(i, 2), 
                a_width=50, 
                a_height=50,
                a_fgColor="medium sea green",
                a_font=("Roboto", 18)
            )
            bend_button.grid(row=8, column=i)

        for i in [3]:
            bend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'''", 
                a_command=lambda i=i: self.play_bend(i, 3), 
                a_width=50, 
                a_height=50,
                a_fgColor="sea green",
                a_font=("Roboto", 18)
            )
            bend_button.grid(row=9, column=i, pady=5)

    def setup_blowbend_buttons(self):
        for i in [8, 9, 10]:
            blowbend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}'", 
                a_command=lambda i=i: self.play_blowbend(i, 1), 
                a_width=50, 
                a_height=50,
                a_fgColor="DodgerBlue2",
                a_font=("Roboto", 18)
            )
            blowbend_button.grid(row=2, column=i, pady=(0, 20))

        for i in [10]:
            blowbend_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}''", 
                a_command=lambda i=i: self.play_blowbend(i, 2), 
                a_width=50, 
                a_height=50,
                a_fgColor="DodgerBlue4",
                a_font=("Roboto", 18)
            )
            blowbend_button.grid(row=1, column=i, pady=5)

    def setup_overblow_overdraw_buttons(self):
        for i in [1, 4, 5, 6]:
            overblow_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}ob", 
                a_command=lambda i=i: self.play_overblow(i), 
                a_width=50, 
                a_height=50,
                a_fgColor="DarkOrange2",
                a_font=("Roboto", 18)
            )
            overblow_button.grid(row=2, column=i, pady=(5, 20))

        for i in [7, 9, 10]:
            overdraw_button = self.create_ctkbutton(
                self.harmonica_frame,
                a_text=f"{i}od", 
                a_command=lambda i=i: self.play_overdraw(i), 
                a_width=50, 
                a_height=50,
                a_fgColor="firebrick3",
                a_font=("Roboto", 18)
            )
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