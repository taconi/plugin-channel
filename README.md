# Micro Plugin Channel

This repository contains the `channel.json` file which lists all micro plugins. This is where the editor looks to search for plugins to install.

#### This is a fork of the [oficial channel](https://github.com/micro-editor/plugin-channel/) and the plugins available there will not be listed

---
⚠️  Warning!⚠️

This is just a plugin centralizer, plugin owners can change or add versions with malicious codes, I recommend checking each plugin before installing, use at your own risk

---

## Settings

Add this repository in `~/.config/micro/settings.json`

```json
"pluginchannels": [
    "https://raw.githubusercontent.com/micro-editor/plugin-channel/master/channel.json",
    "https://codeberg.org/micro-plugins/plugin-channel/raw/branch/main/channel.json"
]
```

## Plugins

----

* [Text utils](#text-utils)
* [Colorschemes](#colorschemes)
* [Syntax highlightings](#syntax-highlightings)
* [Formattings](#formattings)
* [Linters](#linters)
* [Search](#search)
* [File managers](#file-managers)
* [Status bar](#status-bar)
* [Completions](#completions)
* [Languages](#languages)
* [Markdown](#markdown)
* [Others](#others)

----

### Text utils

* [`capitalizer`](https://github.com/CodeGiorgino/capitalizer) - A simple micro-editor plugin that allows to capitalize selected text.

### Colorschemes

* [`colorschemes`](https://codeberg.org/micro-plugins/colorschemes) - Colorschemes aggregator.
* [`sunny-day`](https://github.com/dwwmmn/micro-sunny-day) - Port of the Emacs theme by Martin Haesler.

### Syntax highlightings

* [`language_ignore`](https://codeberg.org/micro-plugins/language-ignore) - Adds syntax highlighting to 'ignore' files.
* [`language_env`](https://codeberg.org/micro-plugins/language-env) - Syntax highlighting for files with .env extension.
* [`language_log`](https://codeberg.org/micro-plugins/language-log) - Syntax highlighting for files with .log extension.

### Formattings

* [`prettier`](https://github.com/sebkolind/micro-prettier) - This plugin provides the ability to format your code with Prettier.

### Linters

* [`lintertypescript`](https://github.com/sebkolind/micro-linter-typescript) - Ability to lint your Typescript (.ts & .tsx) files with tsc.
* [`aspell`](https://github.com/priner/micro-aspell-plugin) - Spellchecking with Aspel.

### Search

* [`findinfolder`](https://codeberg.org/micro-plugins/findinfolder/raw/branch/main/repo.json) - Folder search support.
* [`ag`](https://github.com/sebkolind/micro-ag) - This plugin provides the ability to search with "ag" (aka the_silver_searcher).
* [`fzfinder`](https://github.com/MuratovAS/micro-fzfinder) - Integrate fzf to select and search for your project files.
* [`grepsearch`](https://github.com/gaenseklein/grepsearch) - Using grep to recursively search in files.

### File managers

* [`filemanager2`](https://codeberg.org/micro-plugins/filemanager2) - Plugin that allows for easy navigation of a file tree.
* [`repfiles`](https://github.com/gaenseklein/repfiles) - A filemanager for your git-repository.

### Status bar

* [`gitStatus`](https://codeberg.org/micro-plugins/git-status) - Information about git in status bar.

### Languages

* [`nelua`](https://github.com/leapofazzam123/micro-nelua-plugin) - Nelua support for Micro text editor.

### Markdown

* [`preview`](https://github.com/weebi/micro-preview) - A very simple plugin to preview markdown in a second editor pane using pandoc.
* [`mdtree`](https://notabug.org/dustdfg/micro-mdtree) - A plugin for the micro text editor to add sidebar for jumpring and viewing TOC of markdown files.

### Others

* [`splitterm`](https://github.com/lukhof/splitterm) - Run a file or a selection of an inerpreted language within a new terminal window.
* [`acme`](https://github.com/xxuejie/micro-acme) - An acme style editing plugin for the micro editor.
* [`emacs_select`](https://github.com/kesslern/micro-emacs-select) - Emacs-style selection for Micro.
* [`delve`](https://github.com/serge-v/micro-delve) - Integrates golang delve debugger.
* [`wakatime`](https://github.com/wakatime/micro-wakatime) - Metrics, insights, and time tracking automatically generated from your programming activity.
* [`run`](https://github.com/terokarvinen/micro-run) - F5 to save and run, F12 to 'make', F9 to 'make' in background. Go, Python, Lua and executable file (#!) supported. Can 'make' whole project even from subdir.
* [`cheat`](https://github.com/terokarvinen/micro-cheat) - F1 cheatsheet for the language you're editing: Python, Go, Lua...
* [`palettero`](https://github.com/terokarvinen/palettero) - Command palette - Ctrl-P to fuzzy search & run commands, textfilters and descriptions
* [`gzplugin`](https://github.com/dzmanto/gzplugin4micro) - Read and write .gzip files.
* [`manager`](https://codeberg.org/micro-plugins/manager) - Provides a way to manage linters, formatters, commands, keybindings, settings, plugins.
* [`urlopen`](https://github.com/pjg11/micro-urlopen) - A plugin for the micro text editor to add support for opening URLs in text files.
* [`selto`](https://github.com/PawelMTRK/micro-selto-plugin) - Simple plugin allowing to quickly select lines.
* [`battery`](https://github.com/dubyte/battery-plugin) - Shows battery percentage on infobar.

## Adding your own plugin

Collaboration is super welcome! See [CONTRIBUTING.md](https://codeberg.org/micro-plugins/plugin-channel/src/branch/main/CONTRIBUTING.md).
