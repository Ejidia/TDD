
from calculator import calculate_tax
def test_calculate_tax():
    # Test: No tax for earnings less than 12,000
      assert calculate_tax(10000) == 0

def test_calculate_twenty_tax():
    # Test: 20% tax for earnings exactly 12,000
      assert calculate_tax(12000) == 2400
    
    # Test: 20% tax for earnings between 12,000 and 36,000
      assert calculate_tax(25000) == 5000
    # Test: 20% tax for earnings exactly 36,000
      assert calculate_tax(36000) == 7200

def test_calculate_forty_tax():
    # Test: 40% tax for earnings above 36,000
      assert calculate_tax(40000) == 16000

# Run tests
#test_calculate_tax()
#print("All tests passed!")
