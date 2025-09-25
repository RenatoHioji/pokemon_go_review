dictionary = ["hello", "world", "python", "proggraming", "language"]


def spell_checker(word):
    if word in dictionary:
        return f"{word} está correto!"
    else:
        return f"{word} está incorreto. Verifique a ortografia."

print(spell_checker("python"))
print(spell_checker("progmmming"))
