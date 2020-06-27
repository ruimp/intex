# Intex

__Intex__ is a python terminal application to quickly integrate/differentiate expressions with optional LaTeX convertion. This simple script was developed simplify direct LaTeX note-taking.

## Installation

Get the app by clonig the repo
   
    git clone https://github.com/ruimp/intex.git ~/.intex

and simply add an alias to your shell profile

    echo "alias intex=\"python ~/.intex/intex.py\"" >> .zshrc

replacing `.zshrc` with `.bashrc` if you use bash, and `python` by `python3` according to your setup.

## Options

__Intex__ allows for the following otions, that may be combined:

- `-i` - integrate the expression

- `-d` - differentiate the expression

- `-l` - convert the output to LaTeX

## Examples

![Text][Animations/integ_diff.gif]
