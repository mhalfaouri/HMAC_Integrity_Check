import hmac
import hashlib
hash_gen = hmac.new(b'file key', digestmod=hashlib.sha256)

def checkfile1():
    f1 = open('directory1/file1.txt', 'rb')

    hashinput = f1.read()
    hash_gen.update(hashinput)
    f1.close()

    f1h = open('directory2/file1hash.txt', 'r')
    storedhash = f1h.read()

    if hash_gen.hexdigest() == storedhash:
        print("File 1: YES")
    else:
        print("File 1: NO") 

def checkfile2():
    f2 = open('directory1/file2.txt', 'rb')

    hashinput = f2.read()
    hash_gen.update(hashinput)
    f2.close()

    f2h = open('directory2/file2hash.txt', 'r')
    storedhash = f2h.read()

    if hash_gen.hexdigest() == storedhash:
        print("File 2: YES")
    else:
        print("File 2: NO")

checkfile1()
checkfile2() 