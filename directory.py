import os

def main():

	directory = input("Enter the directory that you want to save the file : ")

	filename = input("Enter the filename : ")

	name = input("Enter your name : ")

	address = input("Enter your address : ")

	phone_number = input("Enter your phone number : ")

	#checking if the directory exists
	if not os.path.isdir(directory):
		os.mkdir(directory)
		
		writeFile = open(os.path.join(directory,filename),'w')
		writeFile.write(name+','+address+','+phone_number+'\n')
		writeFile.close()

		print("File contents:")
		readFile = open(os.path.join(directory,filename),'r')

		for line in readFile:

			print(line)

		readFile.close()

	else:

		print("Sorry that directory does not exist...")

main()