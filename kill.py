#!/usr/bin/env python3

from SndCaenManager import SndCaenManager

def main():
  confPath = 'config_SND.toml'
  manager = SndCaenManager(confPath)
  manager.kill()


if __name__ == '__main__':
  main()