import random

from string import ascii_lowercase, digits


def genarate_nam_files(ext, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count=6):
    for _ in range(count):
        file_nam = "".join(random.choices(ascii_lowercase + digits, k=random.randint(min_len_name, max_len_name)))
        byte_size = bytes(random.randint(0, 255) for i in range(random.randint(min_byte, max_byte)))
        with open(f"{file_nam}.{ext}", "wb") as file:
            file.write(byte_size)


genarate_nam_files("txt")
