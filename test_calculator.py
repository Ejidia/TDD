def calculate_tax(earnings):
    """
    Calculate tax based on given earnings using specified brackets:
    - Earnings < 12,000: No tax
    - 12,000 <= Earnings <= 36,000: 20% tax
    - Earnings > 36,000: 40% tax
    """
    # If earnings are less than 12,000, no tax is owed
    if earnings < 12000:
        return 0
    # If earnings are between 12,000 and 36,000 (inclusive), tax is 20%
    elif earnings <= 36000:
        return earnings * 0.20
    # If earnings are greater than 36,000, tax is 40%
    else:
        return earnings * 0.40

# Test cases to verify the function works as expected
def test_calculate_tax():
    # Test: No tax for earnings less than 12,000
    assert calculate_tax(10000) == 0
    # Test: 20% tax for earnings exactly 12,000
    assert calculate_tax(12000) == 2400
    
    # Test: 20% tax for earnings between 12,000 and 36,000
    assert calculate_tax(25000) == 5000
    # Test: 20% tax for earnings exactly 36,000
    assert calculate_tax(36000) == 7200
    # Test: 40% tax for earnings above 36,000
    assert calculate_tax(40000) == 16000

# Run tests
#test_calculate_tax()
#print("All tests passed!")
