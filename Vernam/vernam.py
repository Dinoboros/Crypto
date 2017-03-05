import re

def vernam(binaryWord, key):
	cryptedWord = ""
	for i in range(len(binaryWord)):
		cryptedWord += str(int(key[i % len(key)]) ^ int(binaryWord[i])) 
	return cryptedWord


# Code execute lors de l'execution du fichier
if __name__ == '__main__':

	def _exit():
		finished[0] = True

	def _vernamBinaryDefaultKey():
		binaryWord = raw_input("\nEntrez votre mot binaire : ")
		defaultKey = "011"
		p = re.compile('[01]+')
		if not p.match(binaryWord):
			print binaryWord, "n'est pas un mot binaire"
		else:
			print "Votre mot", binaryWord, "donne", vernam(binaryWord, defaultKey), "par la cle par default"

	def _vernamBinaryKey():
		binaryWord = raw_input("\nEntrez votre mot binaire : ")
		key = raw_input("Entrez votre cle (sous forme binaire) : ")
		p = re.compile('[01]+')
		if not p.match(binaryWord):
			print binaryWord, "n'est pas un mot binaire"
		elif not p.match(key):
			print key, "n'est pas un mot binaire"
		else:
			print "Votre mot", binaryWord, "donne", vernam(binaryWord, key), "avec la cle", key

	def _vernamStrKey():
		string = raw_input("\nEntrez votre message : ")
		key = raw_input("Entrez votre clez (sous forme binaire) : ")
		p = re.compile('[01]+')
		if not p.match(key):
			print key, "n'est pas un mot binaire"
		else:
			stringAscii = "".join(format(ord(c), 'b') for c in string)
			print "Votre string :", string
			print "En AscII:", stringAscii
			print "En binaire", "0" + bin(int(stringAscii))[2:]
		

	finished = [False]
	while not finished[0]:
		print "\n\n"
		menu = {"1":_vernamBinaryDefaultKey, "2":_vernamBinaryKey, "3":_vernamStrKey, "0":_exit}
		choicesMenu = ["1 - Chiffrer ou dechiffrer un mot binaire avec la cle par default", "2 - Chiffrer ou dechiffrer un mot binaire avec une cle choisie", "3 - Chiffrer une chaine de caractere avec une cle choisie", "0 - Quitter"]

		print "Menu"
		for choice in choicesMenu:
			print "\t", choice
		choice = raw_input("\nChoix : ")

		if choice in menu.keys():
			menu[choice]()
		else:
			print "Choix invalide"
		

