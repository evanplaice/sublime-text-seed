#!/bin/bash

# sublime.sh - Setup sublime symlink, theme, packages, and preferences

isInstalled() {
	if hash $1 2>/dev/null; then
		echo "${1} is installed..."
		return 1
	else
		echo "${1} is not installed..."
		return 0
	fi
}

# OSX Setup
if [[ "$OSTYPE" == "darwin" ]]; then
	echo "Setting up Sublime Text 3 for OSX"
	ST3="${HOME}/Library/Application Support/Sublime Text 3"
	echo "------------------------"
	echo "Symlinking the SublimeText.app to 'sublime'..."
	ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime

# Linux Setup
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
	echo "------------------------"	
	echo "Setting up Sublime Text 3 for Linux"
	echo "------------------------"

	# save the config directory for Sublime Text settings
	ST3=${HOME}/.config/sublime-text-3

	# install sublime text if it's missing
	if isInstalled sublime -eq 0; then
		echo "------------------------"	
		echo "Installing Sublime Text..."
		echo ""
		apt-get install sublime-text &
		wait %1
		# prepare the sublime settings directory
		mkdir ${ST3}
	fi
fi

# prepare the 'Installed Packages' directory
mkdir -p "${ST3}/Installed Packages"

echo "------------------------"
echo "Copying Themes..."
mkdir -p "${ST3}/Installed Packages"
cp -a ./themes/* "${ST3}/Installed Packages"
echo "------------------------"

echo "Installing Package Control..."
echo ""
curl http://sublime.wbond.net/Package%20Control.sublime-package > "${ST3}/Installed Packages/Package Control.sublime-package"
echo "------------------------"

echo "Copying User Settings..."
# prepare the 'Packages' directory
mkdir -p "${ST3}/Packages/User"
cp -a ./user-settings/* $ST3/Packages/User
echo "------------------------"

exit 0
