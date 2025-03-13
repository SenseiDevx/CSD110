def string_to_number(s: str) -> int:
    result = 0
    for i in s:
        if '0' <= i <= '9':
            result = result * 10 + (ord(i) - ord('0'))
        else:
            raise ValueError(f"Invalid character '{i}' in string")
    return result


print(string_to_number("12345"))
print(string_to_number("007"))
