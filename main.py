from core import Buttcrypt, Buttnet
import base64

buttcrypt = Buttcrypt.Buttcrypt()

#print(buttcrypt._aes_key)
encrypted_aes_key = buttcrypt.RSAEncryptContent(buttcrypt._aes_key)
#print(encrypted_aes_key)

# decode = base64.b64decode(encrypted_aes_key)
# print(decode)

# decrypted = buttcrypt.RSADecryptContent(decode)
# print(decrypted)

cryptoContent = (encrypted_aes_key, Buttnet.getMacAddress(), base64.b64encode(buttcrypt._rsa_private_key_string))

print(cryptoContent)