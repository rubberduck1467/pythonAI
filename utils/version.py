"""Small module to extract simple semantic version numbers from docstrings and format them
    Version: 1.0.0
"""

class semVerNum:
    def __init__ (self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def format(self):
        return f"{self.major}.{self.minor}.{self.patch}"

def extractSemVer(docstring):
    words = docstring.split()
    consistent = map(lambda word: word.lower(), words)
    found = False
    for word in consistent:
        if found:
            strVer = word.split('.')
            break
        if "version" in word:
            found = True

    return semVerNum(*list(map (int, strVer)))