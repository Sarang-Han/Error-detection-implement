
# HW3 Part2: Error detection code implementation using shift-register
# Flexible Generator implemented

def crc_shift_register(data, generator):

    data_bits = [int(bit) for bit in data.split()]  # Convert data string to a list of integers
    generator_bits = [int(bit) for bit in generator.split()]  # Convert generator string to a list of integers

    crc_len = len(generator_bits) - 1 # CRC bit length calculation (generator length - 1)
    crc_register = [0] * crc_len # CRC register initialization with zeros
    initial_codeword = data_bits + crc_register # Initial codeword (data bits + CRC register)

    # CRC logic implementation
    for bit_index in range(len(initial_codeword)):
        
        # Calculate the next CRC register value by shifting and appending the current bit
        next_crc_register = crc_register[1:] + [initial_codeword[bit_index]]

        # Check the Most Significant Bit (MSB) of the current CRC register
        if crc_register[0]:
            # XOR with the generator polynomial (excluding the top bit) if MSB is 1
            next_crc_register = list_xor(next_crc_register, generator_bits[1:])

        # Update the CRC register with the XOR result
        crc_register = next_crc_register

    # Final CRC value calculation (the CRC is now in the register)
    crc = crc_register

    # Codeword generation (data + CRC)
    codeword = data_bits + crc

    # Convert lists to strings of 0s and 1s with spaces
    crc_string = " ".join(map(str, crc))  # Convert CRC list to a string with spaces
    codeword_string = " ".join(map(str, codeword))  # Convert codeword list to a string with spaces

    return crc_string, codeword_string # Return result as a tuple

def crc_shift_register2(codeword, generator):

  codeword_bits = [int(bit) for bit in codeword.split()]  # Convert codeword string to a list of integers
  generator_bits = [int(bit) for bit in generator.split()]  # Convert generator string to a list of integers
  crc_len = len(generator_bits) - 1 # CRC bit length calculation (generator length - 1)
  crc_register = [0] * crc_len # CRC register initialization

  # Append CRC register to codeword for processing
  initial_codeword = codeword_bits + crc_register

  # Perform CRC calculation
  for bit_index in range(len(initial_codeword)):
    next_crc_register = crc_register[1:] + [initial_codeword[bit_index]]
    if crc_register[0]:
      next_crc_register = list_xor(next_crc_register, generator_bits[1:])
    crc_register = next_crc_register

  # Final CRC value is in the CRC register
  crc = crc_register

  return crc # Return result

def crc_check(codeword, generator):
  
  # Call crc_shift_register2 for calculation
  crc = crc_shift_register2(codeword, generator)

  # Check if CRC is all zeros (no error)
  if all(bit == 0 for bit in crc):
    print("No error detected")
  else:
    print("An error is detected")

# Helper function for XOR operation (assuming it's not built-in)
def list_xor(list1, list2):
  return [a ^ b for a, b in zip(list1, list2)]


# This function checks for errors in the received codeword using the CRC value.
def crc_check(codeword, generator):
    
  # Call crc_shift_register2 to calculate the CRC value of the received codeword
  crc = crc_shift_register2(codeword, generator)

  # Check if all CRC bits are zero. If so, no error is detected.
  if all(bit == 0 for bit in crc):
    print("No error is detected! (according to generator)")
  else:
    print("An error is detected! (according to generator)")

# This function implements the main logic for Part II of Homework #3, including the TX and RX modes.
def hw3_part2():
  
  print("[HW #3 Part II] Student ID: 2271064 Name: Sarang Han")

  while True:
    mode = input("Select the mode between TX and RX (TX:1, RX:2): ")

    if mode == "1": # TX mode: Send data
      data = input("Type information bits that you want to send: ")
      generator = input("Type generator bits: ")
      crc, codeword = crc_shift_register(data, generator)
      print("CRC bits calculated by Generator:", crc)
      print("The complete codeword:", codeword)
      print("done...")

    elif mode == "2": # RX mode: Receive data and check for errors
      codeword = input("Type the codeword that RX received: ")
      generator = input("Type generator bits: ")
      crc_check(codeword, generator)
      print("Done...")

    else:
      print("Invalid selection. Please select 1 or 2.")

    # Ask if you want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
      break

# Test
hw3_part2()