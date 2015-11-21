#!/bin/bash

# sublime.sh - Setup sublime symlink, theme, packages, and preferences

# OSX Setup
if [[ "$OSTYPE" == "darwin" ]]; then
	echo "Setting up Sublime Text 3 for OSX"
	ST3="${HOME}/Library/Application Support/Sublime Text 3"
	echo "------------------------"
	echo "Symlinking the SublimeText.app to 'sublime'..."
	ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime

# Linux Setup
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	echo "Setting up Sublime Text 3 for Linux"
	ST3=${HOME}/.config/sublime-text-3
	echo "------------------------"
fi

# create the 'Installed Packages' directory
mkdir -p "${ST3}/Installed Packages"

echo "Copying Themes..."
cp -a ./themes/* "${ST3}/Installed Packages"
mkdir -p "${ST3}/Installed Packages"

echo "Installing Package Control..."
curl http://sublime.wbond.net/Package%20Control.sublime-package > "${ST3}/Installed Packages/Package Control.sublime-package"

echo "Copying User Settings..."
mkdir -p "${ST3}/Packages/User"
cp -a ./user-settings/* $ST3/Packages/User