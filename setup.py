import platform
import sys

platform = platform.system()

if platform == 'Darwin':
  print('OSX detected')

  sys.exit(0)

if platform == 'Linux':
  print('Linux detected...')


  sys.exit(0)

if platform == 'Windows':
  print('Windows detected...')

  sys.exit(0)

def isInstalled(platform):

  if platform == 'Darwin':
    return

  if platform == 'Linux':
    return

  if platform == 'Windows':
    return

