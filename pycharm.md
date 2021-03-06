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

**Step 5. Keep your code neat**


PyCharm monitors your code and tries to keep it accurate and clean. It detects potential errors and problems and suggests quick-fixes for them.

Every time the IDE finds unused code, an endless loop, and many other things that likely require your attention, you’ll see a lightbulb. Click it, or press Alt+Enter, to apply a fix.

The complete list of available inspections can be found under Settings | Editor | Inspections (or PyCharm | Preferences | Editor | Inspections for macOS users). Disable some of them, or enable others, plus adjust the severity of each inspection. You decide whether it should be considered an error or just a warning.

---

**Step 6. Generate some code**


Writing code can be a lot easier and quicker when you use the code generation options available in PyCharm. The Code | Generate menu (Alt+Insert) will help you with creating symbols from usage, as well as suggest overriding/implementing some functions:

py QST impl over
Use live templates (choose Code | Insert Live Template or press Ctrl+J) to produce the entire code constructs. You can explore the available ready-to-use live templates In the Settings/Preferences dialog (Ctrl+Alt+S) (Settings | Editor | Live templates or PyCharm | Preferences | Editor | Live Templates if you are a macOS user).

If you see that you are lacking something especially important for your development, extend this set of templates with your own. Also, consider quickly surrounding your code with complete constructs (choose Code | Surround With or press Ctrl+Alt+T. For example, select an if statement:

py QST surround with 1
and you will get:

py QST surround with 2

---

**Step 7. Find your way through**


When your project is big, or when you have to work with someone else’s code, it’s vital to be able to quickly find what you are looking for and dig into the code. This is why PyCharm comes with a set of navigation and search features that help you find your way through any code no matter how tangled it is.

Basic search
With these search facilities, you can find and replace any fragment of code both in the currently opened file (Ctrl+F), or in an entire project (Ctrl+Shift+F).

Search for usages
To find where a particular symbol is used, PyCharm suggests full-scale search via Find Usages (Alt+F7):

py QST find usages
Project navigation
You can tell a lot just looking at your File Structure, with its imports or call hierarchies:

py QST file structure
Also, you can navigate to:

Class by its name (Ctrl+N).
File by its name (Ctrl+Shift+N):
py QST goToFile
Symbol by its name (Ctrl+Shift+Alt+N).
Declaration (Ctrl+B).
Base class/base function (Ctrl+U).
The icons in the left-hand gutter can also help you with navigation:

py QST goToSubclass
Navigate through the timeline
Remembering all your activity in the project, PyCharm can easily navigate you to the Recent Files (Ctrl+E) or Recently Changed Files (Shift+Alt+C).

To go through the history of changes, try using Back/Forward navigation (Ctrl+Alt+Left/ Ctrl+Alt+Right) and/or go to last edit location (Ctrl+Shift+Backspace).

Find Action
Take advantage of many smart actions possible with PyCharm. For example, use the Find Action search (Ctrl+Shift+A): just type a part of the action name, and the IDE will show you the list of all available options. Then, select the action you need:

cl QST findAction
Search Everywhere
If you have a general idea of what you're looking for, you can always locate the corresponding element using one of the existing navigation features. But what if you really want to look for something in every nook and cranny? The answer is to use Search Everywhere!

To try it, click the magnifying glass button in the upper right-hand corner of the window, or invoke it with Double Shift (press Shift twice).

py QST search everywhere

---


**Step 8. Run, debug and test**


Now when you’ve played with the code and discovered what you can do with it, it’s time to run, debug and test your app.

Run configuration
When you perform run, debug, or test operations with PyCharm, you always start a process based on one of the existing run/debug configurations, using its parameters.

Open the Run/Debug Configurations dialog Run | Edit Configurations to see all the available options. For example, if you want to run some script before/after the build phase, you can do this easily by creating an external tool:

py QST runDebugConfiguration
To run a configuration, press Shift+F10.

Run
The easiest way to run an application is to right-click its background in the editor, and then choose Run <name> on the context menu:

py run context menu
If your Python script contains the __main__ clause, then you can click the run from left gutter icon button in the left gutter, and then choose the desired command.

Debug
Does your application stumble on a run-time error? To find out what’s causing it, you will have to do some debugging. PyCharm supports the debugger on all platforms.

Debugging starts with placing breakpoints at which program execution will be suspended, so you can explore program data. Just click the left gutter of the line where you want the breakpoint to appear.

To start debugging your application, press Shift+F9. Then go through the program execution step by step (see the available options in the Run menu or in the Debug tool window), evaluate any arbitrary expression, add watches and manually set values for the variables.

py QST debugger
Refer to the section Debugging for details.

Test
It is a good idea to test your applications, and PyCharm helps doing it as simple as possible.

With PyCharm, you can:

Create tests
Create special testing run/debug configurations.
Run and debug tests right from the IDE, using the testing run/debug configurations.
And, finally, the most important thing - you can explore test results in the test runner tab of the Run tool window:
py test runner tab
To learn about the numbers, read the Test Runner Tab section.

PyCharm supports all the major Python testing frameworks:

Unittest
Doctest
Nosetest
py.test
For each of these frameworks, PyCharm provides its own run/debug configuration.

Refer to the tutorial Step 3. Testing Your First Python Application and to the Performing Tests section for details.

---

**Step 9. Keep your source code under Version Control**


VCS
If you are keeping your source code under version control, you will be glad to know that PyCharm integrates with many popular version control systems: Git (or GitHub), Mercurial, Perforce (supported in Professional edition only), Subversion and CVS. To specify credentials and any settings specific to a particular VCS, go to Settings | Version Control (or PyCharm | Preferences | Version Control if you are a macOS user).

The VCS menu gives you a clue about what commands are available. For example, you can see the changes you’ve made, commit them, create changelists and much more from the Local Changes view: VCS | Show Changes (or just press Alt+9). Also find some VCS basic commands in the Navigation bar above the editor:

py QST VCSbasic
Refer to the section Version control with PyCharm for details.

Local history
In addition to traditional version control, you can use the local history. With Local History, PyCharm automatically tracks changes you make to the source code, the results of refactoring, etc.

Local history is always enabled. To view it for a file or a folder, bring up Local History by selecting VCS | Local History | Show History. Here you can review the changes, revert them or create a patch.

---

**Step 10. Remote development**

With PyCharm, one can use project interpreters located remotely. In the Settings/Preferences dialog (Ctrl+Alt+S), choose the page Project Interpreter, then click artwork studio icons logcat toolbar settings), and select Add :

py add interpreter
You can add and configure the following remote interpreters:

SSH
Vagrant
Docker
Docker Composer
First, you can deploy your local applications to some remote server. To learn about deployment servers, refer to the section Configuring Synchronization with a Web Server. Having deployed an application, you can run, debug and test it remotely. PyCharm also helps you compare local and remote folders, and synchronize the local copy with that deployed on the server.

---
