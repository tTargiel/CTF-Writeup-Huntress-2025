# Huntress CTF 2025 - 👶 Just a Tiny Bit  

**CTF Name:** Huntress CTF 2025  
**Challenge name:** 👶 Just a Tiny Bit  
**Challenge prompt:**  
> If just a little bit were to go missing... would it really even matter?  

**Challenge category:** Warmups  
**Challenge points:** 10  

* * *  

## Steps to solve  

Given binary:  

```  
11001101101100110000111001111111011011001011000110110011011001111000110110001011011001110011100001  
11001011100010110010011001100110010110010111001010110011011000111001010110011011100001110010110101  
1100100011010101110010110110011011011001000111001011001111001101111101  
```  

Flag should be in the following format as per what was written in the CTF rules `Flags for this competition will follow the format: `flag\{[0-9a-f]{32}\}.`  

That means we are looking for 38 characters, 8 bits per character - in total 304 bits.  

Currently we have 268 bits. 36 missing.  

I discovered that every 8th bit is missing, as:  
`f` in binary is `01100110`, but only `1100110` can be found  
`l` in binary is `01101100`, but only `1101100` can be found.  

you get the drill...  

I used the following Python-script to recover the flag (it can also be found in the `./Just a Little Bit/` directory):  

```python  
import sys  

def binary_file_to_text(input_file, output_file=None):  
    data = input_file.replace('\n', '').replace(' ', '')  
    # Split into 7-bit chunks  
    binary_data = [data[i:i+7] for i in range(0, len(data), 7) if len(data[i:i+7]) == 7]  
    # Prepend "0" to each chunk  
    text = ''.join([chr(int('0' + b, 2)) for b in binary_data])  
    if output_file:  
        with open(output_file, 'w') as out:  
            out.write(text + '\n')  
    else:  
        print(text)  

if __name__ == "__main__":  
    if len(sys.argv) < 2:  
        print("Usage: python justALittleBit.py <binary_file> [output_file]")  
    else:  
        with open(sys.argv[1], 'r') as f:  
            data = f.read()  
        binary_file_to_text(data, sys.argv[2] if len(sys.argv) > 2 else None)  
```  

![ad6ab15ac8af.png](../assets/ad6ab15ac8af.png)  

**FLAG:** flag{2c33c169aebdf2ee31e3895d5966d93f}  
