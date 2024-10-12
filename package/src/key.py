from .constants import *
class Key:
    def __init__(self, key):
        """
        Initializes the Key object with a given musical key.

        :param key: The musical key to be matched.
        """
        self.key = self.match_note(key)
        self.majorScale = self.generate_scale("Major")
        

    def get_key(self):
        return self.key
    

    def match_note(self, input_key):
        """
        Matches the input key to the nearest valid note.
        Handles cases where the user input contains flats or sharps.

        :param input_key: The note to match.
        :return: The matched note.
        :raises ValueError: If the input key is invalid.
        """
        if input_key in NOTES:
            return input_key
        for note in NOTES:
            if input_key in note.split("/"):
                return note
        raise ValueError(f"Invalid key {input_key}")

    def generate_mode(self, mode):
        """
        Gives modes that can be generated from that key.
        e.g. the 4th mode of the C major scale is a G Mixolydian.

        :param input_key: The mode we want to convert to.
        :return: The new scale depending on the mode.
        :raises ValueError: If the mode is invalid.
        """
        if mode.capitalize() not in MODES:
            raise ValueError(f"The mode {mode} does not exist")
         
        shift = MODES[mode]
        mode_scale = self.majorScale[shift:] + self.majorScale[:shift]
        return mode_scale
    

    
    def generate_scale(self, scale):
        """
        Generates a musical scale based on the provided scale name.

        :param scale: The name of the scale to generate.
        :return: The generated scale.
        :raises ValueError: If the scale does not exist.
        """
        if scale not in SCALES:
            raise ValueError(f"The scale {scale} does not exist")
        
        generated_scale = [self.get_note_from_halfSteps(x) for x in SCALES[scale]]
        return generated_scale

    def flatten(self, a_note, a_degree):
        """
        Gets the interval name from start note to end note.

        :param a_note: The note to flatten.
        :param a_degree: The number of times we want it to be flattened.
        :return: The flattened note.
        :raises ValueError: If a_note invalid.
        """
          
        a_note = self.match_note(a_note)
        return NOTES[(NOTES.index(a_note) - a_degree) % len(NOTES)]
    
    def sharpen(self, a_note, a_degree):
        """
        Gets the interval name from start note to end note.

        :param a_note: The note to sharpen.
        :param a_degree: The number of times we want it to be sharpened.
        :return: The sharpened note.
        :raises ValueError: If a_note invalid.
        """
          
        a_note = self.match_note(a_note)
        return NOTES[(NOTES.index(a_note) + a_degree) % len(NOTES)]


    def get_degrees_from_intervals(self, intervals):
        """
        Gets the degree notation for each interval in a list

        :param intervals: A list of intervals
        :return: A list of the degrees corresponding to each interval.
        :raises ValueError: If either the start or end note is invalid.
        """

        for interval in intervals:
            if interval not in INTERVALS_TO_DEGREE:
                raise ValueError(f"{interval} does not exist")

        return [INTERVALS_TO_DEGREE[interval] for interval in intervals]



    def get_intervalName_from_twoNotes(self, start, end):
        """
        Gets the interval name from start note to end note.

        :param start: The starting note.
        :param end: The ending note.
        :return: The interval name.
        :raises ValueError: If either the start or end note is invalid.
        """
        if start not in NOTES:
            raise ValueError(f"Invalid start note: {start}")
        if end not in NOTES:
            raise ValueError(f"Invalid end note: {end}")
        
        return INTERVALS[(NOTES.index(end) - NOTES.index(start)) % len(NOTES)]
    


    def get_wholeHalfSteps_from_halfSteps(self, distance):
        """
        Given the number of half steps, returns the representation in whole steps and half steps.

        :param number_of_half_steps: The number of half steps to convert.
        :return: A tuple (whole_steps, half_steps).
        :raises ValueError: If the distance is negative or not an integer.
        """
        if distance < 0 or not isinstance(distance, int):
            raise ValueError("Distance must be a non-negative integer")

        return divmod(distance, 2)
    def get_intervalName_from_halfSteps(self, distance):
        """
        Given a distance in half steps, return the appropriate interval.
        
        :param distance: The distance in half steps.
        :return: The interval corresponding to that distance.
        :raises ValueError: If the distance isn't between 0 and 12.
        """
        if distance > 12 or distance < 0:
            raise ValueError("Distance must be bounded between 0 and 12") 
        
        return INTERVALS[distance]
    


    def get_intervalNames_from_key(self, a_note):
        """
        Given a note, provides the interval name from the root key to that target note
        and from the target note to that root key.

        :param a_note: The note to check.
        :return: A tuple of intervals (forwards and backwards).
        :raises ValueError: If the note does not exist.
        """
        a_note = self.match_note(a_note)
        interval_to_target = self.get_intervalName_from_twoNotes(self.key, a_note)
        interval_to_root = self.get_intervalName_from_twoNotes(a_note, self.key)
        return interval_to_target, interval_to_root

    def get_note_from_halfSteps(self, number_of_halfSteps):
        """
        From the key and given a positive number of half steps, returns the note after # of half steps.
        From the key and given a negative number of half steps, returns the note before # half steps.

        :param number_of_halfSteps: The number of half steps to adjust.
        :return: The note resulting from the adjustment.
        :raises ValueError: If the half steps are not an integer.
        """
        if not isinstance(number_of_halfSteps, int):
            raise ValueError("The half steps must be an integer")
        
        note = NOTES[(NOTES.index(self.key) + number_of_halfSteps) % len(NOTES)]
        return note
    
    def get_halfSteps_from_intervalName(self,an_interval):
        """
        Given an interval, returns the half steps it corresponds to.

        :param an_interval: The name of the interval.
        :return: The number of half steps.
        :raises ValueError: If the interval does not exist.
        """
        if an_interval in INTERVALS.values():

            for half_step, interval in INTERVALS.items():
                if interval == an_interval:
                    return half_step
        else:
                raise ValueError(f"The interval {an_interval} does not exist ")

    def get_note_from_intervalName(self, an_interval, descending):
        """
        Given an interval, returns the note from that interval either ascending or descending.

        :param an_interval: The name of the interval.
        :param descending: A boolean indicating if the interval should be descending.
        :return: The resulting note.
        :raises ValueError: If the interval does not exist.
        """
        if an_interval in INTERVALS.values():
            value = [interval for interval, interval_name in INTERVALS.items() if interval_name == an_interval][0]
            note_from_interval = self.get_note_from_halfSteps(-1 * value if descending else value)
            return note_from_interval
        else:
            raise ValueError(f"The interval {an_interval} does not exist ")
        
    def scale_to_wholeHalf(self, scale, root_relative):
        """
        Converts a musical scale represented in half-steps from the root into the number of whole steps 
        and half-steps between each note.

        :param scale: The name of the scale to convert.
        :raises ValueError: If the scale does not exist.
        :return: A list of intervals represented as tuples of (whole_steps, half_steps).
        """
        if scale not in SCALES:
            raise ValueError(f"The scale {scale} does not exist")
        
        scale = SCALES[scale]
        
        if not root_relative:
            pairs = list(zip(scale[1:], scale[:-1]))
            relative_intervals = [self.get_wholeHalfSteps_from_halfSteps(abs(x[1] - x[0])) for x in pairs]
            return relative_intervals
        
        root_intervals = [self.get_wholeHalfSteps_from_halfSteps(x) for x in scale]
        return root_intervals
    
    def scale_to_intervalNames(self, scale, root_relative):
        """
        Converts a musical scale represented in half-steps from the root into the name of the intervals between
        each note.

        If root_relative is True, it returns the intervals relative to the root note, including the root itself.
        If False, it returns the interval names based on the differences between adjacent notes in the scale.

        :param scale: The name of the scale to convert.
        :raises ValueError: If the scale does not exist.

        :return: A list of intervals represented with their appropriate names between the notes.
        """
        if scale not in SCALES:
            raise ValueError(f"The scale {scale} does not exist")
        
        scale = SCALES[scale]
        
        if not root_relative:
            pairs = list(zip(scale[1:], scale[:-1]))
            relative_intervals = [INTERVALS[abs(x[1] - x[0])] for x in pairs]
            return relative_intervals
        
        root_intervals = [self.get_intervalName_from_halfSteps(x) for x in scale]
        
        return root_intervals
    
