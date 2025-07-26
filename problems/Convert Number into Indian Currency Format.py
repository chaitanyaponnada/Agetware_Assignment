def format_indian_currency(number):
    number = str(number)
    if '.' in number:
        int_part, dec_part = number.split('.')
    else:
        int_part, dec_part = number, ""

    if len(int_part) <= 3:
        formatted = int_part
    else:
        last3 = int_part[-3:]
        int_part = int_part[:-3]
        parts = []
        while len(int_part) > 2:
            parts.insert(0, int_part[-2:])
            int_part = int_part[:-2]
        if int_part:
            parts.insert(0, int_part)
        formatted = ",".join(parts) + "," + last3

    if dec_part:
        formatted += "." + dec_part
    return formatted

print(format_indian_currency(123456.7891))  
