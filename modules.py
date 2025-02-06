import converters #importing converters.py from this same folder
from converters import lbs_to_kg #alternative way of accessing a module can press ctrl + space to see the import options
from utils import find_max 

print(converters.kg_to_lbs(70)) #using import

print(lbs_to_kg(100)) #using from-import


#each file is a module

print(find_max([43, 64, 38, 82, 10, 34, 83, 23, 77])) #find_max() is imported from utils file/module