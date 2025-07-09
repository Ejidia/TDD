def calculate_tax(earnings):
    if earnings < 12000:
        return 0
    elif earnings <= 36000:
        return 0.2 * earnings
    else:
        return 0.4 * earnings
