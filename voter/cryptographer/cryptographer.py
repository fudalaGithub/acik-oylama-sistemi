import hashlib
import os


class Cryptographer():

    def do_Hash256(self, input) -> str:
        hashed_string = hashlib.sha256(input.encode('utf-8')).hexdigest()
        return hashed_string
    
    def save_private_key(self, key):
        private_key = os.getcwd() + "/voter/keys/private_key.aos"
        with open(private_key, "w",encoding = "utf-8") as key_file:
            key_file.write(key)
            
    def save_public_key(self, key):
        public_key = os.getcwd() + "/voter/keys/public_key.aos"
        with open(public_key, "w",encoding = "utf-8") as key_file:
            key_file.write(key)

if __name__ == "__main__":
    print(Cryptographer().do_Hash256("a5ba14f57933a11e3853e1b690451e37c80c41e254da0d792df858a7cd85f11c"))