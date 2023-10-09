def in_250_format(phone_number: str) -> str:
    phone_number = phone_number.strip()
    if len(phone_number) < 9:
        raise ValueError("Phone number must be greater than or equal to 9 characters")
    first_three, first_two = phone_number[0:3], phone_number[0:2]
    phone_number_length = len(phone_number)
    if phone_number_length == 9 and phone_number.startswith("7"):
        phone = f"250{phone_number}"
    elif first_three == "+25":
        phone = phone_number.lstrip("+")
    elif first_two == "07":
        phone = f"25{phone_number}"
    else:
        phone = phone_number
    return phone
