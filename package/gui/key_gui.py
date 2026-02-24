import tkinter as tk
import random
import enum
from tkinter import ttk
from package.src.key import Key
from package.src.constants import NOTES, INTERVALS,SCALES
import customtkinter as ctk


#------------------------------------------Helper Classes-----------------------------------------------#

class QuizMode(enum.Enum):
    DISTANCE = "distance"
    INTERVAL = "interval"
    SCALE = "scale"
#------------------------------------------Initialization-----------------------------------------------#

notes = NOTES
intervals = [x for x in INTERVALS.values()]
scales=  [x for x in SCALES.keys()]
quiz_a = None
quiz_b = None
current_interval = None
current_scale_name = None
current_scale_intervals = None
quiz_mode = QuizMode.DISTANCE
key = Key("C")
window = tk.Tk()
window.title("Music Notes Trainer")
window.geometry("1200x700")
GREEN= "medium sea green"
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
    # You only need StringVar if you're using a dropdown or something.
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


def generate_random_notes():
    # No need to check unisons
    while True:
        first_note = random.choice(NOTES)
        second_note = random.choice(NOTES)

        if first_note != second_note:
            return first_note, second_note
        
def generate_random_interval():
    
    while True:
        random_interval = random.choice(INTERVALS)


        if random_interval not in ["Perfect Unison", "Octave"] :
            return random_interval

def generate_random_scale():

    name = random.choice(list(SCALES.keys()))
    intervals = SCALES[name]
    return name, intervals




#-----------------------Tab 4 Quiz Logic-----------------------#

def set_distance_mode():
    global quiz_mode
    quiz_mode = QuizMode.DISTANCE
    question_label.configure(text="Distance Quiz")
    ascending_answer_label.configure(text="")
    descending_answer_label.configure(text="")

def set_interval_mode():
    global quiz_mode
    quiz_mode = QuizMode.INTERVAL
    question_label.configure(text="Interval Quiz")
    ascending_answer_label.configure(text="")
    descending_answer_label.configure(text="")

def set_scale_mode():
    global quiz_mode
    quiz_mode = QuizMode.SCALE
    question_label.configure(text="Scale Quiz")
    ascending_answer_label.configure(text="")
    descending_answer_label.configure(text="")

def generate_quiz():
    global quiz_a, quiz_b
    quiz_a, quiz_b = generate_random_notes()
    ascending_answer_label.configure(text="")
    descending_answer_label.configure(text="")

    if quiz_mode == QuizMode.DISTANCE:
    
        question_label.configure(
            text=f"What is the distance from {quiz_a} to {quiz_b}?"
        )

    elif quiz_mode == QuizMode.INTERVAL:
        
        global current_interval 
        current_interval = generate_random_interval()
       
        question_label.configure(
            text=f"Apply a {current_interval} on {quiz_a}"
        )
  
    elif quiz_mode == QuizMode.SCALE:
        global current_scale_name
        global current_scale_intervals
        current_scale_name, current_scale_intervals = generate_random_scale()
        question_label.configure(
            text=f"What is the {current_scale_name} scale for the key of {quiz_a}?"
        )


def distance_quiz_answer(): 
    if quiz_a is None or quiz_b is None:
        ascending_answer_label.configure(text="")
        descending_answer_label.configure(text="")
        return

    
    interval = key.get_intervalName_from_twoNotes(quiz_a, quiz_b)
    half_steps = key.get_halfSteps_from_intervalName(interval)
    whole_half = key.get_wholeHalfSteps_from_halfSteps(half_steps)

    descending_half_steps = 12 - half_steps
    descending_interval = key.get_intervalName_from_halfSteps(descending_half_steps)
    descending_whole_half = key.get_wholeHalfSteps_from_halfSteps(descending_half_steps)

    ascending_answer_label.configure(text=f"Ascending: {interval}: {half_steps} half steps or {whole_half} ")
    descending_answer_label.configure(text=f"Descending: {descending_interval}: {descending_half_steps} half steps, {descending_whole_half} ")



def interval_quiz_answer():

    half_steps = key.get_halfSteps_from_intervalName(current_interval)
    ascending_answer = Key(key=f"{quiz_a}").get_note_from_halfSteps(half_steps)
    descending_answer = Key(key=f"{quiz_a}").get_note_from_halfSteps(12 -half_steps)

    ascending_answer_label.configure(text=f"Ascending: {ascending_answer}  ")
    descending_answer_label.configure(text=f"Descending: {descending_answer} ")

def scale_quiz_answer():

    current_key = Key(quiz_a)
    scale_formula = "   ".join(current_key.generate_scale(current_scale_name))
    scale_intervals= current_key.scale_to_intervalNames(current_scale_name, root_relative=True)
    scale_degrees= "   ".join(key.get_degrees_from_intervals(scale_intervals))

    ascending_answer_label.configure(text=f"{scale_formula}  ")
    descending_answer_label.configure(text=f" {scale_degrees} ")
 

  

    

def show_quiz_answer():
     if quiz_mode == QuizMode.DISTANCE:
         distance_quiz_answer()
     elif quiz_mode == QuizMode.INTERVAL:
         interval_quiz_answer()
     elif quiz_mode == QuizMode.SCALE:
         scale_quiz_answer()
         

   

#-----------------------Notebook and Styles-----------------------#

notebook = ttk.Notebook(window, width= 1500, height= 600)
tab1= ttk.Frame(notebook)
tab2= ttk.Frame(notebook)
tab3= ttk.Frame(notebook)
tab4= ttk.Frame(notebook)

notebook.add(tab1, text= "Notes names trainer")
notebook.add(tab2, text= "Interval names trainer")
notebook.add(tab3, text= "Scales Trainer")
notebook.add(tab4, text= "Quiz")
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
halfSteps_label = ttk.Label(tab1_result_container,text= f" {halfStepsResult} ",font= "Arial 30", relief= tk.GROOVE, borderwidth=2, width= 10, background= GREEN,  anchor="center" )
intervalName_label = ttk.Label(tab1_result_container, text= f" {intervalResult}", font="Arial 30", relief= tk.GROOVE,borderwidth=2, width= 20, background=GREEN, anchor="center")

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
note_label = ttk.Label(tab2, text=f"{noteResult}", font= "Arial 60", anchor="center",relief=tk.GROOVE, background= GREEN, width= 7 )
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
full_scale_degrees_label = ttk.Label(tab3_second_container, text= f"Degrees: {full_scale_degrees}", font= "Arial 22 bold italic", foreground= GREEN)
full_scale_interval_label = ttk.Label(tab3_second_container, text= f"Intervals: {full_scale_intervals}", font= "Arial 22 bold italic", foreground= GOLDENROD2)
full_scale_label.grid(row=1, column=0, sticky= "w", pady=20)
full_scale_degrees_label.grid(row=2, column=0, sticky= "w", pady=20)
full_scale_interval_label.grid(row=3, column=0, sticky="w", pady=20)



#-----------------------Tab 4-----------------------#

#-----------------------Tab 4-----------------------#

quiz_x_note = tk.StringVar(value="")
quiz_y_note = tk.StringVar(value="")
tab4_title_label = ttk.Label(tab4, text="Quiz", font="Arial 40 bold")
tab4_title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="w")

# Mode buttons container
tab4_button_container = tk.Frame(tab4)
tab4_button_container.grid(row=1, column=0, pady=10, sticky="w")

distance_mode_button = ctk.CTkButton(
    tab4_button_container,
    text="Distance Quiz",
    command=lambda: set_distance_mode()
)
distance_mode_button.grid(row=0, column=0, padx=5)

interval_mode_button = ctk.CTkButton(
    tab4_button_container,
    text="Interval Quiz",
    command=lambda: set_interval_mode()
)
interval_mode_button.grid(row=0, column=1, padx=5)

scale_mode_button = ctk.CTkButton(
    tab4_button_container,
    text="Scale Quiz",
    command=lambda: set_scale_mode()
)
scale_mode_button.grid(row=0, column=2, padx=5)

# Answers + quiz area
tab4_container = tk.Frame(tab4)
tab4_container.grid(row=2, column=0, pady=20, sticky="w")

question_label = ttk.Label(tab4_container, text="", font="Arial 24")
question_label.grid(row=0, column=0, pady=5)

question_button = ctk.CTkButton(
    tab4_container,
    text="Generate",
    command=lambda: generate_quiz(),
    height=100,
    width=200,
    font=("Roboto", 20, "bold"),
)
question_button.grid(row=0, column=1, pady=5)

ascending_answer_label = ttk.Label(
    tab4_container, text="", anchor="center", width=50,
    font="Arial 24", foreground=GREEN
)
ascending_answer_label.grid(row=1, column=0, pady=5, padx=5)

descending_answer_label = ttk.Label(
    tab4_container, text="", anchor="center", width=50,
    font="Arial 24", foreground=GOLDENROD2
)
descending_answer_label.grid(row=2, column=0, pady=5, padx=5)

answer_button = ctk.CTkButton(
    tab4_container,
    text="Show Answer",
    command=lambda: show_quiz_answer(),
    height=100,
    width=200,
    font=("Roboto", 20, "bold"),
)
answer_button.grid(row=1, column=1, rowspan=2, pady=5)






window.mainloop()




