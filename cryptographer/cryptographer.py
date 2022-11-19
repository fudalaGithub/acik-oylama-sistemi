import hashlib


class Cryptographer():

    def doHash256(self, input) -> str:
        hashed_string = hashlib.sha256(input.encode('utf-8')).hexdigest()
        print(hashed_string)
        return hashed_string

if __name__ == "__main__":
    Cryptographer().doHash256("tdsdest")