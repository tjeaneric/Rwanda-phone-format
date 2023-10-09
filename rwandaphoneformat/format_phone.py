

class FormatPhone:
    def __init__(self, phone_number: str) -> None:
        if len(phone_number) < 9:
            raise ValueError("Phone number must be greater than or equal to 9 characters")
        self.phone_number = phone_number.strip()

    def in_250_format(self) -> str:
        phone_number = self.phone_number
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
