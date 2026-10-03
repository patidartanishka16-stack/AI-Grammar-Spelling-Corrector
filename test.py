import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

text = "She go to college evry day. I am very hapy there."

matches = tool.check(text)

corrected_text = tool.correct(text)
print("Total errors:", len(matches))
print()

for match in matches:
    print("Message:", match.message)
    print("Suggestions:", match.replacements)
    print("First suggestion:", match.replacements[0])
    print("Category:", match.category)
    print("Offset:", match.offset)
    print("Error length:", match.error_length)
    print()

    corrected_text = tool.correct(text)

print("Original:", text)
print("Corrected:", corrected_text)