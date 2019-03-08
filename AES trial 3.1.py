import pyaes
import os

# A 256 bit (32 byte) key
key = os.urandom(32)
print("Enter the plain text")
plaintext =input()

print("the key is")
print(key)
# key must be bytes, so we convert it
#key = key.encode('utf-8')

aes = pyaes.AESModeOfOperationCTR(key)    
ciphertext = aes.encrypt(plaintext)

# show the encrypted data
print("the cipher text is")
print (ciphertext)

#DECRYPTION
# CRT mode decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext
decrypted = aes.decrypt(ciphertext).decode('utf-8')
print(decrypted)
# True
print (decrypted == plaintext)