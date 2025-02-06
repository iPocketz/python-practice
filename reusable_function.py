def emoji_converter(message):
    words = message.split(" ")
    emoji_face = {
    ":(": "😢",
    ":)": "😊"
    }
    output = ""
    for x in words:
        output += emoji_face.get(x, x) + " "
    return output


message = input("> ")
print(emoji_converter(message))
