from colorama import init, Fore, Back
init()

names =input("Enter file name with people's names: ")

namesout =input("Enter file to write user names to:")

infile= open(names, "r")

outfile = open(namesout, "w")



nameSeq=infile.readlines()

for name in nameSeq:

    splitname = name.strip().split(" ")

    firstname = splitname[0]

    lastname = splitname[1]

    username = firstname[0] + lastname[:7]

    username = username.lower()

    

    print ( username, file=outfile)



infile.close()

outfile.close()

print ( Back.BLUE + Fore.WHITE + "All Finished, Your new Document is created (check your folder)")