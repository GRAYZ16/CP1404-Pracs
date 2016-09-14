from Prac07.programminglanguage import ProgrammingLanguage

languages = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995), ProgrammingLanguage("Python", "Dynamic", True, 1991),
			 ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print("The dynamically typed languages are")
for language in languages:
	if language.is_dynamic():
		print(language.name)
