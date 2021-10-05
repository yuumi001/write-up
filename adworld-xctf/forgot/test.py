from sys import *
for a1 in range(1000):
	if a1 > 96 and a1 <= 122 or a1 > 47 and a1 <= 57 or a1 == 95 or a1 == 45 or a1 == 43 or a1 == 46:
		stdout.write(str(chr(a1)))
print
for a1 in range(1000):
	if a1 > 96 and a1 <= 122 or a1 > 47 and a1 <= 57 or a1 == 95:
		stdout.write(chr(a1))
print
for a1 in range(1000):
	if a1 > 96 and a1 <= 122:
		stdout.write(chr(a1))
