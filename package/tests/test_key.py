import unittest
from key import Key  
from constants import SCALES, NOTES, INTERVALS 

# Add test infront of each test function

class TestKey(unittest.TestCase):

    def setUp(self):
        """Set up a Key instance for testing."""
        self.key = Key("C")  
        

    def test_match_note_valid(self):
        """Test matching a valid note."""
        self.assertEqual(self.key.match_note("C#"), "C#/Db") 
        self.assertEqual(self.key.match_note("D"), "D")

    def test_match_note_invalid(self):
        """Test matching an invalid note."""
        with self.assertRaises(ValueError):
            self.key.match_note("X")  

    def test_generate_mode_valid(self):
        """Test generating a valid mode."""
        major_scale = ["C","D","E","F","G","A","B"]

        expected_mode = major_scale[1:] + major_scale[:1]  
        self.assertEqual(self.key.generate_mode("Dorian"), expected_mode)

    def test_generate_mode_invalid(self):
        """Test generating an invalid scale."""
        with self.assertRaises(ValueError):
            self.key.generate_mode("Durian")

    def test_generate_scale_valid(self):
        """Test generating a valid scale."""
        expected_scale = ["C","D","E","F","G","A","B"]
        self.assertEqual(self.key.generate_scale("Major"), expected_scale)
    

    def test_generate_scale_invalid(self):
        """Test generating an invalid scale."""
        with self.assertRaises(ValueError):
            self.key.generate_scale("InvalidScale")

    def get_degrees_from_intervals_valid(self):

        self.assertEqual(self.key.get_degrees_from_intervals(["Perfect Unison", "Major 2nd", "Major 3rd"], ["1","2","3"]))
        self.assertEqual(self.key.get_degrees_from_intervals(["Perfect 4th"], ["4"]))

    def get_degrees_from_intervals_invalid(self):

        with self.assertRaises(ValueError):
            self.assertEqual(self.key.get_degrees_from_intervals(["Perfect Unison", "Major 2nd", "Majorre 3rd"], ["1","2","3"]))

    def test_get_intervalName_from_twoNotes_valid(self):
        """Test getting the interval name between two notes."""
        self.assertEqual(self.key.get_intervalName_from_twoNotes("C", "E"), "Major 3rd")  # Adjust according to INTERVALS
        self.assertEqual(self.key.get_intervalName_from_twoNotes("E", "C"), "Minor 6th")

    def test_get_intervalName_from_twoNotes_invalid(self):
        """Test getting the interval name between two notes."""
        with self.assertRaises(ValueError):
            self.key.get_intervalName_from_twoNotes("C","O")

    def test_get_intervalName_from_halfSteps_valid(self):
        self.assertEqual(self.key.get_intervalName_from_halfSteps(11),"Major 7th" )
        self.assertEqual(self.key.get_intervalName_from_halfSteps(0), "Perfect Unison" )
    
    def test_get_intervalName_from_halfSteps_invalid(self):
        """Test getting the interval name between two notes."""
        with self.assertRaises(ValueError):
            self.key.get_intervalName_from_halfSteps(-1)
        with self.assertRaises(ValueError):
            self.key.get_intervalName_from_halfSteps(13)

    def test_get_wholeHalfSteps_from_halfSteps_valid(self):

        self.assertEqual(self.key.get_wholeHalfSteps_from_halfSteps(5), (2,1))
        self.assertEqual(self.key.get_wholeHalfSteps_from_halfSteps(12), (6,0))
        self.assertEqual(self.key.get_wholeHalfSteps_from_halfSteps(9), (4,1))

    def test_get_wholeHalfSteps_from_halfSteps_invalid(self):

        with self.assertRaises(ValueError):
            self.key.get_wholeHalfSteps_from_halfSteps(-3)

        with self.assertRaises(ValueError):
            self.key.get_wholeHalfSteps_from_halfSteps(3.1)

    def test_get_intervalNames_from_key_valid(self):

        self.assertEqual(self.key.get_intervalNames_from_key("A"), ("Major 6th", "Minor 3rd"))
    
    def test_get_intervalNames_from_key_invalid(self):

        with self.assertRaises(ValueError):
            self.key.get_intervalNames_from_key("X")

    def test_get_note_from_halfSteps_valid(self):

        self.assertEqual(self.key.get_note_from_halfSteps(4), "E")
        # With this test, G#/Ab is required due to the initial representation of NOTES
        self.assertEqual(self.key.get_note_from_halfSteps(-4), "G#/Ab")
        self.assertEqual(self.key.get_note_from_halfSteps(12), "C")
        self.assertEqual(self.key.get_note_from_halfSteps(-14), "A#/Bb")
    
    def test_get_note_from_halfSteps_invalid(self):

        with self.assertRaises(ValueError):
            self.key.get_note_from_halfSteps(3.5)


    def test_get_halfSteps_from_intervalName_valid(self):
   
        for half_step, interval in INTERVALS.items():
            self.assertEqual(self.key.get_halfSteps_from_intervalName(interval), half_step)
    
    
    def test_get_note_from_intervalName_valid(self):

        self.assertEqual(self.key.get_note_from_intervalName("Major 6th",False), "A")
        self.assertEqual(self.key.get_note_from_intervalName("Major 2nd",True), "A#/Bb")
        self.assertEqual(self.key.get_note_from_intervalName("Minor 7th",True), "D")
        self.assertEqual(self.key.get_note_from_intervalName("Minor 7th",False), "A#/Bb")
        self.assertEqual(self.key.get_note_from_intervalName("Perfect Unison",False), "C")
    
    def test_get_note_from_intervalName_invalid(self):

        with self.assertRaises(ValueError):
        
            self.key.get_note_from_intervalName("Majore 4st", False)


    def test_scale_to_intervalNames_valid(self):

        self.assertEqual(self.key.scale_to_intervalNames("Major", True), ["Perfect Unison", "Major 2nd", "Major 3rd", "Perfect 4th", "Perfect 5th", "Major 6th","Major 7th" ])
        self.assertEqual(self.key.scale_to_intervalNames("Major", False), ["Major 2nd", "Major 2nd", "Minor 2nd", "Major 2nd", "Major 2nd", "Major 2nd"])
        self.assertEqual(self.key.scale_to_intervalNames("Minor Blues", True), ["Perfect Unison", "Minor 3rd", "Perfect 4th", "Tritone", "Perfect 5th", "Minor 7th"])
        self.assertEqual(self.key.scale_to_intervalNames("Minor Blues", False), ["Minor 3rd", "Major 2nd", "Minor 2nd", "Minor 2nd", "Minor 3rd"])

    def test_scale_to_intervalNames_invalid(self):

        with self.assertRaises(ValueError):
            self.key.scale_to_intervalNames("Green's Sale", False)

    def test_scale_to_wholeHalf_valid(self):

        self.assertEqual(self.key.scale_to_wholeHalf("Minor",True), [(0,0), (1,0), (1,1), (2,1), (3,1),(4,0), (5,0)] )
        self.assertEqual(self.key.scale_to_wholeHalf("Minor",False), [(1,0), (0,1), (1,0), (1,0), (0,1), (1,0)] )
        self.assertEqual(self.key.scale_to_wholeHalf("Minor Pentatonic",True), [ (0,0), (1,1), (2,1), (3,1), (5,0)] )
        self.assertEqual(self.key.scale_to_wholeHalf("Minor Pentatonic",False), [ (1,1), (1,0), (1,0), (1,1)] )
       

if __name__ == '__main__':
    unittest.main()