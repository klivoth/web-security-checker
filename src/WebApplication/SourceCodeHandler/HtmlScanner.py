import re

class HtmlScanner():
    def __init__(self):
        pass

    def checkHiddenObject(self, elements):
    # Check if elements contain hidden elements.
    # Only check for visibility = "hidden", not display = "none",
    # since the latter cannot be clicked.

        for e in elements:
            a = re.search(r'visibility\s*(:|=)(\s|\"|\')*hidden(\s|\"|\')*', e)
            if a != None and len(a) != 0:
                b = re.search(r'display\s*(:|=)(\s|\"|\')*none(\s|\"|\')*', e)
                if b != None and len(b) == 0 and ('click' not in e):
                    return True
        return False
