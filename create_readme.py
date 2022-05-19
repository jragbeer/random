"""
Quickly create a README.md format/structure. Simply change the title, execute and copy the output into a README.md file.
"""

def format_text(text : str='', italics : bool=False, bold : bool=False, strikethrough: bool=False,) -> str:
    """
    Format text using a method and the various flags.
    :param text: text input
    :param italics: flag for using italics with the text
    :param bold: flag for using bold with the text
    :param strikethrough: flag for using strikethrough formatting with the text
    :return: the formatted text
    """
    output_text = text
    if italics:
        output_text = "_" + output_text + "_"
    if bold:
        output_text = "**" + output_text + "**"
    if strikethrough:
        output_text = "~~" + output_text + "~~"
    return output_text
def header(text : str, level : int=1, italics : bool=False, bold : bool=False, strikethrough: bool=False,) -> str:
    """
    Format the header using a method and various flags.
    :param text: text input
    :param level: What level of header to output
    :param italics: flag for using italics with the text
    :param bold: flag for using bold with the text
    :param strikethrough: flag for using strikethrough formatting with the text
    :return: the formatted text
    """
    return "#"*level + ' ' + format_text(text,italics = italics, bold = bold, strikethrough=strikethrough)
def badges() -> str:
    """
    Output a list of badges used for the project.
    :return: a string that contains all of the relevant badges.
    """
    return """[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
     [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
       [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
        [![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
        [![Interrogate](https://interrogate.readthedocs.io/en/latest/_static/interrogate_badge.svg)](https://github.com/econchick/interrogate)
        [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
"""

print(header('DBEng_WiresharkParsing_2022'))
print(badges())
print(header('Overview', level=2))
print(header('Additional Information', level=2))
print(header('Installation Instructions', level=2))
print(header('License', level=2))
license = """Copyright DB Engineering

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""
print(license)

