import hmac
import hashlib
hash_gen = hmac.new(b'file key', digestmod=hashlib.sha256)

def hash_file1():
    f1 = open('directory1/file1.txt', 'rb')
    hashinput = f1.read()
    hash_gen.update(hashinput)
    f1.close()

    f1h = open('directory2/file1hash.txt','w')
    hashval1 = hash_gen.hexdigest()
    f1h.write(hashval1)
    print(hashval1)

def hash_file2():
    f2 = open('directory1/file2.txt', 'rb')
    hashinput = f2.read()
    hash_gen.update(hashinput)
    f2.close()

    f2h = open('directory2/file2hash.txt','w')
    hashval2 = hash_gen.hexdigest()
    f2h.write(hashval2)
    print(hashval2)

hash_file1()
hash_file2()