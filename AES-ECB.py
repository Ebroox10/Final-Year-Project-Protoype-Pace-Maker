from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class ECB:
    ecbout =""
    
    def start(mode, data, passwd):
        if mode == "e":
            print("encrypting...")
            ECB.encrypt(data, passwd)
        if mode == "d":
            print ("decrypting...")
            ECB.decrypt(data, passwd)
        
    def encrypt(data, passwd):
        key = ECB.hash(passwd)
        BLOCK_SIZE = 16
        PAD = "{"
        padding = lambda s: s + (BLOCK_SIZE - len(s))* PAD
        cipher = AES.new(key, AES.MODE_ECB)
        result = (cipher.encrypt(padding(data).encode('utf-8'))).hex()
        
        print ("encrypted hexcode:", result)
        return result

    def decrypt(data , passwd):
        #bdata = bytes(data, 'utf-8')
        bdata = bytes.fromhex(data)
        key = ECB.hash(passwd)
        PAD = "{"
        decipher = AES.new(key, AES.MODE_ECB)
        print(bdata)
        ptext = decipher.decrypt(bdata).decode('utf-8')
        pad_index = ptext.find(PAD)
        result = ptext[:pad_index]
        print ("decrypted text:", result)
        return result

    def hash(passwd):
        phash = SHA256.new(passwd.encode('utf-8'))
        key = phash.digest()
        return key


mode = input("encrypt(e) or decrypt(d): ")
passwd = input("enter password: ")
data = input("Enter Data: ")
ECB.start(mode, data, passwd)




