line = "50, 50, 8.5509906, 39.3109560, 2021-12-23 00:07:54"

line_to_list = line.split(",")

line_to_list = [item.strip() for item in line_to_list]

line_to_list = tuple(line_to_list)

# print(line_to_list)


# str_to_hex = "{:x}".format(int(line))

s = line.encode("utf-8")
str_to_hex = s.hex()
print(str_to_hex)

hex_to_str = bytes.fromhex(str_to_hex).decode("utf-8")

print(hex_to_str)
