#!/usr/bin/env python

import platform
import sys
import os
import signal
import subprocess
import errno
import shutil
import urllib2


platform = platform.system()
app_path = ''
config_path = ''

# the application main entry point
def main():
  # OSX Setup:
  # - check and install via `brew cask`
  # - copy configuration to '/Library/Application Support/Sublime Text 3'
  if platform == 'Darwin':
    print('OSX detected')
    app_path = '/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl'
    config_path = os.path.expanduser('~') + '/Library/Application Support/Sublime\ Text\ 3' # TODO: test this in OSX
    if not is_installed(app_path):
      print('Sublime not installed...')
      install_osx(app_path)
    config_osx(config_path)
    sys.exit(0)
  # Linux Setup:
  # - check and install via `apt-get`
  # - copy configuration to '~/.config/sublime-text-3'
  if platform == 'Linux':
    print('Linux detected...')
    app_path = 'sublime'
    config_path = os.path.expanduser('~') + '/.config/sublime-text-3'
    if not is_installed(app_path):
      print('Sublime not installed...')
      install_linux(app_path)
    config_linux(config_path)
    sys.exit(0)
  # Windows Setup:
  # - check and notify user to install
  # - copy configuration to '%APPDATA%\Sublime Text 3'
  if platform == 'Windows':
    print('Windows detected...')
    # TODO: do a windows install to determine the default install location
    # app_path = ''
    # TODO: do a windows install to determine the default config location
    # config_path = ''
    if not is_installed(app_path):
      print('Sublime not installed...')
      install_windows(app_path)
    config_windows(config_path)
    sys.exit(0)
  else:
    raise Exception('Operating system not supported');
    sys.exit(1)


# Check to see if an application is installed
def is_installed(app_path):
  try:
    p = subprocess.Popen(app_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.kill(p.pid, signal.SIGTERM)
    return True
  except OSError as e:
    return False


# create a directory if it doesn't already exist
def make_dir(dir):
  try:
    os.makedirs(dir)
  # capture any non-file-creation errors
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise


# recursively copies all the files in a directory
#  required because shutil.copytree (sucks) can't overwrite directories
def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
      try:
        shutil.copytree(s, d, symlinks, ignore)
      except OSError as exception:
        if exception.errno != errno.EEXIST:
          raise
    else:
      shutil.copy2(s, d)


def install_package_control(config_path):
  path = config_path + '/Installed Packages/Package Control.sublime-package'
  url = 'http://sublime.wbond.net/Package%20Control.sublime-package'
  response = urllib2.urlopen(url)
  CHUNK = 16 * 1024
  with open(path, 'wb') as f:
   while True:
      chunk = response.read(CHUNK)
      if not chunk: break
      f.write(chunk)

# OSX installation instructions
def install_osx(app_path):
  try:
    if not is_installed(['brew', 'help', '&>/dev/null']):
      raise NotInstalledError('Error: Homebrew required to install Sublime Text.')
    print('Updating sources...')
    subprocess.call(['brew', 'update'], stdout=subprocess.PIPE)
    print('Installing Sublime Text...')
    os.environ['HOMEBREW_CASK_OPTS'] = '--appdir=/Applications'
    subprocess.call(['brew', 'install', 'caskroom/cask/brew-cask'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(['brew', 'tap', 'caskroom/versions'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(['brew', 'cask', 'install', 'sublime-text3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # symlink to 'sublime'
    subprocess.Popen(['ln', '-s', app_path, '/usr/local/bin/sublime'])
    print('Installation complete...')
  except Exception as e:
    print(e)
    sys.exit(1)


# OSX configuration instructions
def config_osx(config_path):
  packages = config_path + '/Installed\ Packages'
  settings = config_path + '/Packages/User'
  # create the settings directories
  make_dir(config_path)
  make_dir(packages)
  make_dir(settings)
  # copy the themes
  copytree('./themes', packages)
  # copy the user preferences
  copytree('./user-settings', settings)
  print('Configuration complete...')


# Linux installation instructions
def install_linux(app_path):
  try:
    subprocess.call(['sudo', 'id', '-nu'], stdout=subprocess.PIPE)
    print('Updating sources...')
    subprocess.call(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE)
    print('Installing Sublime Text...')
    subprocess.call(['sudo', 'apt-get', 'install', 'sublime-text'], stdout=subprocess.PIPE)
    print('Installation complete...')
  except OSError as e:
    print(e)
    sys.exit(1)


# Linux configuration instructions
def config_linux(config_path):
  packages = config_path + '/Installed Packages'
  settings = config_path + '/Packages/User'
  # create the settings directories
  make_dir(config_path)
  make_dir(packages)
  make_dir(settings)
  print('Installing Package Control...')
  install_package_control(config_path)
  # copy the themes
  copytree('./themes', packages)
  # copy the user preferences
  copytree('./user-settings', settings)
  print('Configuration complete...')


# Windows installation instructions
def install_windows(app_path):
  # TODO: implement Windows installation
  return


# Windows configuration instructions
def config_windows(config_path):
  # TODO: implement Windows config
  return


class NotInstalledError(Exception):
  pass


if __name__ == '__main__':
  main()
