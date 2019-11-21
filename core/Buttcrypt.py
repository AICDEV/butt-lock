from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Hash import SHA512
from Crypto.Util.Padding import pad, unpad
import string
import random
import base64

class Buttcrypt():
    def __init__(self):
        self.__generateNewRSAKey(4096)
        self.__buildAESKey()

    def getPrivateKey(self):
        return self._rsa_private_key_string

    def getPublicKey(self):
        return self._rsa_public_key_string

    def getAesKey(self):
        return self._aes_key+self._aes_iv

    def encryptContent(self, content):
        return self._aes_cipher.encrypt(pad(content, AES.block_size))

    def decryptContent(self, decrypted_aes_key, encrypted_content):
        aes_key         = decrypted_aes_key[:32]
        aes_iv          = decrypted_aes_key[32:]
        aes_cipher      = AES.new(aes_key, AES.MODE_CBC, iv = aes_iv)
        unciphered_data = unpad(aes_cipher.decrypt(encrypted_content), AES.block_size)
        return unciphered_data


    def RSAEncryptContent(self, aes_concatinated_key):
        rsa_public_key                   = RSA.import_key(self._rsa_public_key_string)
        cipher_rsa                       = PKCS1_OAEP.new(rsa_public_key, hashAlgo = SHA512)
        rsa_encrypted                    = cipher_rsa.encrypt(aes_concatinated_key)
        rsa_encrypted_base64             = base64.b64encode(rsa_encrypted)
        return rsa_encrypted_base64

    def RSADecryptContent(self, rsa_encrypt, private_key):
        rsa_private_key       = RSA.import_key(private_key)
        rsa_cipher            = PKCS1_OAEP.new(rsa_private_key, hashAlgo = SHA512)
        rsa_decrypted   = rsa_cipher.decrypt(rsa_encrypt)
        return rsa_decrypted

    def __generateNewRSAKey(self, rsa_key_length):
        self._rsa_key                      = RSA.generate(rsa_key_length)
        self._rsa_private_key_string       = self._rsa_key.exportKey(format='PEM', pkcs=8)
        self._rsa_public_key_string        = self._rsa_key.publickey().exportKey(format='PEM')
        self.__processPrivateRSAKey()

    def __processPrivateRSAKey(self):
        self._rsa_private_key       = RSA.import_key(self._rsa_private_key_string)
        self._rsa_cipher            = PKCS1_OAEP.new(self._rsa_private_key, hashAlgo = SHA512)

    def __buildAESKey(self):
        self._aes_key = str.encode(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32)))
        self._aes_iv = str.encode(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)))
        self._aes_cipher  = AES.new(self._aes_key, AES.MODE_CBC, iv = self._aes_iv)

