#!/usr/bin/env python3

import argparse
from SndCaenManager import SndCaenManager

def main():
  parser = argparse.ArgumentParser('Setting the LV')
  parser.add_argument('mode', type=str, help='The operaton mode (\'off\' or \'on\')')
  parser.add_argument('channels', type=str, nargs='+', help='List the channels to be switched.')
  args = parser.parse_args()

  if 'all' in args.channels:
    args.channels = None

  confPath = 'config_SND.toml'
  manager = SndCaenManager(confPath)
  manager.switchLV(args.mode == 'on', args.channels)


if __name__ == '__main__':
  main()