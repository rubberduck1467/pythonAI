"""Small module to extract simple semantic version numbers from docstrings and format them and format them
    Version: 1.0.0
"""

class semVerNum:
    def __init__ (self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def format(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    
bob = semVerNum(27,1,10)
print(bob.format())