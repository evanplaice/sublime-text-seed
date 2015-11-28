import platform
import sys

platform = platform.system()

def main():
  if platform == 'Darwin':
    print('OSX detected')
    sys.exit(0)

  if platform == 'Linux':
    print('Linux detected...')
    sys.exit(0)

  if platform == 'Windows':
    print('Windows detected...')
    sys.exit(0)

  else:
    raise Exception('Operating system not supported');
    sys.exit(1)

if __name__ == '__main__':
  main()