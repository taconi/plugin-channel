# Micro Plugin Channel

This repository contains the 'channel.json' file which lists all micro plugins. This is where the editor looks to search for plugins to install.

## Settings

Add this repository in ~/.config/settings.json
```json
"pluginchannels": [
    "https://raw.githubusercontent.com/micro-editor/plugin-channel/master/channel.json",
    "https://raw.githubusercontent.com/taconi/plugin-channel/main/channel.json"
]
```

## Plugins

| Plugin          | Description                                             | Link                                                       | 2.0 Support                              |
| --------------- | ------------------------------------------------------- | -------------------------------------------------------    | ---------------------------------------- |
| `icons`         | Icons by type files in status bar.                      | https://gitlab.com/taconi/micro-icons                      | :heavy_check_mark:                       |
| `gloom`         | A dark and gloomy pastel color syntax theme for Micro.  | https://gitlab.com/taconi/micro-gloom                      | :heavy_check_mark:                       |
| `manager`       | Provides a way to manage automatic code formatting.     | https://gitlab.com/taconi/micro-manager                    | :heavy_check_mark:                       |
| `language_ignore` | Adds syntax highlighting to 'ignore' files.           | https://gitlab.com/taconi/micro-language-ignore            | :heavy_check_mark:                       |
| `gitStatus`     | Information about git in status bar.                    | https://gitlab.com/taconi/micro-git-status                 | :heavy_check_mark:                       |
| `yosyslint`  | Plugin for checking the syntax of the Verilog language. Based on yosys | https://github.com/MuratovAS/micro-yosyslint   | :heavy_check_mark:                       |
| `fzfinder` | The plugin allows you to integrate fzf to select and search for your project files | https://github.com/MuratovAS/micro-fzfinder | :heavy_check_mark: |
| `splitterm` | Run a file or a selection of an inerpreted language within a new terminal window. | https://github.com/lukhof/splitterm | :heavy_check_mark: |
| `ag` | This plugin provides the ability to search with "ag" (aka the_silver_searcher). | https://github.com/sebkolind/micro-ag | :heavy_check_mark: |
| `prettier` | This plugin provides the ability to format your code with Prettier. | https://github.com/sebkolind/micro-prettier | :heavy_check_mark: |
| `lintertypescript` | Ability to lint your Typescript (.ts & .tsx) files with tsc. | https://github.com/sebkolind/micro-linter-typescript | :heavy_check_mark: |
| `acme` | An acme style editing plugin for the micro editor. | https://github.com/xxuejie/micro-acme | :heavy_check_mark: |
| `nelua` | Nelua support for Micro text editor | https://github.com/leapofazzam123/micro-nelua-plugin | :heavy_check_mark: |
| `emacs_select` | Emacs-style selection for Micro | https://github.com/kesslern/micro-emacs-select | :heavy_check_mark: |
| `darken` | Plugin with colorscheme of micro editor. | https://github.com/informeai/darken | :heavy_check_mark: |
| `delve` | Integrates golang delve debugger | https://github.com/serge-v/micro-delve | :heavy_check_mark: |
| `bookmarks` | Support for adding bookmarks while editing. | https://github.com/davidalbertainley/micro-bookmarks-plugin | :x: |
| `exec` | Run the code you edit and show the results directly in the editor. | https://github.com/ibotdeu/exec-plugin | :x: |
| `autosave` | This plugin will let you automatically save on focus lost, or 5 seconds after your last edit. | https://github.com/transmutrix/micro-plugin-autosave | :x: |
| `mcompiler` | Simple plugin to compile code | https://github.com/joselbr2099/mcompiler |:x: |
| `sunny-day` | Port of the Emacs theme by Martin Haesler | https://github.com/dwwmmn/micro-sunny-day | :heavy_check_mark: |
| `ctags`         | This plugin adds (rudimentary) support for reading/parsing a ctags file. | https://github.com/codezapper/micro-ctags-plugin | :x:  |
| `comment`       | Plugin to auto comment or uncomment lines               | https://github.com/micro-editor/comment-plugin             | :heavy_check_mark: (provided by default) |
| `snippets`      | Provides snippets functionality                         | https://github.com/micro-editor/updated-plugins/tree/master/micro-snippets-plugin         | :heavy_check_mark:                       |
| `go`            | Provides `gofmt` and `goimports` support for Go files   | https://github.com/micro-editor/go-plugin                  | :heavy_check_mark:                       |
| `fish`          | Provides `fishfmt` support for Fish files               | https://github.com/onodera-punpun/micro-fish-plugin        | :heavy_check_mark:                       |
| `wc`            | Plugin to count words/characters                        | https://github.com/adamnpeace/micro-wc-plugin              | :heavy_check_mark:                       |
| `fzf`           | Provides `fzf` support for opening files                | https://github.com/samdmarshall/micro-fzf-plugin           | :heavy_check_mark:                       |
| `pony`          | Provides auto-indentation for Pony files                | https://github.com/Theodus/micro-pony-plugin               | :heavy_check_mark:                       |
| `editorconfig`  | EditorConfig Support for micro                          | https://github.com/10sr/editorconfig-micro                 | :heavy_check_mark:                       |
| `crystal`       | Provides various `crystal` tools for crystal files      | https://github.com/ColinRioux/micro-crystal                | :heavy_check_mark:                       |
| `gotham-colors` | A colorscheme for code that never sleeps in Gotham City | https://github.com/novln/micro-gotham-colors               | :heavy_check_mark: (provided by default) |
| `misspell`      | Plugin that corrects commonly misspelled words          | https://github.com/onodera-punpun/micro-misspell-plugin    | :heavy_check_mark:                       |
| `monokai-dark`  | A dark monokai colorscheme                              | https://github.com/Theodus/micro-monokai-dark              | :heavy_check_mark: (provided by default) |
| `scratch`       | Plugin to create scratch buffers                        | https://github.com/samdmarshall/micro-scratch-plugin       | :x:                                      |
| `manipulator`   | Extend text manipulation abilities                      | https://github.com/NicolaiSoeborg/manipulator-plugin       | :heavy_check_mark:                       |
| `filemanager`   | A file manager!                                         | https://github.com/NicolaiSoeborg/filemanager-plugin       | :heavy_check_mark:                       |
| `vcs`           | Mark changed lines in Git or Mercurial repositories     | https://bitbucket.org/dermetfan/micro-vcs                  | :heavy_check_mark: (provided by default) |
| `fmt`           | A multi-language formatting plugin                      | https://github.com/sum01/fmt-micro                         | :x:                                      |
| `joinLines`     | Plugin which joins selected lines or the following with the current | https://github.com/Lisiadito/join-lines-plugin | :heavy_check_mark:                       |
| `bounce`     | Plugin that implements nano-style smart home and bouncing the cursor between matching-brackets | https://github.com/deusnefum/micro-bounce | :heavy_check_mark:                       |
| `quoter`     | Plugin that allows you to add quotes or brackets around selected text | https://github.com/deusnefum/micro-quoter | :heavy_check_mark:                       |
| `zigfmt`        | Provides `zig fmt` integration for Zig files            | https://github.com/squeek502/micro-zigfmt                  | :heavy_check_mark:                       |
| `jlabbrev`      | Provides backslash abbreviations from the julia prompt  | https://github.com/MasFlam/jlabbrev                        | :heavy_check_mark:                       |
| `nord-colors`   | A set of dark and light colorschemes based on Nord      | https://github.com/KiranWells/micro-nord-tc-colors         | :heavy_check_mark:                       |
| `yapf`          | Runs `yapf` in place when saving python files           | https://github.com/a11ce/micro-yapf                        | :heavy_check_mark:                       |
| `bookmark`      | Bookmark lines to quickly jump between saved positions  | https://github.com/haqk/micro-bookmark                     | :heavy_check_mark:                       |
| `quickfix`      | Adds a functionality similar to VIM quickfix pane       | https://github.com/serge-v/micro-quickfix                  | :heavy_check_mark:                       |
| `jump`      | Jump to any function, class or heading with F4. Go, Markdown, Python, C and in 40 other languages | https://github.com/terokarvinen/micro-jump   | :heavy_check_mark:      |
| `detectindent`  | Automatically detect indentation settings               | https://github.com/dmaluka/micro-detectindent              | :heavy_check_mark:                       |
| `language-env`  | Syntax highlighting for files with .env extension       | https://gitlab.com/taconi/micro-language-env               | :heavy_check_mark:                       |
| `findinfolder`  | Folder search support                                   | https://gitlab.com/taconi/micro-findinfolder               | :heavy_check_mark:                       |


## Adding your own plugin

Collaboration is super welcome! See [CONTRIBUTING.md](https://github.com/taconi/plugin-channel/blob/main/CONTRIBUTING.md).
