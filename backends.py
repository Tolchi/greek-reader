class LaTeX:

    def preamble(self, typeface, language):
        return """
\\documentclass[a4paper,12pt]{{scrartcl}}

\\usepackage{{setspace}}
\\usepackage{{fontspec}}
\\usepackage{{dblfnote}}
\\usepackage{{pfnote}}
\\usepackage{{polyglossia}}
\\setdefaultlanguage[variant=ancient]{{greek}}
\\setotherlanguage{{{language}}}

\\setromanfont{{{typeface}}}

\\linespread{{1.5}}
\\onehalfspacing

\\makeatletter
\\renewcommand\\@makefntext[1]{{\\leftskip=2em\\hskip-2em\\@makefnmark#1}}
\\makeatother

\\begin{{document}}
""".format(typeface=typeface, language=language)

    def chapter_verse(self, chapter, verse):
        return "\\textbf{{\Large {}.{}}}~".format(chapter, verse)

    def verse(self, verse):
        return "\\textbf{{{}}}~".format(verse)

    def word(self, text, headword=None, parse=None, gloss=None, language=None):
        if headword is None and parse is None and gloss is None:
            return text
        else:
            footnote = []
            if headword:
                footnote.append(headword)
            if parse:
                footnote.append("\\textendash\\ {}".format(parse))
            if gloss:
                footnote.append("\\textendash\\ \\text{}{{\\textit{{{}}}}}".format(language, gloss))

            return "{}\\footnote{{{}}}".format(text, " ".join(footnote))

    def comment(self, text):
        return "% {}".format(text)

    def postamble(self):
        return "\\end{document}"


class SILE:

    def preamble(self, typeface, language):
        return """\
\\begin[papersize=a4,class=book]{{document}}

\\font[family="{typeface}",size=12pt,language=el]
\\set[parameter=document.lineskip,value=6pt]
""".format(typeface=typeface)

    def chapter_verse(self, chapter, verse):
        return "\\font[size=16pt,weight=700]{{{}.{}}}\\nobreak".format(chapter, verse)

    def verse(self, verse):
        return "\\font[weight=700]{{{}}}\\nobreak".format(verse)

    def word(self, text, headword=None, parse=None, gloss=None, language=None):
        if headword is None and parse is None and gloss is None:
            return text
        else:
            footnote = []
            if headword:
                footnote.append(headword)
            if parse:
                footnote.append("– {}".format(parse))
            if gloss:
                footnote.append("– \\font[style=italic,language={}]{{{}}}".format(language, gloss))

            return "{}\\footnote{{{}}}".format(text, " ".join(footnote))

    def comment(self, text):
        return "% {}".format(text)

    def postamble(self):
        return "\\end{document}"
