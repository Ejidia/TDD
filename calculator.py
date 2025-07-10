def calculate_tax(earnings):
    # If the earnings are less than 12,000, no tax is applied
    if earnings < 12000:
        return 0

    # If the earnings are between 12,000 and 36,000 (inclusive),
    # a 20% tax is applied to the entire amount
    elif earnings <= 36000:
        tax = 0.2 * (earnings - 12000)


    # If the earnings are greater than 36,000,
    # a 40% tax is applied to the entire amount
    else:
        tax = 0.4 * (earnings - 36000) + 0.2 * (36000 - 12000)

    return tax
