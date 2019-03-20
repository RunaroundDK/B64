import base64
import time

def decode():
	print ("Enter the decrpyted text massage")
	ciphertext = input(">> ")
	print ("Converting plane text into bytes...")
	time.sleep(1)
	stringasbytes = str.encode(ciphertext)
	type(stringasbytes)
	
	output = base64.b64decode(stringasbytes)
	print (output)


def encode():
	print ("Enter a message to encrypt: ")
	planetext = input(">> " )
	print ("Converting plane text into bytes...")
	time.sleep(1)

	stringasbytes = str.encode(planetext) # Convert the string into 
	type(stringasbytes) # bytes

	output = base64.b64encode(stringasbytes) # Bytes-objects only not strings
	print(output) 



encode()
decode()
