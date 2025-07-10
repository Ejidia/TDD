
from calculator import calculate_tax
def test_calculate_tax():
    # Test: No tax for earnings less than 12,000
      assert calculate_tax(10000) == 0

def test_calculate_twenty_tax():
      assert calculate_tax(12100) == 20

def test_calculate_36000_tax():
      assert calculate_tax(36000) == 4800

def test_calculate_36100_tax():
      assert calculate_tax(36100) == 4840

def test_calculate_120000_tax():
      assert calculate_tax(120000) == 38400

    
