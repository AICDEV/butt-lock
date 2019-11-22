from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Hash import SHA512
from Crypto.Util.Padding import pad, unpad
import string
import random
import base64

class Buttdecrypt():
    def decryptContent(self, key, iv, encrypted_content):
        aes_cipher = AES.new(key, AES.MODE_CBC, iv = iv)
        unciphered_data = unpad(aes_cipher.decrypt(encrypted_content), AES.block_size)
        return unciphered_data


    def RSADecryptContent(self, rsa_encrypt, private_key):
        rsa_private_key       = RSA.import_key(private_key)
        rsa_cipher            = PKCS1_OAEP.new(rsa_private_key, hashAlgo = SHA512)
        rsa_decrypted   = rsa_cipher.decrypt(rsa_encrypt)
        return rsa_decrypted

    
