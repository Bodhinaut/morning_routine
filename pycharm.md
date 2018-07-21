https://www.jetbrains.com/pycharm/documentation/

---


### Quick Start Guide

#### This Quick Start Guide is designed to introduce the key concepts and help you make a quick start with the IDE.

**Step 0. Before you start**


Which languages does PyCharm support?
With PyCharm you can develop applications in Python. In addition, in the Professional edition, one can develop Django, Flask and Pyramid applications. Also, it fully supports HTML (including HTML5), CSS, JavaScript, and XML: these languages are bundled in the IDE via plugins and are switched on for you by default. Support for the other languages and frameworks can also be added via plugins (go to Settings | Plugins or PyCharm | Preferences | Plugins for macOS users, to find out more or set them up during the first IDE launch).

What platforms can I run PyCharm on?
PyCharm is a cross-platform IDE that works on Windows, macOS, and Linux.

If you need assistance installing PyCharm, see the installation instructions: Requirements, Installation and Launching

What do I need to start with PyCharm?
In general to start developing in Python with PyCharm you need to download, install and start PyCharm (depending on your platform).

---

**Step 1**

**Open/Create a project in PyCharm**

Why do I need a project?

Everything you do in PyCharm is done within the context of a project. It serves as a basis for coding assistance, bulk refactoring, coding style consistency, etc.

You have three options to start working on a project inside the IDE:

Open an existing project

Begin by opening one of your existing projects stored on your computer. You can do by clicking Open Project on the Welcome screen (or choosig File | Open):

---

**Step 2. Look around**


When you launch PyCharm for the very first time, or when there are no open projects, you see the Welcome screen. It gives you the main entry points into the IDE: creating or opening a project, checking out a project from version control, viewing documentation, and configuring the IDE.

When a project is opened, you see the main window divided into several logical areas. Let’s take a moment to see the key UI elements here:

Project view on the left side displays your project files.
Editor on the right side, where you actually write your code. It has tabs for easy navigation between open files.
Navigation bar above the editor additionally allows you to quickly run and debug your application as well as do the basic VCS actions.
Left gutter, the vertical stripe next to the editor, shows the breakpoints you have, and provides a convenient way to navigate through the code hierarchy like going to definition/declaration. It also shows line numbers and per-line VCS history.
Right gutter, on the right side of the editor. PyCharm constantly monitors the quality of your code and always shows the results of its code inspections in the right gutter: errors, warnings, etc. The indicator in the top right-hand corner shows the overall status of code inspections for the entire file.
Tool windows are specialized windows attached to the bottom and sides of the workspace and provide access to typical tasks such as project management, source code search and navigation, integration with version control systems, etc.
The status bar indicates the status of your project and the entire IDE, and shows various warnings and information messages like file encoding, line separator, inspection profile, etc.
Also, in the bottom-left corner of the PyCharm window, in the Status bar, you see the button  show hide tool window bars or show tool window bars. This button toggles the showing of the tool window bars. If you hover your mouse pointer over this button, the list of the currently available tool windows show up:

---

**Step 3.**

Customize your environment
Feel free to tweak the IDE so it suits your needs perfectly and is as helpful and comfortable as it can be. Go to File | Settings (PyCharm | Preferences for macOS users) to see the list of available customization options.

Appearance
The first thing to fine-tune is the general "look and feel." Go to File | Settings | Appearance and Behavior | Appearance (PyCharm | Preferences | Appearance and Behavior | Appearance for macOS users) to select the IDE theme: the default light theme, or Darcula if you prefer a darker setting.

Editor
The many pages available under File | Settings | Editor (PyCharm | Preferences | Editor for macOS users) help you adjust every aspect of the editor’s behavior. A lot of options are available here, from general settings (like Drag'n'Drop enabling, scrolling configuration, etc.), to color configuration for each available language and use case, to tabs and code folding settings, to code completion behavior and even postfix templates.

Refer to the section Customizing PyCharm for details.

Code style
Code style can be defined for each language under File | Settings | Editor | Code Style (PyCharm | Preferences | Editor | Code Style for macOS users). You can also create and save your own coding style scheme.

_Keymap_

PyCharm uses the keyboard-centric approach, meaning that nearly all actions possible in the IDE are mapped to keyboard shortcuts.

The set of keyboard shortcuts you work with is one of your most intimate habits — your fingers "remember" certain combinations of keys, and changing this habit is easier said than done. PyCharm supplies you with a default keymap (choose Help | Keymap Reference on the main menu) making your coding really productive and convenient. However, you can always change it going to File | Settings | Keymap (PyCharm | Preferences | Keymap for macOS users).

There are also some pre-defined keymaps (like Emacs, Visual Studio, Eclipse, NetBeans etc.), and you can also create your own keymap based on an existing one.

If you feel most productive with vi/Vim, an emulation mode will give you the best of both worlds. Simply enable the IdeaVim plugin in the IDE and select the vim keymap.

Refer to the section Configuring Keyboard Shortcuts for details.

---

**Step 4.** 

Code with smart assistance
PyCharm takes care of the routine so that you can focus on the important. Use the following coding capabilities to create error-free applications without wasting precious time.

Code completion
Code completion is a great time-saver, regardless of the type of file you’re working with.

Basic completion works as you type and completes any name instantly.

Smart type completion analyzes the context you’re currently working in and offers more accurate suggestions based on that analysis.

Intention actions
PyCharm keeps an eye on what you are currently doing and makes smart suggestions, called intention actions, to save more of your time. Indicated with a lightbulb, intention actions let you apply automatic changes to code that is correct (in contrast to code inspections that provides quick-fixes for code that may be incorrect). Did you forget to add some parameters and field initializers to the constructor? Not a problem with PyCharm. Click the lightbulb (or press Alt+Enter) and select one of the suggested options:

py QST intentionAction
The full list of available intention actions can be found in File | Settings | Editor | Intentions or PyCharm | Preferences | Editor | Intentions for macOS users.

---



