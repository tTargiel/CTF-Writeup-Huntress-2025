if __name__ == "__main__":
    with open("AYGIW.tmp", "r") as f:
        content = f.read()
        byte_array = bytearray(content, "utf-8")
        with open("output.bin", "wb") as f:
            f.write(byte_array)