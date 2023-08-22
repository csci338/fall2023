---
layout: two-column
title: The Command Line
parent: resources
type: resource
category: "Code Editors"
---

## Why is important to know how to the command line?
* You can SSH (Secure Shell) into any server in the world (without installing special software / clients).
* It allows you greater control over your system's functions (creating files and folders, changing permissions, running executables, creating shortcuts / symlinks).
* Many advanced system functions don't have a GUI interface (or the GUI isn't any easier to use!).
* It's faster (once you get the hang of it).
* You can bundle system commands into scripts tailored to specific use cases (and configure when and how they run).
* It allows you to easily stop and start services and processes (e.g., database servers, web servers, system tasks).
* Most package managers (e.g., `npm`, `pip`, `gem`, `brew`, `apt-get`, `yum`) require them for tracking / organizing dependencies (which you need when building software).


## Useful References
In this course, we will be using bash. Bash is a Unix shell and command language that runs natively on Mac, Linux, and Unix operating systems. If you are a Windows user, you will be using WSL (see below) to run a GNU/Linux environment.

### Using Linux Commands on Windows via WSL
The **Windows Subsystem for Linux** (WSL) lets Windows users run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.
* [About](https://learn.microsoft.com/en-us/windows/wsl/about)
* [Installation / Configuration](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)

### Environment files
Environment files set environment variables on your operating system. This allows you to configure shortcuts and run scripts on startup. Here are some relevant resources for configuring these files:
* [Bash startup files loading order](https://medium.com/@rajsek/zsh-bash-startup-files-loading-order-bashrc-zshrc-etc-e30045652f2e)
* Sample `.zshrc` customizations you can make: Check out [Semmy's GitHub repo](https://github.com/semmypurewal/dotfiles/blob/master/zsh).

## Cheatsheet of Useful Bash Commands
Online cheatsheets:
* [https://github.com/RehanSaeed/Bash-Cheat-Sheet](https://github.com/RehanSaeed/Bash-Cheat-Sheet)


{:.instructions.medium}
| | Shell (Mac / Linux / WSL) |
|--|--|
| **What directory am I in?** | `$ pwd` |
| **Change directories** | `$ cd {{your_file_path}}` |
| **List files & directories** | `$ ls`<br>`$ ls -l` |
| **Navigate to parent directory** |
| **Navigate into child directory** | `$ cd csci338` |
| **Navigate into descendant directory** | `$ cd lectures/lecture03` |
| **Navigate to sibling directory** | `$ cd  ../lecture02` |
| **Navigate to ancestor directory** | `$ cd  ../../` |
| **Navigate to home directory** | `$ cd` |
| **Command history** | `$ history` |

Other commands you may find useful...

{:.instructions.medium}
| | Shell (Mac / Linux) |
|--|--|--|
| **Create a new file** | `$ echo . > my_file.txt`<br> `$ touch my_file.txt` |
| **Append to a file** | `$ echo "some text" > my_file.txt` |
| **Save history to a file** | `$ history > my_history.txt` |
| **Move a file** | `$ mv my_history.txt Documents/.` |
| **Make a folder** | `$ mkdir my_folder` |
| **Delete a file** | `$ rm my_history.txt` |
| **Delete a folder** | `$ rm -r my_folder` |

## What is sudo?
<img src="https://imgs.xkcd.com/comics/sandwich.png" />

Sudo is a command line utility that provides a way to temporarily grant users or user groups privileged access to system resources so that they can run commands that they cannot run under their regular accounts. Only accounts listed in the system's "sudoers" file are granted privileged access. On Macs and PCs, accounts that have administrator privileges are typically also added to the sudoers file.

* Read more [here](https://www.techtarget.com/searchsecurity/definition/sudo-superuser-do).