import base64
import hashlib
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt  # pip install cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


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
            with open(public_key, "w", encoding="utf-8") as key_file:
                key_file.write(key)
        except:
            print("Dosya yolu hatası.")

    def save_password(self, voter_password):
        try:
            password = os.getcwd() + "/keys/password.aos"
            with open(password, "w", encoding="utf-8") as password_file:
                password_file.write(voter_password)
        except:
            print("Dosya yolu hatası.")

    def encrypt(self, chunkParam, passwordParam):
        key = self.deriveKey(passwordParam)
        fernet = Fernet(key)
        encryptedChunk = fernet.encrypt(bytes(chunkParam, 'utf-8'))
        return encryptedChunk.decode()

    def decrypt(self, chunkParam, passwordParam):
        key = self.deriveKey(passwordParam)
        fernet = Fernet(key)
        decryptedChunk = fernet.decrypt(chunkParam)
        return decryptedChunk.decode()

    def deriveKey(self, passwordParam):
        if type(passwordParam) == str:
            passwordParam = passwordParam.encode("utf-8")
        keyDerivationFunction = Scrypt(
            salt=b'ABCDEFGHIJKLMNOP',
            length=32,
            n=2 ** 14,
            r=8,
            p=1,
            backend=default_backend()
        )
        deriveKey = keyDerivationFunction.derive(passwordParam)
        key = base64.urlsafe_b64encode(deriveKey)
        return key


if __name__ == "__main__":
    print(CryptographerAos().do_Hash256("Fudala'ya el ver."))
