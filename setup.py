import platform
import sys
import os
import signal
import subprocess

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
    config_path = os.path.expanduser('~') + '/Library/Application Support/Sublime Text 3' # TODO: test this in OSX
    if not is_installed(app_path):
      install_osx(app_path)
    config_osx(config_path)
    sys.exit(0)
  # Linux Setup:
  # - check and install via `brew cask`
  # - copy configuration to '~/.config/sublime-text-3'
  if platform == 'Linux':
    print('Linux detected...')
    app_path = 'sublime'
    config_path = os.path.expanduser('~') + '/.config/sublime-text-3'
    if not is_installed(app_path):
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
      install_windows(app_path)
    config_windows(config_path)
    sys.exit(0)
  else:
    raise Exception('Operating system not supported');
    sys.exit(1)


# Check to see if an application is installed
def is_installed(app_path):
  try:
    p = subprocess.Popen(app_path)
    os.kill(p.pid, signal.SIGTERM)
    print('Sublime is installed...')
    return True
  except OSError as e:
    print('Sublime not installed...')
    return False


# OSX installation instructions
def install_osx(app_path):
  try:
    print('Updating sources...')
    if not is_installed('brew cask'):
      raise NotInstalledError('Homebrew not installed...')
    subprocess.call(['brew', 'update'], stdout=subprocess.PIPE)
    if not is_installed('brew cask'):
      raise NotInstalledError('Brew Cask not installed...')
    print('Installing Sublime Text...')
    os.environ['HOMEBREW_CASK_OPTS'] = '--appdir=/Applications'
    subprocess.call(['brew', 'cask', 'install', 'sublime-text3'], stdout=subprocess.PIPE)
    # symlink to 'sublime'
    subprocess.Popen('ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/sublime')
    print('Installation complete...')
  except Exception as e:
    print('Install failed:' + e)
    sys.exit(1)


# OSX configuration instructions
def config_osx(config_path):
  # TODO: implement OSX config
  return


# Linux installation instructions
def install_linux(app_path):
  try:
    print('Updating sources...')
    subprocess.call(['apt-get', 'update'], stdout=subprocess.PIPE)
    print('Installing Sublime Text...')
    subprocess.call(['apt-get', 'install', 'sublime-text'], stdout=subprocess.PIPE)
    print('Installation complete...')
  except OSError as e:
    print('Install failed:' + e)
    sys.exit(1)


# Linux configuration instructions
def config_linux(config_path):
  # TODO: implement Linux config
  return


# Windows installation instructions
def install_windows(app_path):
  # TODO: implement Windows installation
  return


# Windows configuration instructions
def config_windows(config_path):
  # TODO: implement Windows config
  return


class NotInstalledError(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)


if __name__ == '__main__':
  main()
