import re

example = ".111.111.111-1"
pattern = r'^\d{1,3}(\.\d{3})*-[\dkK]$'
match = re.search(pattern,example)

print(match)

if match:
	print("found", match.group())
else:
	print("No match found")
