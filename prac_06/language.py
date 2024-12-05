from programming_language import ProgrammingLanguage

# Create instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print each instance to check the __str__ method
print(python)
print(ruby)
print(visual_basic)

# Create a list of programming languages
languages = [python, ruby, visual_basic]

# Test the is_dynamic method for each language
print("\nDynamically Typed Languages:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
