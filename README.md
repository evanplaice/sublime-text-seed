# Sublime Text Seed

Automated installation + configuration of Sublime Text in OSX, Linux, and Windows.

The setup script loads a 'seed' configuration. Meaning, it provides a quick/easy path for new and existing `Sublime Text` users to quickly get up and running.

*This package:*

 1. Installs `Sublime Text 3`
 2. Installs `Package Control`
 3. `./themes` -> Loads Themes
 4. `./user-settings` -> Loads Configuration files
 5. `./license` -> Loads License

The setup script works transparently across all platforms by leveraging python as well as OS-specific package managers.


# Usage

Run the following to install and config `Sublime Text`

```bash
./setup.py
```

Restart the editor when prompted to do so. To view the package installation progress open the `Sublime Text` console.

*Note: This WILL overwrite the existing configuration but it will prompt before replacing the license.*


# Configuration

A default configuration is included with this package. Feel free to fork the project and add your own custom configuration.


# General Settings

*User-Settings*
```json
{
	"highlight_modified_tabs": true,
	"tab_size": 2,
	"translate_tabs_to_spaces": true,
	"draw_white_space": "all",
	"indent_guide_options":
	[
		"draw_normal",
		"draw_active"
	],
	"ignored_packages": [
		"Vintage"
	]
}
```

*Note: Tabs aren't translated to spaces by default to avoid introducing unrelated changes to a commit while editing preexisting codebases.*


## Themes

### [Predawn](https://packagecontrol.io/packages/Predawn)

A stylish low-contrast theme.

*User-Settings*
```json
{
	"theme": "predawn-DEV.sublime-theme",
	"color_scheme": "Packages/User/SublimeLinter/predawn (SL).tmTheme"
}
```


## Packages

Sublime Text is powerful on its own but the following add-ons unlock the full potential.

### [Package Control](https://packagecontrol.io/)

Package management to simplify the process of adding/removing modules.

**Common Commands**
* Package Control: Install Package (`Command Palette + p + c + i`)
* Package Control: Remove Package (`Command Palette + p + c + r`)

*Package Control-Settings*
```json
{
	"installed_packages":
	[
		"Package Control",
		"Predawn",
		"Emmet",
		"EditorConfig",
		"SublimeCodeIntel",
		"AutoFileName",
		"Autoprefixer",
		"Can I Use",
		"GhostText",
		"Markdown Preview", 
		"SideBarEnhancements",
		"SideBarGit",
		"Terminal",
		"BracketHighlighter",
		"SublimeLinter",
		"SublimeLinter-csslint",
		"SublimeLinter-jshint",
		"SublimeLinter-json"
	]
}
```

## Package Details

### [SublimeLinter](https://packagecontrol.io/packages/SublimeLinter)

Base package required to enable linting in SublimeText3.

*Note: Since the 3.x release of `Sublime Text`, SublimeLinter no longer includes linters for specific languages by default.*

### [SublimeLinter-jshint](https://packagecontrol.io/packages/SublimeLinter-jshint)

JavaScript linting for Sublime Text. 

Requires jshint to be installed via NPM (Node Package Manager).

```bash
sudo npm install -g jshint
```

### [SublimeLinter-csslint](https://packagecontrol.io/packages/SublimeLinter-csslint)

CSS linting for Sublime Text.

Requires csslint to be installed via NPM (Node Package Manager).

```bash
sudo npm install -g csslint
```

### [SublimeLinter-json](https://packagecontrol.io/packages/JSONLint)

JSON linting for Sublime Text.

### [SidebarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements)

Adds additional options to the sidebar.

The following settings are included to improve the look-and-feel.

*User-Settings*
```json
{
	"sidebar_medium": true,
	"tabs_small": true
}
```

### [BracketHighlighter](https://packagecontrol.io/packages/BracketHighlighter)

Displays matching brackets to the left of the line numbers.

Useful for navigating complex code with multiple layers of nesting.

### [Emmet](https://packagecontrol.io/packages/Emmet)

Used to quickly scaffold html using a shorthand syntax.

### [AutoPrefixer](https://packagecontrol.io/packages/Autoprefixer)

Automatically adds CSS prefixes required cross browser compatibility.

### [Can I Use](https://packagecontrol.io/packages/Can%20I%20Use)

Used to look up a tag's compatibility.

Triggered via `^ + ⌥ + f` | `CTRL + ALT + f`

### [CodeIntel](https://packagecontrol.io/packages/SublimeCodeIntel)

Code completion for SublimeText.

### [Terminal](https://packagecontrol.io/packages/Terminal)

Launch a terminal window from inside Sublime Text.

### [MarkdownPreview](https://packagecontrol.io/packages/Markdown%20Preview)

Launch a browser tab to preview Markdown from Sublime Text.

Available via the Command Palette (ie `⌘ + ⇧ + p` | `SUPER + SHIFT + p`)

Use `Command Palette + m + b + p` as a shortcut to quickly preview a Markdown file in the browser.

### [EditorConfig](https://packagecontrol.io/packages/EditorConfig)

Maintain consistent code formatting/style across multiple editors and developers.

Configured by including an `.editorconfig` file the project root.

To determine which settings to use see the [Official Documentation](http://editorconfig.org/).

### [AutoFilename](https://packagecontrol.io/packages/AutoFileName)

Autocompletes filenames used in 'src' or 'href' attributes.

### [GhostText](https://packagecontrol.io/packages/GhostText)

Used to edit text fields in the browser directly in Sublime Text.

Select a textarea, start the plugin in Chrome, and code edited directly in `Sublime Text` will be reflected in the textarea.

Requires a Chrome Extension.

### [LiveReload](https://packagecontrol.io/packages/GhostText) [Not Installed]

Automatically reloads the browser when files are saved in SublimeText.

Requires a Chrome Extension.

*Note: Not available in Linux or Windows. Install manually via `Package Control` to use in OSX.*
