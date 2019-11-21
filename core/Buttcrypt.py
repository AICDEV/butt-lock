from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Hash import SHA512
from Crypto.Util.Padding import pad
import string
import random
import base64

class Buttcrypt():
    def __init__(self):
        self.__generateNewRSAKey(4096,"buttlock")
        self.__buildAESKey()

    def getPrivateKey(self):
        return self._rsa_private_key_string

    def getPublicKey(self):
        return self._rsa_public_key_string

    def encryptContent(self, content):
        return self._aes_cipher.encrypt(pad(content, AES.block_size))

    def RSAEncryptContent(self, aes_concatinated_key):
        rsa_public_key                   = RSA.import_key(self._rsa_public_key_string)
        cipher_rsa                       = PKCS1_OAEP.new(rsa_public_key, hashAlgo = SHA512)
        rsa_encrypted                    = cipher_rsa.encrypt(aes_concatinated_key)
        rsa_encrypted_base64             = base64.b64encode(rsa_encrypted)
        return rsa_encrypted_base64

    def RSADecryptContent(self, rsa_encrypt):
        rsa_decrypted   = self._rsa_cipher.decrypt(rsa_encrypt)
        return rsa_decrypted

    def __generateNewRSAKey(self, rsa_key_length, passphrase):
        self._rsa_key                      = RSA.generate(rsa_key_length)
        self._rsa_private_key_string       = self._rsa_key.exportKey(passphrase=passphrase, format='PEM', pkcs=8, protection="scryptAndAES128-CBC")
        self._rsa_public_key_string        = self._rsa_key.publickey().exportKey(format='PEM')
        self.__processPrivateRSAKey(passphrase)

    def __processPrivateRSAKey(self, passphrase):
        self._rsa_private_key       = RSA.import_key(self._rsa_private_key_string, passphrase=passphrase)
        self._rsa_cipher            = PKCS1_OAEP.new(self._rsa_private_key, hashAlgo = SHA512)

    def __buildAESKey(self):
        self._aes_key = str.encode(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32)))
        self._aes_iv = str.encode(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)))
        self._aes_cipher  = AES.new(self._aes_key, AES.MODE_CBC, iv = self._aes_iv)

