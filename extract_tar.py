import tarfile
import os

filename = 'target/tarfile-assembly-testcase-1.0-SNAPSHOT-src.tar.gz'
f = open(filename)

print("Trying to open", filename)

if not os.path.exists(filename):
    print("File", filename, "does not exists. Did you run 'mvn package'?")
    exit(1)

if not os.path.isfile(filename):
    print("File", filename, "is not a file.")
    exit(1)

try:
    tarfile.open(fileobj=f, mode='r:gz')
except Exception, e:
    print("Failed with exception", e.message)

print('Try to unpack the file from command-line with:\n   tar xvfz ' + filename)