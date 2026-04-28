def currency_conversion(amount : float)-> float:
    # conversion rate from USD to INR
    conversion_rate = 82.0
    return amount * conversion_rate

# Example usage
usd_amount = 100.0
inr_amount = currency_conversion(usd_amount)
print(inr_amount)