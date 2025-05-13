import tkinter as tk
from tkinter import ttk
from package.src.key import Key
from package.src.constants import NOTES, INTERVALS,SCALES
import customtkinter as ctk


#------------------------------------------Initialization-----------------------------------------------#

notes = NOTES
intervals = [x for x in INTERVALS.values()]
scales=  [x for x in SCALES.keys()]
key = Key("C")
window = tk.Tk()
window.title("Music Notes Trainer")
window.geometry("1200x700")
window.overrideredirect(True)
window.overrideredirect(False)
window.attributes('-fullscreen',True)
GOLDENROD= "goldenrod4"
GOLDENROD2= "goldenrod2"

#------------------------------------------Functions-----------------------------------------------#


def update_key_tab1(event):
    
    global key
    selected_key = tab1_note.get()
    key = Key(selected_key)
    print(f"Key updated to {key.get_key()}")

def update_key_tab2(event):
    
    global key
    selected_key = note_string.get()
    key = Key(selected_key)
    print(f"Key updated to {key.get_key()}")

def update_key_tab3(event):
    
    global key
    selected_key = scale_key_string.get()
    key = Key(selected_key)
    print(f"Key updated to {key.get_key()}")

def change_intervalNames():
    global key
    first= key.get_key()
    second= tab1_second_note.get()
    newValue = key.get_intervalName_from_twoNotes(first,second)
    intervalName_label.configure(text= f"{newValue}")

def change_halfSteps():
    
    global key
    first = key.get_key()
    second= tab1_second_note.get()
    interval_name = key.get_intervalName_from_twoNotes(first,second)
    newValue = key.get_halfSteps_from_intervalName(interval_name)
    halfSteps_label.configure(text= f" {newValue}")

def change_halfSteps_from_intervals():
   
    global key
    interval= interval_string.get()
    condition= descending_var.get()
    newValue = key.get_note_from_intervalName(interval,condition)
    note_label.configure(text= f"{newValue}" )
   
def generateScale():

    global key
    scale = key.generate_scale(scale_string.get())
    scale_intervals= (key.scale_to_intervalNames(scale_string.get(), True))
    
    scale_degrees= key.get_degrees_from_intervals(scale_intervals)

    if accidentals_var.get():
      
        scale= [note.split("/")[0] if "/" in note else note for note in scale]
    else: 
        scale= [note.split("/")[1] if "/" in note else note for note in scale]
       
   
    full_scale= '  '.join(scale,)
    full_scale_intervals= ' |  '.join(scale_intervals)
    full_scale_degrees = '  '.join(scale_degrees)
    full_scale_label.configure(text= f"Notes: {full_scale}")
    full_scale_degrees_label.configure(text= f"Degrees: {full_scale_degrees}")
    full_scale_interval_label.configure(text=f"Intervals: {full_scale_intervals}")

#-----------------------Notebook and Styles-----------------------#

notebook = ttk.Notebook(window, width= 1500, height= 600)
tab1= ttk.Frame(notebook)
tab2= ttk.Frame(notebook)
tab3= ttk.Frame(notebook)

notebook.add(tab1, text= "Notes names trainer")
notebook.add(tab2, text= "Interval names trainer")
notebook.add(tab3, text= "Scales Trainer")
notebook.grid(row=0, column=0)
style = ttk.Style()
style.configure("TRadiobutton",
                font=("Arial", 20),
              
                

               )
# style.configure("TButton",
#                 font=("Arial", 30), padx= 10
               
#                 )

#-----------------------Tab 1-----------------------#

tab1_title_label = ttk.Label(tab1, text="Note to Note Trainer", font="Arial 40 bold")
tab1_title_label.grid(row=0, column=0, columnspan=1, pady=20, sticky= "w")

tab1_container = ttk.Frame(tab1)
tab1_container.grid(row=1, column=0, sticky="w")



# Tab 1 container for the first note
tab1_note = tk.StringVar(value=notes[0])
tab1_note_label= ttk.Label(tab1_container,text= "First Note:" , font= "Arial 25")
tab1_note_combo = ttk.Combobox(tab1_container, textvariable= tab1_note, font="Arial 25", width= 10 )
tab1_note_combo.bind("<<ComboboxSelected>>", update_key_tab1)
tab1_note_combo.bind("<KeyRelease>", update_key_tab1)
tab1_note_combo['values'] = notes

# Setup tab 1's first container
tab1_note_label.grid(row=0, column=0,)
tab1_note_combo.grid(row=0, column=1)

#Tab 1 container for the second note
tab1_second_container = ttk.Frame(tab1)
tab1_second_container.grid(row=2, column=0, sticky="w", pady= 5)

tab1_second_note = tk.StringVar(value=notes[0])
tab2_second_combo= ttk.Combobox(tab1_second_container, textvariable= tab1_second_note, font="Arial 24", width= 10 )
tab2_second_combo['values'] = notes

second_note_label= ttk.Label(tab1_second_container,text= "Second Note:" , font= "Arial 24")
second_note_label.grid(row=0, column=0)
tab2_second_combo.grid(row=0, column=1)

# Buttons and Labels

tab1_button_container = ttk.Frame(tab1, padding= 20)
tab1_result_container = ttk.Frame(tab1)

halfStepsButton = ctk.CTkButton(tab1_button_container, text= "Half-Steps", command= lambda: change_halfSteps(), height= 100, width= 150,  font=("Roboto", 20, "bold"),)
intervalButton = ctk.CTkButton(tab1_button_container, text= "Interval ", command= lambda: change_intervalNames(), height= 100, width= 150,  font=("Roboto", 20, "bold"),  )

ttk.Separator(tab1, orient="vertical").grid(column=1, row=1, padx= 30, rowspan=4, sticky='ns')
tab1_button_container.grid(row=3, column = 0, rowspan= 2, sticky= "nsew" )
tab1_result_container.grid(row=1,  column=2, sticky= "w")
intervalButton.grid(row= 0, column =1,  sticky="ew", padx= 10)
halfStepsButton.grid(row= 0, column =0, sticky="ew")



halfStepsResult = ""
intervalResult= ""
ttk.Label(tab1_result_container,text="Half-Steps & Interval Name", font= "Arial 25  ").grid(row=0,column=0 , pady= 20, sticky="n")
halfSteps_label = ttk.Label(tab1_result_container,text= f" {halfStepsResult} ",font= "Arial 30", relief= tk.GROOVE, borderwidth=2, width= 10, background= GOLDENROD,  anchor="center" )
intervalName_label = ttk.Label(tab1_result_container, text= f" {intervalResult}", font="Arial 30", relief= tk.GROOVE,borderwidth=2, width= 20, background=GOLDENROD, anchor="center")

halfSteps_label.grid(row=1, column=0 ,  ipady= 10,  sticky= "ew" )
intervalName_label.grid(row=1,column=1, ipady= 10 , sticky= "ew" )

#-----------------------Tab 2-----------------------#

note_string = tk.StringVar(value=notes[0])


tab2_title_label = ttk.Label(tab2, text="Interval to Note Trainer", font="Arial 40 bold")
tab2_title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky= "w")

tab2_container = ttk.Frame(tab2)
tab2_container.grid(row=1, column=0, sticky="w")

ttk.Separator(tab2, orient="vertical").grid(column=1, row=1, rowspan=5, padx= 30, sticky='ns')


tab2_note_combo = ttk.Combobox(tab2_container, textvariable= note_string, font="Arial 24")
tab2_note_combo['values'] = notes
tab2_note_combo.bind("<<ComboboxSelected>>", update_key_tab2)
tab2_note_combo.bind("<KeyRelease>", update_key_tab2)
tab2_note_combo.grid(row = 0, column = 1)
note_label= ttk.Label(tab2_container,text= "Note:" , font= "Arial 24")
note_label.grid(row=0, column=0)


tab2_second_container = ttk.Frame(tab2)
tab2_second_container.grid(row=2, column=0, sticky="w", pady= 5)

interval_string = tk.StringVar(value=intervals[0])
interval_combo = ttk.Combobox(tab2_second_container, textvariable= interval_string, font="Arial 24")
interval_combo['values'] = intervals
interval_combo.grid(row =0, column =1 )
interval_label= ttk.Label(tab2_second_container,text= "Interval: " , font= "Arial 24")
interval_label.grid(row=0, column=0)


tab2_third_container= ttk.Frame(tab2)
tab2_third_container.grid(row=3, column=0, sticky="w", pady= 1)

descending_var = tk.BooleanVar(value=False)
radio_label = ttk.Label(tab2_third_container, text="Direction:", font="Arial 24")
radio_label.grid(row= 0, column=0 ,pady=5)

radio_true = ttk.Radiobutton(tab2_third_container, text="Descending", variable=descending_var, value=True,)
radio_false = ttk.Radiobutton(tab2_third_container, text="Ascending", variable=descending_var, value=False)

radio_true.grid(row=0, column = 1, padx=10)
radio_false.grid(row=0, column = 2, padx=10)


noteResult = ""
notesButton = ctk.CTkButton(tab2, text= "Generate",   command= lambda: change_halfSteps_from_intervals(), height= 100, width= 150,  font=("Roboto", 20, "bold"))

ttk.Label(tab2,text="Note", font= "Arial 20 bold ",anchor="center").grid(row=1,column=5,  sticky="n")
note_label = ttk.Label(tab2, text=f"{noteResult}", font= "Arial 60", anchor="center",relief=tk.GROOVE, background= GOLDENROD, width= 7 )
notesButton.grid(row=5, column= 0, pady= 10)
note_label.grid(row=2, column= 5)


#-----------------------Tab 3-----------------------#

tab3_title_label = ttk.Label(tab3, text="Scale Trainer", font="Arial 40 bold")
tab3_title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky= "w")



tab3_container = tk.Frame(tab3)
tab3_container.grid(row=1, column=0, pady= 20, sticky="w")


scale_key_string = tk.StringVar(value=notes[0])
scale_key_combo = ttk.Combobox(tab3_container, textvariable= scale_key_string, font="Arial 30", width= 5)
scale_key_combo.bind("<<ComboboxSelected>>", update_key_tab3)
# Allows the key to change when user inputs values rather than after the selection
scale_key_combo.bind("<KeyRelease>", update_key_tab3)
scale_key_combo['values'] = notes
scale_key_combo.grid(row=0, column=0, sticky="w")



scale_string = tk.StringVar(value=scales[0])
scale_combo = ttk.Combobox(tab3_container, textvariable= scale_string, font="Arial 30", width= 15)
scale_combo['values']= scales
scale_combo.grid(row=0, column= 1, sticky="w")

accidentals_container= ttk.Frame(tab3_container)
accidentals_container.grid(row=0, column=3, sticky="w")

accidentals_var = tk.BooleanVar(value=False)
radio_flats = ttk.Radiobutton(accidentals_container, text="Flats", variable=accidentals_var, value=False,)
radio_sharps = ttk.Radiobutton(accidentals_container, text="Sharps", variable=accidentals_var, value=True)


accidentals_container.bind("<KeyRelease>", generateScale)
radio_flats.grid(row=0, column = 1, padx= 10, sticky="w")
radio_sharps.grid(row=0, column = 2,padx= 10, sticky="w")


generateScaleButton = ctk.CTkButton(tab3_container, text= "Generate" ,command= lambda: generateScale(), height= 100, width=150, font= ("Roboto", 20) )

generateScaleButton.grid(row=0, column= 4, columnspan=3, sticky="w", padx= 20)

tab3_second_container = ttk.Frame(tab3)
ttk.Separator(tab3, orient="horizontal").grid(column=0, columnspan=2 ,row=2,  sticky='we')
tab3_second_container.grid(row=3, column=0)
full_scale = ""
full_scale_degrees = ""
full_scale_intervals = ""
full_scale_label = ttk.Label(tab3_second_container, text= f"Notes:{full_scale}", font= "Arial 22 bold italic ",foreground= "light goldenrod" )
full_scale_degrees_label = ttk.Label(tab3_second_container, text= f"Degrees: {full_scale_degrees}", font= "Arial 22 bold italic", foreground= GOLDENROD)
full_scale_interval_label = ttk.Label(tab3_second_container, text= f"Intervals: {full_scale_intervals}", font= "Arial 22 bold italic", foreground= GOLDENROD2)
full_scale_label.grid(row=1, column=0, sticky= "w", pady=20)
full_scale_degrees_label.grid(row=2, column=0, sticky= "w", pady=20)
full_scale_interval_label.grid(row=3, column=0, sticky="w", pady=20)



window.mainloop()




