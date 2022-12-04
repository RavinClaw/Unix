import os

def decoder(binaryfile: str, outputfile: str):
	if os.path.exists(binaryfile):
		with open(binaryfile, 'r') as file:
			filedata = file.read()
		binary_int = int(filedata, 2);
		byte_number = binary_int.bit_length() + 7 // 8
		binary_array = binary_int.to_bytes(byte_number, 'big')
		ascii_text = binary_array.decode()
		print(ascii_text)
		with open(outputfile, 'w') as file:
			file.write(ascii_text)
		return
	else:
		return

def encoder(inputfile: str, outputfile: str):
	with open(inputfile, 'r') as file:
		value = file.read()
	byte_array = value.encode()
	binary_int = int.from_bytes(byte_array, 'big')
	binary_string = bin(binary_int)
	with open(outputfile, 'w') as file:
		file.write(binary_string)
	return binary_string
