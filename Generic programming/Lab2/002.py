str1 = "X-DSPAM-Confidence:0.8475"

colon = str1.find(":")
number_str = str1[colon + 1:]
number_str = number_str.strip()

float_value = float(number_str)
print(f"The extracted floating pont number is: {float_value}")