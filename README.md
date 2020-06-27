# Intex

__Intex__ is a python terminal application to quickly integrate/differentiate expressions with optional LaTeX convertion. This simple script was developed simplify direct LaTeX note-taking.

## Installation

Get the app by clonig the repo
   
   git clone https://github.com/ruimp/intex.git ~/.intex

and simply add an alias to your shell profile

    echo "alias intex=\"python ~/.intex/intex.py\"" >> .zshrc

replacing `.zshrc` with `.bashrc` if you use bash an `python` by `python3` according to your setup.

## Options

__Intex__ allows for the following otions:

- `-i` to integrate the expression

- `-d` to differentiate the expression

- `-l` to convert the output to LaTeX
