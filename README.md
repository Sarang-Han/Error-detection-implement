## CRC Error Detection Implementation Project

This project implements a CRC (Cyclic Redundancy Check) based error detection system using Shift Register in Python.

Detailed report can be found [here](https://github.com/Sarang-Han/Error-detection-implement/blob/main/Error%20Detection%20Implement%20Report.pdf).
<br><br>

## Features

- **Transmitter (TX) Mode**: Calculate CRC by receiving data and generator polynomial
- **Receiver (RX) Mode**: Detect errors in received codewords
<br><br>

## Implementation Details

- `crc_shift_register()`: Calculate CRC and generate codeword in TX mode
- `crc_shift_register2()`: Calculate CRC for error detection in RX mode
- `crc_check()`: Verify errors in received codewords
<br><br>

## How to Use

1. **TX Mode (Option 1)**:
   - Enter information bits
   - Enter generator polynomial
   - Confirm CRC bits and complete codeword

2. **RX Mode (Option 2)**:
   - Enter received codeword
   - Enter generator polynomial
   - Check error detection results
<br><br>

## Execution Results

![CRC Error Detection Execution Results](https://github.com/user-attachments/assets/4436beb0-0770-4978-bd2c-b8d2ff5d90ff)

## How to Run

```bash
python HW3_part2.py
```
<br><br>
