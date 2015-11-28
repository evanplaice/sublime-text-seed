import platform
import sys
import os
import subprocess

platform = platform.system()
app_path = ''
config_path = ''

def main():
  if platform == 'Darwin':
    print('OSX detected')
    # TODO: test this in OSX
    app_path = '/Applications/Sublime Text.app'
    # TODO: test this in OSX
    config_path = os.path.expanduser('~') + '/Library/Application Support/Sublime Text 3'
    is_installed(app_path);
    sys.exit(0)

  if platform == 'Linux':
    print('Linux detected...')
    app_path = 'sublime-text'
    config_path = os.path.expanduser('~') + '/.config/sublime-text-3'
    is_installed(app_path);
    sys.exit(0)

  if platform == 'Windows':
    print('Windows detected...')
    # TODO: do a windows instal to determine the default install location
    # app_path = ''
    # TODO: do a windows instal to determine the default config location
    # config_path = ''
    is_installed(app_path);
    sys.exit(0)

  else:
    raise Exception('Operating system not supported');
    sys.exit(1)

def is_installed(app_path):
  try:
    subprocess.call([app_path]);
    print('Sublime is installed...')
    return True

  except OSError as e:
    print('Sublime not installed...')
    return False

if __name__ == '__main__':
  main()