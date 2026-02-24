import unittest
from package.src.key import Key 
from package.src.chord import Chord

class TestChords(unittest.TestCase):

    def setUp(self):
        """Set up a Chord instance for testing."""
        key= Key("A")
        self.chords = Chord(key)
    

    def test_get_randomChords_valid(self):

        self.assertEqual(self.chords.get_majorChord(), ["A", "C#/Db", "E"])
        self.assertEqual(self.chords.get_minorChord(), ["A", "C", "E"])
        self.assertEqual(self.chords.get_diminished_7thChord(), ["A", "C", "D#/Eb", "F#/Gb"])
        self.assertEqual(self.chords.get_augmentedChord(), ["A", "C#/Db", "F"])
        self.assertEqual(self.chords.get_major_7thChord(), ["A", "C#/Db", "E", "G#/Ab"])
        self.assertEqual(self.chords.get_dominant_7thChord(), ["A", "C#/Db", "E", "G"])
        self.assertEqual(self.chords.get_minor_7thChord(), ["A", "C", "E", "G"])
        self.assertEqual(self.chords.get_half_diminished_7thChord(), ["A", "C", "D#/Eb", "G"])
        self.assertEqual(self.chords.get_minor_major_7thChord(), ["A", "C", "E", "G#/Ab"])
        self.assertEqual(self.chords.get_augmented_7thChord(), ["A", "C#/Db", "F", "G"])
     


    if __name__ == '__main__':
        unittest.main()

    