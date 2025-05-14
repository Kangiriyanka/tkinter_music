from .key import Key
from .harmonica import Harmonica
from .chord import Chord

def main():

  key = input("Choose a key: ")
  key = Key(key)
  chords = Chord(key)
  harmonica = Harmonica(key)
  print(harmonica.generate_layout())
 


  


 
 
if __name__ == "__main__":
    main()




    

    
