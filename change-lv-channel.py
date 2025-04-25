#!/usr/bin/env python3

import argparse
from SndCaenManager import SndCaenManager
import json

def main():
  parser = argparse.ArgumentParser('Get the LV status')
  parser.add_argument('channels', type=str, nargs='+', help='List the channels to be returned.')
  args = parser.parse_args()

  print(args.channels)

  if 'all' in args.channels:
    args.channels = None
  
  confPath = '../DcsConf/config_SND.toml'
  manager = SndCaenManager(confPath)
  print(json.dumps(manager.getChannelInfo('board', args.channels)))


if __name__ == '__main__':
  main()