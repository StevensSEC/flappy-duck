# flappy-duck
A Flappy Bird clone built using pygame.

## Prerequisites

- [WSL 2 (if on Windows)](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Git](https://git-scm.com/)
- [Python 3.10](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

(Note: if using on Windows and using WSL, you'll be installing most of these things *onto* WSL rather than your host machine. The only exception is Visual Studio Code.)

## Environment Setup

Navigate to the root folder of this project. Then, create a virtual environment:

```bash
python3.10 -m venv venv
```

Once your virtual environment has been created, you will need to activate it:

```bash
source /venv/bin/activate
```

You can ensure that it worked by running `which`:
```bash
which python
```

If you get a result such as `<HOME_DIRECTORY>/flappy-ducks/venv/bin/python`, then you know that it worked correctly. (Replace
<HOME_DIRECTORY> swith the actual value of your home directory.)

Install the libraries that Flappy Ducks depends on:

```bash
pip install -r requirements.txt
```

## Running

In the root directory of the project, run:

```bash
./src/app.py
```

## Guides

You'll probably be unfamilar with much of the project to begin with. That's okay! An important part of software engineering is being
able to learn about a project's technology stack by referring to the documentation or guides. Here are a few for this project:

- [A Newbie Guide to pygame](https://www.pygame.org/docs/tut/newbieguide.html)
- [Pygame Docs](https://www.pygame.org/docs/)

Another great way to learn how to develop software is to read code! Try to go into this project and trace the program execution in your head. You'll find that you better understand what needs to be changed in order to implement a feature or fix a bug after doing so.