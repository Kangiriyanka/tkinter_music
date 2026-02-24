import unittest
from package.src.harmonica import Harmonica

class TestHarmonica(unittest.TestCase):

    def setUp(self):
        self.harmonica = Harmonica("D")


    def test_blow_valid(self):

        self.assertEqual(self.harmonica.blow(1), "D")
        self.assertEqual(self.harmonica.blow(2), "F#/Gb")
        self.assertEqual(self.harmonica.blow(3), "A")
    
    def test_blow_invalid(self):

        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.blow(11), "D")
        
        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.blow("1"), "D")


    def test_draw_valid(self):

        self.assertEqual(self.harmonica.draw(1), "E")
        self.assertEqual(self.harmonica.draw(2), "A")
        self.assertEqual(self.harmonica.draw(3), "C#/Db")

    def test_draw_invalid(self):

        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.draw(-2), "D")
        
        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.blow("nothing"), "D")


    def test_bend_valid(self):

     self.assertEqual(self.harmonica.bend(1,1), "D#/Eb")
     self.assertEqual(self.harmonica.bend(2,1), "G#/Ab")
     self.assertEqual(self.harmonica.bend(2,2), "G")
     self.assertEqual(self.harmonica.bend(3,1), "C")
     self.assertEqual(self.harmonica.bend(3,2), "B")
     self.assertEqual(self.harmonica.bend(3,3), "A#/Bb")
     self.assertEqual(self.harmonica.bend(4,1), "D#/Eb")
     self.assertEqual(self.harmonica.bend(6,1), "A#/Bb")
     

    
    def test_bend_invalid(self):

        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.bend(-2,0), "D")
        
        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.bend(2,"1"), "D")
        
        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.bend(3,4), "D")

        with self.assertRaises(KeyError):
         self.assertEqual(self.harmonica.bend(5,1), "D")

    def test_blowbend_valid(self):
      
      self.assertEqual(self.harmonica.blowbend(8,1), "F")
      self.assertEqual(self.harmonica.blowbend(9,1), "G#/Ab")
      self.assertEqual(self.harmonica.blowbend(10,1), "C#/Db")
      self.assertEqual(self.harmonica.blowbend(10,2), "C")


      

    def test_blowbend_invalid(self):

        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.blowbend(-2,0), "D")

        
        with self.assertRaises(ValueError):
         self.assertEqual(self.harmonica.blowbend(8,3), "D")
    
        
        with self.assertRaises(KeyError):
         self.assertEqual(self.harmonica.blowbend(3,2), "D")
        

    def test_overblow_valid(self):
      
        self.assertEqual(self.harmonica.overblow(4), "F")
        self.assertEqual(self.harmonica.overblow(5), "G#/Ab")
        self.assertEqual(self.harmonica.overblow(6), "C")
      

    def test_overblow_invalid(self):
      
     with self.assertRaises(KeyError):
       
        self.assertEqual(self.harmonica.overblow(3), "D")

     with self.assertRaises(KeyError):

        self.assertEqual(self.harmonica.overblow(7), "A")
    
     with self.assertRaises(KeyError):

        self.assertEqual(self.harmonica.overblow(9), "A")
       


    def test_overdraw_valid(self):

        self.assertEqual(self.harmonica.overdraw(7), "D#/Eb")
        self.assertEqual(self.harmonica.overdraw(9), "A#/Bb")
        self.assertEqual(self.harmonica.overdraw(10), "D#/Eb" )


    def test_ovedraw_invalid(self):
      
     with self.assertRaises(KeyError):
       
        self.assertEqual(self.harmonica.overdraw(3), "D")

     with self.assertRaises(KeyError):

        self.assertEqual(self.harmonica.overdraw(8), "A")
    
     with self.assertRaises(KeyError):

        self.assertEqual(self.harmonica.overdraw(6), "A")
       




       


       


    
       
       



    
