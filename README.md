## butt-lock

### disclaimer
These repository is only for informational and educational purpose. These repository is only for those who’re willing and curious to know and learn about security.I will not be responsible for any action performed by any reader. If you planned to use the content for illegal purpose, please leave this repository immediately and fuck yourself.

### what's butt-lock ?
It's an example of how a ransomware could work. In this particular case, butt-lock will encrypt all file on the hard disk (selectable / configurable as param) with
a random generated aes-cbc key. Before the encryption process starts, butt-lock will also create a rsa public and private key with a length of 4096 and reads your
mac address. The aes-key itselfs will be encrypted with the generated public key, after that the public key will be deleted. The "output" after the encryption process
is finished, is the base64 encoded rsa-oaep encrypted aes-cbc key, the mac-address and the private key (that's the important information, without a private key you are not able to decrypt the aes key).

You could send the butt-lock output object to you by email, twitter or whatever you prefer and... ;-). But remeber, it's only for education. DON'T DO IT!

Example output with format [encrypted_aes_key base64 encoded, mac address, private key base 64 encoded]
```ascii
WwI76NVTNeeSn00wAy9jzlpf3eJOtm=;f0:18:98:30:34:0b;LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUpRd0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQ
```

### how to use it to encrypt files
Buttlock comes with a few command line options.

-   --mode (simply set mode to encrypt or decrypt) default is encrypt
-   --dir (input directory for encryption) just leave it empty if you are in decrypt mode
-   --recovery (path to the buttlock_recovery file) it will be generated if you run encryption
-   -- replace (just for encryption) if you wish that buttlock will create a encrypted copy of your file, simply add copy as argument (it also the default value). If you set replace as argument, buttlock will override all your files with the encrypted outpu. be careful!.

Example call to encrypt files and override

```ascii
python3 main.py --mode=encrypt --dir ./temp --replace replace
```
This will encrypt all my files in temp directory and overrides the orginial files.

Buttlock will create a folder ./buttlock there you can find the recovery file that you need to decrypting your files. don't modify it.

Example call to encrypt files and create copy

```ascii
python3 main.py --mode=encrypt --dir ./temp --replace copy
```

### how to use it to decrypt files
Buttlock comes with a few command line options.

-   --mode (simply set mode to encrypt or decrypt) default is encrypt
-   --dir (input directory for encryption) just leave it empty if you are in decrypt mode
-   --recovery (path to the buttlock_recovery file) it will be generated if you run encryption
-   -- replace (just for encryption) if you wish that buttlock will create a encrypted copy of your file, simply add copy as argument (it also the default value). If you set replace as argument, buttlock will override all your files with the encrypted outpu. be careful!.

Example call to decrypt your files:

```ascii
python3 main.py --mode=decrypt --dir ./temp --recovery ./buttlock/buttlock_recovery
```

This will decrypt all your files in ./temp. Important: You need the --recovery to decrypt the encrypted files.