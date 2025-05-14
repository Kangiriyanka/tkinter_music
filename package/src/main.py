from .key import Key
from .harmonica import Harmonica
from .chord import Chord

def main():

  key = input("Choose a key: ")
  key = Key(key)
  chords = Chord(key)
  harmonica = Harmonica(key)
 
  harmonica.generate_1st_position_scale("Major Pentatonic")



  


 
 
if __name__ == "__main__":
    main()




    

    
