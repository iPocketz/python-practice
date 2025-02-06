#directories:google -> python 3 module index

from pathlib import Path

# Absolute path
#root of hard disk

# Relative path
#local directories

path = Path()
for file in path.glob('*'):
    print(file)