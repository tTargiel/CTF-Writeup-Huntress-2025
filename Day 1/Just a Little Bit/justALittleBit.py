import sys


def binary_file_to_text(input_file, output_file=None):
    data = input_file.replace("\n", "").replace(" ", "")
    # Split into 7-bit chunks
    binary_data = [
        data[i : i + 7] for i in range(0, len(data), 7) if len(data[i : i + 7]) == 7
    ]
    # Prepend "0" to each chunk
    text = "".join([chr(int("0" + b, 2)) for b in binary_data])
    if output_file:
        with open(output_file, "w") as out:
            out.write(text + "\n")
    else:
        print(text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python justALittleBit.py <binary_file> [output_file]")
    else:
        with open(sys.argv[1], "r") as f:
            data = f.read()
        binary_file_to_text(data, sys.argv[2] if len(sys.argv) > 2 else None)
