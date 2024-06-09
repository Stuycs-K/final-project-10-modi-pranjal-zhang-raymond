import sys, sha512v2

mode = sys.argv[1]
msg = sys.argv[2]

print(sha512v2.sha512(mode, msg))