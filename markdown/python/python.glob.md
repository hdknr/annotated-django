## os.walk & fmatch

~~~py
import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('../Fleck'):
    for filename in fnmatch.filter(filenames, '*.cs'):
        matches.append(os.path.join(root, filename))

for m in matches:
    print m
~~~
