import aes
import hashlib
import sha3
import hmac

class USBKeys(str):
	def __init__(self, seed):
		self.seed = seed

	def hmac_sha3_512(self, seed):
		s = hashlib.sha3_512()
		s.update(s.hexdigest().encode('utf-8'))
		salt = s.hexdigest()
		return hmac.new(bytes(salt, 'ascii'), bytes(seed, 'ascii'), hashlib.sha256).hexdigest()

	def encrypt(self, inputSecretText, seed):
		secretKey = self.hmac_sha3_512(seed)
		cipher = aes.AESCipher(secretKey)
		encryptedText = cipher.encrypt(inputSecretText)
		try:
			encryptedText = encryptedText.decode('utf-8')
			return encryptedText
		except UnicodeDecodeError:
			return ""

	def decrypt(self, encryptedText, seed):
		secretKey = self.hmac_sha3_512(seed)
		cipher = aes.AESCipher(secretKey)
		decryptedText = cipher.decrypt(encryptedText)
		try:
			decryptedText = decryptedText.decode('utf-8')
			return decryptedText
		except UnicodeDecodeError:
			return ""