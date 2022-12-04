class __2337__: # The Library required for vmc.py
    def decoder(binaryfile: str):
        if os.path.exists(binaryfile):
            with open(binaryfile, "r") as file:
                filedata = file.read()
            binary_int = int(filedata, 2);
            byte_number = binary_int.bit_length() + 7 // 8
            binary_array = binary_int.to_bytes(byte_number, "big")
            ascii_text = binary_array.decode()
            return ascii_text
        else:
            return
