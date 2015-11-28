import platform
import sys
import subprocess

platform = platform.system()
app_path = ''

def main():
  if platform == 'Darwin':
    print('OSX detected')
    is_installed(app_path);
    sys.exit(0)

  if platform == 'Linux':
    print('Linux detected...')
    is_installed(app_path);
    sys.exit(0)

  if platform == 'Windows':
    print('Windows detected...')
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