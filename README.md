# Micro Plugin Channel

This repository contains the `channel.json` file which lists all micro plugins. This is where the editor looks to search for plugins to install.

#### This is a [oficial channel](https://github.com/micro-editor/plugin-channel/) fork.


## Settings

Add this repository in `~/.config/micro/settings.json`
```json
"pluginchannels": [
    "https://raw.githubusercontent.com/micro-editor/plugin-channel/master/channel.json",
    "https://raw.githubusercontent.com/taconi/plugin-channel/main/channel.json"
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
* [Others](#others)
----

### Text utils
  - [`snippets`](https://github.com/micro-editor/updated-plugins/tree/master/micro-snippets-plugin) - Provides snippets functionality.
  - [`wc`](https://github.com/adamnpeace/micro-wc-plugin) - Plugin to count words/characters.
  - [`manipulator`](https://github.com/NicolaiSoeborg/manipulator-plugin) - Extend text manipulation abilities.
  - [`manipulator2`](https://github.com/taconi/micro-manipulator2) - Text manipulation functions.
  - [`joinLines`](https://github.com/Lisiadito/join-lines-plugin) - Plugin which joins selected lines or the following with the current.
  - [`bounce`](https://github.com/deusnefum/micro-bounce) - Plugin that implements nano-style smart home and bouncing the cursor between matching-brackets.
  - [`quoter`](https://github.com/deusnefum/micro-quoter) - Plugin that allows you to add quotes or brackets around selected text.
  - [`bookmark`](https://github.com/haqk/micro-bookmark) - Bookmark lines to quickly jump between saved positions.
  - [`capitalizer`](https://github.com/CodeGiorgino/capitalizer) - A simple micro-editor plugin that allows to capitalize selected text.
  - [`align`](https://github.com/mosskjohnson/align-plugin) - Simple plugin to align multiple cursors in micro..

### Colorschemes
  - [`gloom`](https://gitlab.com/taconi/micro-gloom) - A dark and gloomy pastel color syntax theme for Micro.
  - [`darken`](https://github.com/taconi/micro-darken) - Plugin with colorscheme of micro editor.
  - [`nord-colors`](https://github.com/KiranWells/micro-nord-tc-colors) - A set of dark and light colorschemes based on Nord.
  - [`sunny-day`](https://github.com/dwwmmn/micro-sunny-day) - Port of the Emacs theme by Martin Haesler.

### Syntax highlightings
  - [`language_ignore`](https://gitlab.com/taconi/micro-language-ignore) - Adds syntax highlighting to 'ignore' files.
  - [`language-env`](https://gitlab.com/taconi/micro-language-env) - Syntax highlighting for files with .env extension.

### Formattings
  - [`go`](https://github.com/micro-editor/go-plugin) - Provides `gofmt` and `goimports` support for Go files.
  - [`manager`](https://gitlab.com/taconi/micro-manager) - Provides a way to manage automatic code formatting.
  - [`prettier`](https://github.com/sebkolind/micro-prettier) - This plugin provides the ability to format your code with Prettier.
  - [`zigfmt`](https://github.com/squeek502/micro-zigfmt) - Provides `zig fmt` integration for Zig files.
  - [`yapf`](https://github.com/a11ce/micro-yapf) - Runs `yapf` in place when saving python files.

### Linters
  - [`yosyslint`](https://github.com/MuratovAS/micro-yosyslint) - Plugin for checking the syntax of the Verilog language. Based on yosys.
  - [`lintertypescript`](https://github.com/sebkolind/micro-linter-typescript) - Ability to lint your Typescript (.ts & .tsx) files with tsc.
  - [`editorconfig`](https://github.com/10sr/editorconfig-micro) - EditorConfig Support for micro.
  - [`lsp`](https://github.com/AndCake/micro-plugin-lsp) - An basic LSP client implementation

### Search
  - [`jump`](https://github.com/terokarvinen/micro-jump) - Jump to any function, class or heading with F4. Go, Markdown, Python, C and in 40 other languages.
  - [`findinfolder`](https://gitlab.com/taconi/micro-findinfolder) - Folder search support.
  - [`ag`](https://github.com/sebkolind/micro-ag) - This plugin provides the ability to search with "ag" (aka the_silver_searcher).
  - [`fzfinder`](https://github.com/MuratovAS/micro-fzfinder) - Integrate fzf to select and search for your project files.

### File managers
  - [`filemanager2`](https://gitlab.com/taconi/micro-filemanager2) - Plugin that allows for easy navigation of a file tree.
  - [`filemanager`](https://github.com/NicolaiSoeborg/filemanager-plugin) - A file manager!.

### Status bar
  - [`icons`](https://gitlab.com/taconi/micro-icons) - Icons by type files in status bar.
  - [`gitStatus`](https://gitlab.com/taconi/micro-git-status) - Information about git in status bar.

### Completions
 - [`jlabbrev`](https://github.com/MasFlam/jlabbrev) - Provides backslash abbreviations from the julia prompt.

### Languages
  - [`nelua`](https://github.com/leapofazzam123/micro-nelua-plugin) - Nelua support for Micro text editor.

### Others
  - [`splitterm`](https://github.com/lukhof/splitterm) - Run a file or a selection of an inerpreted language within a new terminal window.
  - [`quickfix`](https://github.com/serge-v/micro-quickfix) - Adds a functionality similar to VIM quickfix pane.
  - [`acme`](https://github.com/xxuejie/micro-acme) - An acme style editing plugin for the micro editor.
  - [`emacs_select`](https://github.com/kesslern/micro-emacs-select) - Emacs-style selection for Micro.
  - [`delve`](https://github.com/serge-v/micro-delve) - Integrates golang delve debugger.
  - [`detectindent`](https://github.com/dmaluka/micro-detectindent) - Automatically detect indentation settings.
  - [`wakatime`](https://github.com/wakatime/micro-wakatime) - Metrics, insights, and time tracking automatically generated from your programming activity.
  - [`run`](https://github.com/terokarvinen/micro-run) - F5 to save and run, F12 to 'make', F9 to 'make' in background. Go, Python, Lua and executable file (#!) supported. Can 'make' whole project even from subdir.
  - [`cheat`](https://github.com/terokarvinen/micro-cheat) - F1 cheatsheet for the language you're editing: Python, Go, Lua...
  - [`palettero`](https://github.com/terokarvinen/palettero) - Command palette - Ctrl-P to fuzzy search & run commands, textfilters and descriptions
  - [`gzplugin`](https://github.com/dzmanto/gzplugin4micro) - Read and write .gzip files.


## Adding your own plugin

Collaboration is super welcome! See [CONTRIBUTING.md](https://github.com/taconi/plugin-channel/blob/main/CONTRIBUTING.md).
