# Based on the assembly code analysis of the deconstructed shellcode,
# this script reconstructs the flag directly as if the shellcode had been executed.

if __name__ == "__main__":
    pushedDWORDs = [
        b"\x93\xd8\x84\x84",
        b"\x90\xc3\xc6\x97",
        b"\xc3\x90\x93\x92",
        b"\x90\xc4\xc3\xc7",
        b"\x9c\x93\x9c\x93",
        b"\xc0\x9c\xc6\xc6",
        b"\x97\xc6\x9c\x93",
        b"\x94\xc7\x9d\xc1",
        b"\xde\xc1\x96\x91",
        b"\xc3\xc9\xc4\xc2",
    ]
    # Combine the DWORDs in reverse order to reconstruct the original byte sequence
    pushedBytes = b"".join(reversed(pushedDWORDs))
    decoded = bytes([b ^ 0xA5 for b in pushedBytes])
    print(decoded.decode())
