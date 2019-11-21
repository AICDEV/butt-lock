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
WwI76NVTNeeSn00wAy9jzlpf3eJOtmXUM7h0Z+OAlJOxe27jdvy6lu+LG+RX3NDZQAIa1jjF2sVQKWgDooxi8FWxovahlng1qie7ksa2xbXE6w2EqDv1tu3pteK9rtGCFd7AcoQPPZpjfCkeB9uFt/fKozWN6rDnTqTgnylsRVo/j0S6XvPKP2levVlhfNqK8uAHLTCCo9oHTJNATUzz6XKYz5mXsjo+y95MmHbnaxM2hxnm1AL8yzVhKKPM0Fk7zP3GMp1l/mOn41D8i6j3lglIecDLi4h7LFQ656fTBBZRqaSrC8U/Z3gxggNlAsdAkgdDb8D77LDkTBr86L7XKAjSZK94sGC95DWXz28BfzSE8dYMb0nnGAH47WnHNy5rjyIY6bYeYHi6eNRqixYOxZgvvuoylrLgWsEQ0k+MpMdldFThHp0kLiwhxFjU76YHi16P9/e3NMpVWrDPtxrqwvTE+swCvdRWrsPEAz0jtqdM0fBWSO+mNefC/CbB1T0YYmjXYf+ZKo74AKv6ks7SRZ6nM45CNZIgnsdxThO0g9L7Da8tnXO3v+G57kvljPDsPeLT60E2liJNkUXK7qHnFoI+7QTVu2GqyBFVdNzE479lLQYo6biALCw7/ygVadKcYIe5cE4J7XvggSESs6CyCYOTVYTvsUCZXhkAuTN60Fk=;f0:18:98:30:34:0b;-----BEGIN PRIVATE KEY-----
A 4096 length private key
-----END PRIVATE KEY-----
```