import os, fnmatch


#Change this path string to the directory you want to refactor 
path = "/Users/damonskinner/Documents/Development/CodeBase/testParse"

#The old string you want to change
old_string = "tmp"

#The string you want to change to
new_string = ""

#The file types you want to modify
extensions = ["*.m","*.h"]

#Any specific edge case exceptions you want to omit from the refactoring
exceptions = ["tmpSelf", "tmpFloat"]

#Any sub-directories you want to omit from the refactoring
skipDirectories = ["Pods","Libraries"]



alphabetArray = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Q","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def findfilesAndReplaceString (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
        	with open(os.path.join(root, file), "r") as auto:
        		if any(eachDirectory in os.path.join(root,file) for eachDirectory in skipDirectories):
        			skippedFile = os.path.join(root,file)
        			print 'Skipping {skippedFile}'.format(**locals())
        		else:
        			for eachLetter in alphabetArray:
						stringToReplace = old_string + eachLetter
						inplace_change(auto.name, stringToReplace, eachLetter.lower())

def inplace_change(filename, old_string, new_string):
	s = open(filename).read()
	for word in s.split():
		if not any(eachException in word for eachException in exceptions):
			if old_string in word:
				name = os.path.basename(filename)
				newWord=word.replace(old_string, new_string)
				print 'Changing "{word}" to "{newWord}" in {name}'.format(**locals())
				s=s.replace(word, newWord)
				f=open(filename, 'w')
				f.write(s)
				f.flush()
				f.close()


print('Refactoring all "{old_string}" strings to "{new_string}" in directory: {path}'.format(**locals()))
print('Exceptions:{exceptions}'.format(**locals()))
print('Skipped Directories:{skipDirectories}\n'.format(**locals()))

for eachExtension in extensions:
	findfilesAndReplaceString(path, eachExtension)


	