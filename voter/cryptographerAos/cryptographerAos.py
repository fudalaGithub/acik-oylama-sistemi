import hashlib
import os


class CryptographerAos():

    def do_Hash256(self, input) -> str:
        hashed_string = hashlib.sha256(input.encode('utf-8')).hexdigest()
        return hashed_string

    def save_private_key(self, key):
        try:
            private_key = os.getcwd() + "/keys/private_key.aos"
            with open(private_key, "w", encoding="utf-8") as key_file:
                key_file.write(key)
        except:
            print("Dosya yolu hatası. Çözüm; private_key = os.getcwd() voter/keys/private_key.aos olabilir")



    def save_public_key(self, key):
        try:
            public_key = os.getcwd() + "/keys/public_key.aos"
            with open(public_key, "w",encoding = "utf-8") as key_file:
                key_file.write(key)
        except:
            print("Dosya yolu hatası.")
            
    def save_password(self, voter_password):
        try:
            password = os.getcwd() + "/keys/password.aos"
            with open(password, "w",encoding = "utf-8") as password_file:
                password_file.write(voter_password)
        except:
            print("Dosya yolu hatası.")


if __name__ == "__main__":
    print(Cryptographer().do_Hash256("Fudala'ya el ver."))

