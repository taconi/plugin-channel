# Micro Plugin Channel

This repository contains the `channel.json` file which lists all micro plugins. This is where the editor looks to search for plugins to install.

#### This is a [oficial channel](https://github.com/micro-editor/plugin-channel/) fork

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

* [`snippets`](https://github.com/micro-editor/updated-plugins/tree/master/micro-snippets-plugin) - Provides snippets functionality.
* [`wc`](https://github.com/adamnpeace/micro-wc-plugin) - Plugin to count words/characters.
* [`manipulator`](https://github.com/NicolaiSoeborg/manipulator-plugin) - Extend text manipulation abilities.
* [`joinLines`](https://github.com/Lisiadito/join-lines-plugin) - Plugin which joins selected lines or the following with the current.
* [`bounce`](https://github.com/deusnefum/micro-bounce) - Plugin that implements nano-style smart home and bouncing the cursor between matching-brackets.
* [`quoter`](https://github.com/deusnefum/micro-quoter) - Plugin that allows you to add quotes or brackets around selected text.
* [`bookmark`](https://github.com/haqk/micro-bookmark) - Bookmark lines to quickly jump between saved positions.
* [`capitalizer`](https://github.com/CodeGiorgino/capitalizer) - A simple micro-editor plugin that allows to capitalize selected text.

### Colorschemes

* [`colorschemes`](https://codeberg.org/micro-plugins/colorschemes) - Colorschemes aggregator.
* [`nord-colors`](https://github.com/KiranWells/micro-nord-tc-colors) - A set of dark and light colorschemes based on Nord.
* [`sunny-day`](https://github.com/dwwmmn/micro-sunny-day) - Port of the Emacs theme by Martin Haesler.

### Syntax highlightings

* [`language_ignore`](https://codeberg.org/micro-plugins/language-ignore) - Adds syntax highlighting to 'ignore' files.
* [`language_env`](https://codeberg.org/micro-plugins/language-env) - Syntax highlighting for files with .env extension.
* [`language_log`](https://codeberg.org/micro-plugins/language-log) - Syntax highlighting for files with .log extension.

### Formattings

* [`go`](https://github.com/micro-editor/go-plugin) - Provides `gofmt` and `goimports` support for Go files.
* [`prettier`](https://github.com/sebkolind/micro-prettier) - This plugin provides the ability to format your code with Prettier.
* [`zigfmt`](https://github.com/squeek502/micro-zigfmt) - Provides `zig fmt` integration for Zig files.
* [`yapf`](https://github.com/a11ce/micro-yapf) - Runs `yapf` in place when saving python files.

### Linters

* [`yosyslint`](https://github.com/MuratovAS/micro-yosyslint) - Plugin for checking the syntax of the Verilog language. Based on yosys.
* [`lintertypescript`](https://github.com/sebkolind/micro-linter-typescript) - Ability to lint your Typescript (.ts & .tsx) files with tsc.
* [`editorconfig`](https://github.com/10sr/editorconfig-micro) - EditorConfig Support for micro.
* [`lsp`](https://github.com/AndCake/micro-plugin-lsp) - An basic LSP client implementation

### Search

* [`jump`](https://github.com/terokarvinen/micro-jump) - Jump to any function, class or heading with F4. Go, Markdown, Python, C and in 40 other languages.
* [`findinfolder`](https://codeberg.org/micro-plugins/findinfolder/raw/branch/main/repo.json) - Folder search support.
* [`ag`](https://github.com/sebkolind/micro-ag) - This plugin provides the ability to search with "ag" (aka the_silver_searcher).
* [`fzfinder`](https://github.com/MuratovAS/micro-fzfinder) - Integrate fzf to select and search for your project files.
* [`grepsearch`](https://github.com/gaenseklein/grepsearch) - Using grep to recursively search in files.

### File managers

* [`filemanager2`](https://codeberg.org/micro-plugins/filemanager2) - Plugin that allows for easy navigation of a file tree.
* [`filemanager`](https://github.com/NicolaiSoeborg/filemanager-plugin) - A file manager!.
* [`repfiles`](https://github.com/gaenseklein/repfiles) - A filemanager for your git-repository.

### Status bar

* [`gitStatus`](https://codeberg.org/micro-plugins/git-status) - Information about git in status bar.

### Completions

* [`jlabbrev`](https://github.com/MasFlam/jlabbrev) - Provides backslash abbreviations from the julia prompt.

### Languages

* [`nelua`](https://github.com/leapofazzam123/micro-nelua-plugin) - Nelua support for Micro text editor.

### Markdown

* [`preview`](https://github.com/weebi/micro-preview) - A very simple plugin to preview markdown in a second editor pane using pandoc.
* [`mdtree`](https://notabug.org/dustdfg/micro-mdtree) - A plugin for the micro text editor to add sidebar for jumpring and viewing TOC of markdown files.

### Others

* [`splitterm`](https://github.com/lukhof/splitterm) - Run a file or a selection of an inerpreted language within a new terminal window.
* [`quickfix`](https://github.com/serge-v/micro-quickfix) - Adds a functionality similar to VIM quickfix pane.
* [`acme`](https://github.com/xxuejie/micro-acme) - An acme style editing plugin for the micro editor.
* [`emacs_select`](https://github.com/kesslern/micro-emacs-select) - Emacs-style selection for Micro.
* [`delve`](https://github.com/serge-v/micro-delve) - Integrates golang delve debugger.
* [`detectindent`](https://github.com/dmaluka/micro-detectindent) - Automatically detect indentation settings.
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
