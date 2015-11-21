# SublimeText3 Dev Stack Notes

The following is used to track the plugins, settings, and setup required to get build a producting dev toolstack.

## Workflows

A selection of shortcuts or key combinations that help to speed up workflow in Sublime Text.

**Multiple Cursor Selection**

Hold ```⌘``` while dropping cursors or drag while holding ```⌘ + ⌥```

Use ```^ + ⇧ + w``` to wrap the selection in a tag

To wrap with Emmet use ```^ + w```

**Paste with tab formatting**

Paste content with ```⇧ + ⌘ + v```

**Go to file**

```⌘ + p```

**Go to symbol**

```⌘ + r```

**Line Bubbling**

```⌘ + ^ + ↕```

## Packages

The editor that will be used is Sublime Text. While powerful on its own, the following list of add-ons will be required to unlock the full potential.

### [Package Control](https://packagecontrol.io/)

Package management to simplify the process of adding/removing modules.

**Common Commands**
* Package Control: Install Package (pci)
* Package Control: Remove Package (pcr)

**Package Control.sublime-settings**
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

### [Predawn](https://packagecontrol.io/packages/Predawn)

A stylish low-contrast theme.

**User-Settings**
```json
{
	// predawn theme prerequisites
	"theme": "predawn-DEV.sublime-theme",
	"color_scheme": "Packages/User/SublimeLinter/predawn (SL).tmTheme",
	// highlights modifications prior to a save
	"highlight_modified_tabs": true,
	// tab preferences
	"tab_size": 2,
	"translate_tabs_to_spaces": false,
	// display indent guides
	"indent_guide_options":
	[
		"draw_normal",
		"draw_active"
	],
	// adjust the sidebar appearance
	"sidebar_medium": true,
	// adjust file tab appearance
	"tabs_small": true
	// disable vim-style editing
	"ignored_packages": ["Vintage"]
}
```

### [SublimeLinter](https://packagecontrol.io/packages/SublimeLinter)

The base package required to enable code linting.

### [SublimeLinter-jshint](https://packagecontrol.io/packages/SublimeLinter-jshint)

JavaScript linting for Sublime Text. 

Requires jshint to be installed via NPM (Node Package Manager).

```sudo npm install -g jshint```

### [SublimeLinter-csslint](https://packagecontrol.io/packages/SublimeLinter-csslint)

CSS linting for Sublime Text.

Requires csslint to be installed via NPM (Node Package Manager).

```sudo npm install -g csslint```

### [SublimeLinter-json](https://packagecontrol.io/packages/JSONLint)

JSON linting for Sublime Text.

### [SidebarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements)

Adds additional options to the sidebar.

### [BracketHighlighter](https://packagecontrol.io/packages/BracketHighlighter)

Displays matching brackets to the left of the line numbers. Useful for navigating complex code with multiple layers of nesting.

### [Emmet](https://packagecontrol.io/packages/Emmet)

Used to quickly scaffold html using a shorthand syntax.

Requires NodeJS:csslint

### [AutoPrefixer](https://packagecontrol.io/packages/Autoprefixer)

Automatically adds CSS prefixes required cross browser compatibility.

### [Can I Use](https://packagecontrol.io/packages/Can%20I%20Use)

Used to look up a tag's compatibility.

Triggered via ```^ + ⌥ + f```

### [CodeIntel](https://packagecontrol.io/packages/SublimeCodeIntel)

Code completion for SublimeText.

### [Terminal](https://packagecontrol.io/packages/Terminal)

Launch a terminal window from inside Sublime Text.

### [MarkdownPreview](https://packagecontrol.io/packages/Markdown%20Preview)

Launch a browser tab to preview Markdown from Sublime Text.


### [EditorConfig](https://packagecontrol.io/packages/EditorConfig)

Maintain consistent code formatting/style across multiple editors and developers.

Configured via adding a .editorconfig file to a project.

### [AutoFilename](https://packagecontrol.io/packages/AutoFileName)

Autocompletes filenames used in 'src' or 'href' attributes.

### [GhostText](https://packagecontrol.io/packages/GhostText)

Used to edit text fields in the browser directly in Sublime Text.

Requires a Chrome Extension.

---------

**Plugins worth trying in the future:**

* HTML5Snippets
* SidebarEnhancements?
* ColorHighlighter?
* ColorPicker? ```⌘ + ⇧ + c```
* LiveStyle
* GitGutter
* Expand to Quotes
* ES6 Syntax Highlighting
* CSS3 Syntax Hightlighting