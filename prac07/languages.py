from prac07.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languageList = [ruby,python,visual_basic]
    print("The dynamically typed languages are:")
    for each in languageList:
        if each.is_dynamic():
            print(each.name)

main()