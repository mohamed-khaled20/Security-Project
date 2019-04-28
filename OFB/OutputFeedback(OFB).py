import SingleBlock as SingleDes


class OFB:

    def __init__(self,Key,IV):
        self.Key=Key
        self.IV=IV
        self.EncryptedData=""
        self.DecryptedData=""



    def Encrypt(self,Data):
        IV=self.IV
        # Pading Last Block with 0's
        while len(Data)%8!=0:
            Data="0"+Data

        for i in range(0,len(Data),8):
            A=SingleDes.SingleBlockDes(IV,self.Key)
            IV=A.Encrypt()
            print(chr(50))
            for j in range(8):
                self.EncryptedData+=chr(ord(IV[j])^ord(Data[i:i+8][j]))

    def Decrypt(self,Data):
        IV=self.IV
        # Pading Last Block with 0's
        while len(Data)%8!=0:
            Data="0"+Data

        for i in range(0,len(Data),8):
            A=SingleDes.SingleBlockDes(IV,self.Key)
            IV=A.Encrypt()
            for j in range(8):
                self.DecryptedData+=chr(ord(IV[j])^ord(Data[i:i+8][j]))
