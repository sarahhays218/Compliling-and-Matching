import re

# characters are defined
character_1 = "Dorothy"
character_2 = "Henry"

# compile regular expression
# \w{7} means a word with 7 characters
regular_expression = re.compile("\w{7}")

# check for a match to character_1 here
result_1 = re.match(regular_expression, character_1)
match_1 = result_1.group(0)
#access matched text
print(match_1)

result_2 = re.match("\w{7}",character_2)
print(result_2)
# compile a regular expression to match a 7 character string of word characters and check for a match to character_2 