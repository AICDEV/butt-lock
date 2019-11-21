## butt-lock

### disclaimer
These repository is only for informational and educational purpose. These repository is only for those who’re willing and curious to know and learn about security.I will not be responsible for any action performed by any reader. If you planned to use the content for illegal purpose, please leave this repository immediately and fuck yourself.

### what's butt-lock ?
It's an example of how a ransomware could work. In this particular case, butt-lock will encrypt all file on the hard disk (selectable / configurable as param) with
a random generated aes-cbc key. Before the encryption process starts, butt-lock will also create a rsa public and private key with a length of 4096 and reads your
mac address. The aes-key itselfs will be encrypted with the generated public key, after that the public key will be deleted. The "output" after the encryption process
is finished, is the base64 encoded rsa-oaep encrypted aes-cbc key, the mac-address and the private key (that's the important information, without a private key you are not able to decrypt the aes key).

You could send the butt-lock output object to you by email, twitter or whatever you prefer and... ;-). But remeber, it's only for education. DON'T DO IT!

Example output:

```ascii
WwI76NVTNeeSn00wAy9jzlpf3eJOtm=;f0:18:98:30:34:0b;-----BEGIN PRIVATE KEY-----
A 4096 length private key
-----END PRIVATE KEY-----
```