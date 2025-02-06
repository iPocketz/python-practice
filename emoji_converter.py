

message = input("> ") #gather users input message
words = message.split(' ') # split each word apart depending on each use of spacebar
emoji_face = {
    ":(": "😢",
    ":)": "😊"
} # assign emoji faces, inside of a dictionary, depending on the users smile or frown

result = '' #empty string for appending new words
for x in words: #loop through user input
    result += emoji_face.get(x, x) + " " #append each index into result + space .get(x, x) assigns an emoji if it is :) or :( and default x value if it has not been reassigned
print(result) #print the appended result