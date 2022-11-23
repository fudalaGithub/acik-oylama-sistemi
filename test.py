import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def DeriveKey(passwordParam): # Parola ile key oluşturmak için bu func
    #Parolayı byte olmalı
    if type(passwordParam) == str:
        passwordParam = passwordParam.encode("utf-8")
    keyDerivationFunction = Scrypt(
        # bu *salt* çok önemli hep aynı parolayı oluşturması için 16 bytelik statik değer lazım
        # eğer sabit değer olmazsa hep değişik key oluşturamış ve decrypt yapakan şifre gırılmazmış
        salt = b'ABCDEFGHIJKLMNOP',  # Bu da aslında parola ile eşleşen ikinci parola
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    deriveKey = keyDerivationFunction.derive(passwordParam)
    key = base64.urlsafe_b64encode(deriveKey) # Fernet() oluşturulan key'i base64 olarak istediği için
    # urlsafe_b64encodeb64encode() +'yı -'e ve /'u _'e dönüştürür Fernet'te problem olmasın diye
    return key

#a = DeriveKey("Merhaba1122")
#print("Key : ", a)

def Encrypt(chunkParam, passwordParam: str):
    key = DeriveKey(passwordParam)
    fernet = Fernet(key)
    encryptedChunk = fernet.encrypt(chunkParam) # Chunk yığın demek, string yerine bu chunk
    return encryptedChunk

def Decrypt(chunkParam, passwordParam: str):
    key = DeriveKey(passwordParam)
    fernet = Fernet(key)
    decryptedChunk = fernet.decrypt(chunkParam) # Chunk yığın demek, string yerine bu chunk
    return decryptedChunk


a = DeriveKey("Merhaba1122")
print("Key : ", a)

text = b'butext'
fernet = Fernet(a)
crypted_text = fernet.encrypt(text)
print("Crypted text " + str(crypted_text))

decrypted_text = fernet.decrypt(crypted_text)
print("decrypted_text text " + str(decrypted_text))
