# tkinter_music
Harmonica and Guitar GUIs on TkInter




# How to run



## On MacOS

You must have Python installed on your system: https://www.python.org/downloads/

- Inside tkinter_music-main, create a virtual environment, activate it and install the requirements

```python
python3 -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
```

- To see the harmonica or guitar gui, run the following commands. 

```python
python3 -m package.gui.harmonica_gui
python3 -m package.gui.guitar_gui
```






#### Guitar GUI Showcase
Main screen
![Guitar Gui Main Screen](images/main.png)
C Major Scale
![C Major Scale](images/C_Major.png)
D Major Chord
![D Major Chord](images/D_Major.png)
Guitar to Piano
![Visualize Piano](images/piano.png)
Color the fretboard
![Color fretboard](images/color.png)

### Harmonica GUI Showcase

Main Screen
![Harmonica Gui Main Screen](images/main_harp.png)
1st Position Major Pentatonic
![1st Position Major Pentatonic](images/major_pentatonic_1st.png)
2nd Position Minor Blues
![2nd Position Minor Blues](images/minor_blues_2nd.png)
3rd Position Dorian
![3rd Position Dorian](images/dorian_3rd.png)


# Future implementations

1. Implementing color pickers that let the user choose the colors for each individual note.
2. Consider how tkinter looks on Linux and Windows.
3. Use more CTk as opposed to TK for scaling issues.
4. Comment more as I go. 


# Love

I love harmonica, guitar & piano!