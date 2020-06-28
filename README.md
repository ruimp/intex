# Intex

__Intex__ is a python terminal application to quickly integrate/differentiate expressions with optional LaTeX convertion. This simple script was developed to simplify direct LaTeX note-taking.

## Installation

Get the app by cloning the repo
   
    git clone https://github.com/ruimp/intex.git ~/.intex

and simply add an alias to your shell profile

    echo "alias intex=\"python ~/.intex/intex.py\"" >> .zshrc

replacing `.zshrc` with `.bashrc` if you use bash, and `python` by `python3` according to your setup.

## Options

__Intex__ allows for the following options, that may be combined:

- `-i` - integrate the expression

- `-d` - differentiate the expression

- `-l` - convert the output to LaTeX

## Examples

### Integration and Differentiation

![gif1](Animations/integ_diff.gif)

### Integration and Latex Conversion

![gif1](Animations/integ_latex.gif)

__Note:__ This is a simple project for simple use. If you need anything more complex I suggest using the Mathematica API. I aim to implement these features as an Emacs snippet to directly act on the buffer while writing LaTeX. Feedback is welcome.
