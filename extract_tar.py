import tarfile
import os
import sys
import traceback

filename = 'target/tarfile-assembly-testcase-1.0-SNAPSHOT-src.tar.gz'
f = open(filename)

print "Trying to open", filename

if not os.path.exists(filename):
    print "File", filename, "does not exists. Did you run 'mvn package'?"
    exit(1)

if not os.path.isfile(filename):
    print "File", filename, "is not a file."
    exit(1)

try:
    tarfile.open(fileobj=f, mode='r:gz')
except Exception, e:
    type_, value_, traceback_ = sys.exc_info()
    print(''.join(traceback.format_exception(type_, value_, traceback_)))

print('Now try to unpack the file from command-line with:\n   tar xvfz ' + filename)