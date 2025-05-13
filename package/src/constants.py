NOTES = [
    "C",
    "C#/Db",
    "D",
    "D#/Eb",
    "E",
    "F",
    "F#/Gb",
    "G",
    "G#/Ab",
    "A",
    "A#/Bb",
    "B"
    
]

COLORED_NOTES = {
    "C": "#ffe730",
    "C#/Db": "#a9c431",
    "D": "#53cd32",
    "D#/Eb": "#256e5b",
    "E": "#001a81",
    "F": "#ac3f97",
    "F#/Gb": "#cf3452",
    "G": "#f2290d",
    "G#/Ab": "#f28d82",
    "A": "#f1f1f1",
    "A#/Bb": "#80787e",
    "B": "#ff83c1"
}


# INTERVALS can be seen as distances measured in half steps
# 0, don't move any keys
# 1, move 1 key 
# 2, move 2 keys.
# 3, move 3 keys.

INTERVALS = {
    0: "Perfect Unison",
    1: "Minor 2nd",
    2: "Major 2nd",
    3: "Minor 3rd",
    4: "Major 3rd",
    5: "Perfect 4th",
    6: "Tritone",
    7: "Perfect 5th",
    8: "Minor 6th",
    9: "Major 6th",
    10: "Minor 7th",
    11: "Major 7th",
    12: "Octave"

}


INTERVALS_TO_DEGREE = {
    "Perfect Unison": "1",
    "Minor 2nd": "b2",
    "Major 2nd": "2",
    "Minor 3rd": "b3",
    "Major 3rd": "3",
    "Perfect 4th": "4",
    "Tritone": "#4/b5",
    "Perfect 5th": "5",
    "Minor 6th": "b6",
    "Major 6th": "6",
    "Minor 7th": "b7",
    "Major 7th": "7",
    "Octave": "8"
}



SCALES = {

    "Major": [0,2,4,5,7,9,11],
    "Minor": [0,2,3,5,7,8,10],
    "Major Pentatonic": [0,2,4,7,9],
    "Minor Pentatonic": [0,3,5,7,10],
    "Major Blues": [0,2,3,4,7,9],
    "Minor Blues": [0,3,5,6,7,10],
    "Dorian": [0,2,3,5,7,9,10],
    "Phrygian": [0,1,3,5,7,8,10],
    "Lydian": [0,2,4,6,7,9,11],
    "Mixolydian": [0,2,4,5,7,9,10],
    "Aeolian": [0,1,3,5,7,8,10],
    "Locrian": [0,1,3,5,6,8,10]
    
}

MODES = {
    "Ionian": 0,
    "Dorian": 1,
    "Phrygian": 2,
    "Lydian": 3,
    "Mixolydian": 4,
    "Aeolian": 5,
    "Locrian": 6,
}

CHORDS = {

    "Major": ["Major 3rd", "Perfect 5th"],
    "Minor": ["Minor 3rd", "Perfect 5th"],
    "Diminished": ["Minor 3rd", "Tritone"],
    "Augmented": ["Major 3rd", "Minor 6th"],
    "Major 7th": ["Major 3rd", "Perfect 5th", "Major 7th"],
    "Dominant 7th": ["Major 3rd", "Perfect 5th", "Minor 7th"],
    "Augmented 7th": ["Major 3rd", "Minor 6th", "Minor 7th"],
    "Dominant 7th b5": ["Major 3rd", "Tritone", "Minor 7th"],
    "Minor 7th": ["Minor 3rd", "Perfect 5th", "Minor 7th"],
    "Minor Major 7th": ["Minor 3rd", "Perfect 5th", "Major 7th"],
    "Half Diminished 7th": ["Minor 3rd", "Tritone", "Minor 7th"],
    "Diminished 7th":["Minor 3rd", "Tritone", "Major 6th"]
}




GUITAR_TO_PIANO = {
    2: "#F2A922",
    3: "#294296",
    4: "#962942",
    5: "#3b8f7c",
    6: "#7C3B8F",
}


GUITAR_STRINGS = ["E", "B", "G", "D", "A", "E"]



HARMONICA_DEGREES= {
    1: "'",
    2: "''",
    3: "'''"
}

HARMONICA_SCALES = {

    [4,-4,5,6,-6,7]
}