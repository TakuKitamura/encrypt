import usbKeys as keys
import usbInfo as info

def main():
	seed = info.USBInfo().getUSBInfo()
	usbKeys = keys.USBKeys(seed)
	print("0: encrypt\n1: decrypt\n")
	inputType = input("type: ")
	print()
	if inputType == "0":
		inputSecretText = input("secretText: ")

		if len(inputSecretText) == 0:
			print("no secretText.")
			exit(1)
		print()
		encryptedText = usbKeys.encrypt(inputSecretText, seed)
		print("encryptedText: [" + encryptedText + "]")
	elif inputType == "1":
		inputEncryptedText = input("encryptedText: ")
		if len(inputEncryptedText) != 64:
			print("shoud be input correct encryptedText.")
			exit(1)
		print()
		decryptedText = usbKeys.decrypt(inputEncryptedText, seed)
		if len(decryptedText) == 0:
			print("decrypt faild.")
			exit(1)

		print("decryptedText: [" + decryptedText + "]")
	else:
		print("shoud be input correct type.")
		exit(1)

if __name__ == '__main__':
	main()
	exit(0)