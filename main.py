import usbKeys as keys
import usbInfo as info
import ntp
from datetime import datetime
from pytz import timezone

def main():
	seed = info.USBInfo().getUSBInfo()
	usbKeys = keys.USBKeys(seed)
	print("0: encrypt\n1: decrypt\n")
	inputType = input("type: ")
	if inputType != "0" and inputType != "1":
		print("shoud be input correct type.")
		exit(1)
	print()
	password = input("password: ")
	print()
	if len(password) == 0:
		print("no password.")
		exit(1)

	seed += password + "|"
	utc = timezone('UTC')
	nowDate = ntp.NTPClient('0.europe.pool.ntp.org').getNowtime()
	nowUTCDate = utc.localize(nowDate)

	if inputType == "0":
		inputSecretText = input("secretText: ")

		if len(inputSecretText) == 0:
			print("no secretText.")
			exit(1)
		print()
		encryptedUSBInfo = usbKeys.encrypt(inputSecretText, seed)
		
		limitDate = input("limit date (ex. 2018-01-01 13:10:15): ")
		print()
		limitUTCDate = datetime.strptime(limitDate, '%Y-%m-%d %H:%M:%S').astimezone(utc)

		if limitUTCDate < nowUTCDate:
			print("shoud be limitDate > nowDate.")
			exit(1)
		encryptedDate = usbKeys.encrypt(str(limitUTCDate), seed)
		encryptedText = encryptedUSBInfo + encryptedDate
		
		print("encryptedText: [" + encryptedText + "]")
	elif inputType == "1":
		inputEncryptedText = input("encryptedText: ")
		print()
		if len(inputEncryptedText) != 128:
			print("shoud be input correct encryptedText.")
			exit(1)

		limitDate = usbKeys.decrypt(inputEncryptedText[64:], seed)

		if len(limitDate) == 0:
			print("decrypt faild.")
			exit(1)
		limitUTCDate = utc.localize(datetime.strptime(limitDate, '%Y-%m-%d %H:%M:%S+00:00'))
		
		if limitUTCDate < nowUTCDate:
			print("encryptedText is expaired.")
			exit(1)

		decryptedText = usbKeys.decrypt(inputEncryptedText[:64], seed)
		if len(decryptedText) == 0:
			print("decrypt faild.")
			exit(1)

		print("decryptedText: [" + decryptedText + "]")

if __name__ == '__main__':
	main()
	exit(0)