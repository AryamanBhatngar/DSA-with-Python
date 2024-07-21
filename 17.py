import re

def check_pattern(pattern, string):
  """
  Checks if a regular expression pattern is matching with a string.

  Args:
    pattern: The regular expression pattern.
    string: The string to check.

  Returns:
    True if the pattern matches the string, False otherwise.
  """

  regex = re.compile(pattern)
  match = regex.search(string)
  if match:
    return True
  else:
    return False

# Example usage:

pattern = 'test.*regular'
string = 'I want to test this string against a regular expression'

if check_pattern(pattern, string):
  print('Matched')
else:
  print('Not Matched')s