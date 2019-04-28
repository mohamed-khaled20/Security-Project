from Crypto.Cipher import DES

class SingleBlockDes:

    def __init__(self,IV,Key):
        self.IV=IV
        self.Key=Key
        return

    def Encrypt(self):
        cipher=DES.new(self.Key, DES.MODE_ECB)
        return cipher.encrypt(self.IV)
