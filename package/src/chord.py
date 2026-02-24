from .constants import CHORDS

class Chord:
    def __init__(self, key):
        self.key = key 

    def generate_chord(self, intervals):
        """
        Generates a chord based on the provided intervals.
        
        :param intervals: A list of interval names (e.g., "Major 3rd", "Perfect 5th").
        :return: A list of notes forming the chord, starting from the root note.
        """
    
        return [self.key.get_key()] + [self.key.get_note_from_intervalName(interval, False) for interval in intervals]
      

    def get_majorChord(self):
        """
        Returns the notes of a major triad (root, major 3rd, perfect 5th).
        
        :return: A list of notes forming the major chord.
        """
        return self.generate_chord(CHORDS["Major"])

    def get_minorChord(self):
        """
        Returns the notes of a minor triad (root, minor 3rd, perfect 5th).
        
        :return: A list of notes forming the minor chord.
        """
        return self.generate_chord(CHORDS["Minor"])

    def get_dimishedChord(self):
        """
        Returns the notes of a diminished triad (root, minor 3rd, tritone).
        
        :return: A list of notes forming the diminished chord.
        """
        return self.generate_chord(CHORDS["Diminished"])

    def get_augmentedChord(self):
        """
        Returns the notes of an augmented triad (root, major 3rd, minor 6th).
        
        :return: A list of notes forming the augmented chord.
        """
        return self.generate_chord(CHORDS["Augmented"])

    def get_major_7thChord(self):
        """
        Returns the notes of a major 7th chord (root, major 3rd, perfect 5th, major 7th).
        
        :return: A list of notes forming the major 7th chord.
        """
        return self.generate_chord(CHORDS["Major 7th"])

    def get_dominant_7thChord(self):
        """
        Returns the notes of a dominant 7th chord (root, major 3rd, perfect 5th, minor 7th).
        
        :return: A list of notes forming the dominant 7th chord.
        """
        return self.generate_chord(CHORDS["Dominant 7th"])

    def get_augmented_7thChord(self):
        """
        Returns the notes of an augmented 7th chord (root, major 3rd, minor 6th, minor 7th).
        
        :return: A list of notes forming the augmented 7th chord.
        """
        return self.generate_chord(CHORDS["Augmented 7th"])

    def get_dominant_7th_b5Chord(self):
        """
        Returns the notes of a dominant 7th chord with a flattened 5th (root, major 3rd, minor 6th, minor 7th).
        
        :return: A list of notes forming the dominant 7th chord with a flattened 5th.
        """
        return self.generate_chord(CHORDS["Dominant 7th b5"])
    
    

    def get_minor_7thChord(self):
        """
        Returns the notes of a minor 7th chord (root, minor 3rd, perfect 5th, minor 7th).
        
        :return: A list of notes forming the minor 7th chord.
        """
        return self.generate_chord((CHORDS["Minor 7th"]))

    def get_minor_major_7thChord(self):
        """
        Returns the notes of a minor major 7th chord (root, minor 3rd, perfect 5th, major 7th).
        
        :return: A list of notes forming the minor major 7th chord.
        """
        return self.generate_chord(CHORDS["Minor Major 7th"])

    def get_half_diminished_7thChord(self):
        """
        Returns the notes of a half-diminished 7th chord (root, minor 3rd, tritone, minor 7th).
        
        :return: A list of notes forming the half-diminished 7th chord.
        """
        return self.generate_chord((CHORDS["Half Diminished 7th"]))

    def get_diminished_7thChord(self):
        """
        Returns the notes of a diminished 7th chord (root, minor 3rd, tritone, major 6th).
        
        :return: A list of notes forming the diminished 7th chord.
        """
        return self.generate_chord((CHORDS["Diminished 7th"]))
    

    def get_major_6thChord(self):
        """
        Returns the notes of a major 6th chord (root, major 3rd, perfect 5th, major 6th).
        """
        return self.generate_chord(CHORDS["Major 6th"])

    def get_minor_6thChord(self):
        """
        Returns the notes of a minor 6th chord (root, minor 3rd, perfect 5th, major 6th).
        """
        return self.generate_chord(CHORDS["Minor 6th"])
    
    def get_inversions(self, chord):
        
        for i in range(1,len(chord)):
            inversion = [chord[(chord.index(note)+ i) % len(chord)] for note in chord]
            print(f"Inversion {i} inversion: {inversion}")