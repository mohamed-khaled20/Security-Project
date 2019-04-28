import SingleBlock as SingleDes

class Counter:

    def __init__(self,Counter,Key):
        self.Counter=Counter
        self.Key=Key

    def Encrypt(self,Data):
        Counter=self.Counter
        # Pading Last Block with 0's
        while len(Data)%8!=0:
            Data="0"+Data

        for i in range(0,len(Data),8):
            A=SingleDes.SingleBlockDes(Counter,self.Key)
            E=A.Encrypt()
            print(chr(50))
            for j in range(8):
                self.EncryptedData+=chr(ord(E[j])^ord(Data[i:i+8][j]))
            Counter+=1

    def Decrypt(self,Data):
        Counter=self.Counter
        # Pading Last Block with 0's
        while len(Data)%8!=0:
            Data="0"+Data

        for i in range(0,len(Data),8):
            A=SingleDes.SingleBlockDes(Counter,self.Key)
            E=A.Encrypt()
            print(chr(50))
            for j in range(8):
                self.EncryptedData+=chr(ord(E[j])^ord(Data[i:i+8][j]))
            Counter+=1
