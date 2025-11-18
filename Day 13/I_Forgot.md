# Huntress CTF 2025 - 🔍 I Forgot

**CTF Name:** Huntress CTF 2025
**Challenge name:** 🔍 I Forgot
**Challenge prompt:**
> So.... bad news.
> We got hit with ransomware.
> And... worse news... we paid the ransom.
> After the breach we FINALLY set up some sort of backup solution... it's not that good, but, it might save our bacon... because my VM crashed while I was trying to decrypt everything.
> And perhaps the worst news... I forgot the decryption key.
> Gosh, I have such bad memory!!

```
CAUTION

⚠️ This file was produced from a fresh Windows installation. Included within that are some antivirus signature strings and artifacts that may include profanity or unsettling language. Please be advised these remnants exist, but they are not part of the challenge.
```

```
NOTE

The archive password is "i_forgot".
```

**Challenge category:** Forensics
**Challenge points:** 10

* * *

## Steps to solve

In this challenge, `i_forgot.zip` file was provided. Once extracted, two files emerged: `flag.enc` and `memdump.dmp`. The first one is potentially out flag, but encrypted. The other one - as the name suggests - memory dump.

I decided to use volatility3 to inspect `memdump.dmp` snapshot:

![43d8b729e887.png](../assets/43d8b729e887.png)

`python3 ./vol.py -f ../memdump.dmp windows.pstree` was executed to browse the processes that were running while the VM crashed:

![40339136dcfc.png](../assets/40339136dcfc.png)

From the list of the processes above - we can clearly see that the user was running `Powershell.exe`, `notepad.exe` and `BackupHelper.exe`. The last one was of great interest to me, thus I decided to dump its information based on the PID value:

![406f20bac099.png](../assets/406f20bac099.png)

Once dumped, I used `binwalk` to examine and extract:

![d35c92d61d66.png](../assets/d35c92d61d66.png)

![7357d21c8b81.png](../assets/7357d21c8b81.png)

I tried extracting `.7z` archive but it is malformed. `key.enc` and `private.pem` files are 0 bytes each. `4000.zip` archive is protected with password - but it may contain files that are necessary for `flag.enc` decryption:

![1b95dbaf8a12.png](../assets/1b95dbaf8a12.png)

Thus, I proceeded to look for the potential password in the memory dump again:

![9da96aacc9f6.png](../assets/9da96aacc9f6.png)

I found `ePDaACdOCwaMiYDG` - and it worked!

![a63c260407ab.png](../assets/a63c260407ab.png)

![a7f666e7a72f.png](../assets/a7f666e7a72f.png)

Information from the OpenSSL documentation about possible values of rsa_padding_mode:

![a1ca00d53470.png](../assets/a1ca00d53470.png)

I tried `openssl pkeyutl -decrypt -inkey private.pem -in key.enc -out key_raw.bin -pkeyopt rsa_padding_mode:oaep` and it worked:

![21010b3f7063.png](../assets/21010b3f7063.png)

To proceed with decryption, I base64 encoded contents of `flag.enc` and pasted them to cyberchef. Next I tried dividing key_raw.bin into 32 bytes key and 16 bytes IV:

![f0a6b7bc0b5f.png](../assets/f0a6b7bc0b5f.png)

**FLAG:** flag{fa838fa9823e5d612b25001740faca31}
