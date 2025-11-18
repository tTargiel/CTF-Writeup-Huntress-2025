# Huntress CTF 2025 - 🐞 NetSupport  

**CTF Name:** Huntress CTF 2025  
**Challenge name:** 🐞 NetSupport  
**Challenge prompt:**  
> An unexpected Remote Monitoring and Management (RMM) tool was identified on this laptop. We identified a suspicious PowerShell script written to disk at a similar time. Can you find the link between the two?

```
NOTE

The password to the ZIP archive is "netsupport".
```

**Challenge category:** Malware  
**Challenge points:** 10

* * *  

## Steps to solve  

In this challenge, we were provided with a single script file upon downloading and extracting the initial archive. 

Upon initial analysis of the script, a large, obfuscated line was immediately apparent. It defined a byte array in PowerShell, a common technique for hiding malicious or secondary payloads within a script file to evade static analysis.

The line began as follows:

```powershell
[Byte[]]$xϞzzghϞ = @(80,75 ...
```

To extract this embedded data, I used `grep` to isolate the line containing the byte array and redirected the output to a file for easier handling:

```bash
grep "@" netsupport > out.txt
```

With the decimal values extracted, I used CyberChef to process them. After cleaning the input to leave only the comma-separated numbers, the "From Decimal" operation converted the byte array back into its original binary form, which revealed it was a ZIP archive. 

After saving and extracting the contents of this new ZIP archive, a directory containing numerous files was created. I used `grep` to recursively search for the string "flag" across all the files in the directory:

```bash
grep -ir "flag" ./
```

This command quickly identified a promising entry within the `CLIENT32.ini` file. The file contained a `Flag` parameter with a base64 encoded string:

```ini
Flag=ZmxhZ3tiNmU1NGQwYTBhNWYyMjkyNTg5YzM4NTJmMTkzMDg5MX0NCg==
```

Decoding this base64 string revealed the solution to the challenge.

**FLAG:** flag{b6e54d0a0a5f2292589c3852f1930891}  
