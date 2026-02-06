# test_deployspectra.py
"""
Tests for deploySpectra module.
"""

import unittest
from deployspectra import deploySpectra

class TestdeploySpectra(unittest.TestCase):
    """Test cases for deploySpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = deploySpectra()
        self.assertIsInstance(instance, deploySpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = deploySpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
