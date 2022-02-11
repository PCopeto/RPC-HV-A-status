#!/usr/bin/env python3

from SndCaenManager import SndCaenManager

def main():
  confPath = 'config_test.toml'
  manager = SndCaenManager(confPath)
  manager.clearAlarm()


if __name__ == '__main__':
  main()