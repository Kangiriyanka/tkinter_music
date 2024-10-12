BLOW_NOTES = ["Perfect Unison", "Major 3rd", "Perfect 5th"] * 3 + ["Perfect Unison"]
DRAW_NOTES = ["Major 2nd", "Perfect 5th", "Major 7th", "Major 2nd", "Perfect 4th", 
              "Major 6th", "Major 7th", "Major 2nd", "Perfect 4th", "Major 6th"]

class Harmonica:
    def __init__(self, key):
        """
        Initializes the Harmonica object corresponding to the given key.
        
        :param key: The root note of the harmonica.
        """
        self.key = key
        self.layout = self.generate_layout()

    def print_layout(self):
        """
        Prints the layout of the harmonica in a readable format.
        """
        for hole, notes in self.layout.items():
            print(f"Hole {hole}:")
            print(f"  Blow: {notes['blow']}")
            print(f"  Draw: {notes['draw']}")
            if 'bend' in notes:
                print(f"  Bend: {', '.join(notes['bend'])}")
            if 'blowbend' in notes:
                print(f"  Blow Bend: {', '.join(notes['blowbend'])}")
            if 'overblow' in notes:
                print(f"  Overblow: {', '.join(notes['overblow'])}")
            if 'overdraw' in notes:
                print(f"  Overdraw {', '.join(notes['overdraw'])}")
            print("")  # Print a new line for better readabilityxw

    def generate_layout(self):
        """
        Generates the layout of the harmonica based on the blow and draw notes.

        :return: A dictionary representing the layout of the harmonica.
        """
        harmonica = {}
        blow_notes = [self.key.get_note_from_intervalName(interval, False) for interval in BLOW_NOTES]
        draw_notes = [self.key.get_note_from_intervalName(interval, False) for interval in DRAW_NOTES]

        # Fill the harmonica with the basic blow and draw notes
        # The first hole i.e. key is supposed to be 1, therefore we start at 1 our loop
        for i in range(1, 11):
            harmonica[i] = {"blow": blow_notes[i - 1], "draw": draw_notes[i - 1]}

        # Add the bends on holes 1,2,3,4,6
        harmonica[1]["bend"] = [self.key.flatten(draw_notes[0],1)]
        harmonica[2]["bend"] = [self.key.flatten(draw_notes[1], i) for i in range(1,3)]  
        harmonica[3]["bend"] = [self.key.flatten(draw_notes[2],i) for i in range(1,4)]
        harmonica[4]["bend"] = [self.key.flatten(draw_notes[3],1)]
        harmonica[6]["bend"] = [self.key.flatten(draw_notes[5],1)]

        # Add blow bend on holes 8,9,10

        harmonica[8]["blowbend"] = [self.key.flatten(blow_notes[7],1)]
        harmonica[9]["blowbend"] = [self.key.flatten(blow_notes[8],1)]
        harmonica[10]["blowbend"] = [self.key.flatten(blow_notes[9], i) for i in range(1,3)]  

        # Adding overblows

        harmonica[1]["overblow"] = [harmonica[8]["blowbend"][0]]
        harmonica[4]["overblow"] = [harmonica[8]["blowbend"][0]]
        harmonica[5]["overblow"] = [harmonica[9]["blowbend"][0]]
        harmonica[6]["overblow"] = [self.key.flatten((harmonica[10]["blowbend"][0]),1)]

        # Adding overdraws

        harmonica[7]["overdraw"] = [harmonica[4]["bend"][0]]
        harmonica[9]["overdraw"] = [harmonica[6]["bend"][0]]
        harmonica[10]["overdraw"] = [harmonica[4]["bend"][0]]

        
        return harmonica
    


    def blow(self, hole):
        """
        Returns the blow note for the specified hole.

        :param hole: The hole number on the harmonica (1-10).
        :return: The blow note for the specified hole.
        """

        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
         raise ValueError("Hole number must be an integer between 1 and 10.")
        return self.layout[hole]["blow"]

    def draw(self, hole):
        """
        Returns the draw note for the specified hole.

        :param hole: The hole number on the harmonica (1-10).
        :return: The draw note for the specified hole.
        """

        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
          raise ValueError("Hole number must be between 1 and 10.")
        return self.layout[hole]["draw"]
    
    def bend(self, hole, degree):

        """
        Returns the bended note for the specified draw hole.
        These bends are specific to each hole, holess such as 1 and 6 do not have a draw bend of the 2nd degree

        :param hole: The hole number on the harmonica (1-10).
        :param degree: Number representing # half steps under the note
        :return: The bend note for the specified hole.
        """

        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
          raise ValueError("Hole number must be between 1 and 10.")
        
        if not isinstance(degree,int) or degree < 1  or degree > 3 :
          raise ValueError("Bends must be between 1 and 3 .")
        
        try:
            return self.layout[hole]["bend"][degree - 1]
    
        except IndexError:
            raise IndexError(f"Hole {hole} does not have a bend at {degree} half-steps below .")
        
        
        except KeyError:
            raise KeyError(f"Hole {hole} doesn't have any bends ")
        
    def blowbend(self, hole, degree):

        """
        Returns the bended note for the specified blow hole.
        These blowbends are specific to each hole. 

        :param hole: The hole number on the harmonica (1-10).
        :param degree: Number representing # half steps under the note
        :return: The bend note for the specified hole.
        """

        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
          raise ValueError("Hole number must be between 1 and 10.")
        
        if  not isinstance(degree,int)  or degree < 1  or degree > 2 :
          raise ValueError("Blowbends must be between 1 and 2 .")
        
        try:
            return self.layout[hole]["blowbend"][degree - 1]
    
        except IndexError:
            raise IndexError(f"Hole {hole} does not have a blowbend at {degree} half-steps below .")
        
        except KeyError:
            raise KeyError(f"Hole {hole} doesn't have any blowbends ")
        
    def overblow(self, hole):

        """
        Returns the overblow for the specified blow hole.
        Overblows are specific to some holes on the harmonica. 

        :param hole: The hole number on the harmonica (1-10).
        :param degree: Number representing # half steps under the note
        :return: The bend note for the specified hole.
        """

        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
          raise ValueError("Hole number must be between 1 and 10.")
   
        
        try:
            return self.layout[hole]["overblow"][0]
    
        except KeyError:
            raise KeyError(f"Hole {hole} does not have an overblow.")
        

    def overdraw(self,hole):
       
        if not isinstance(hole,int) or  hole < 1 or hole > 10 :
          raise ValueError("Hole number must be between 1 and 10.")
   
        
        try:
            return self.layout[hole]["overdraw"][0]
    
        except KeyError:
            raise KeyError(f"Hole {hole} does not have an overdraw.")
       

       

  




    
   