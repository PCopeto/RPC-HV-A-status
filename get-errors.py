#!/usr/bin/env python3

from SndCaenManager import SndCaenManager

def main():
  confPath = '../DcsConf/config_SND.toml'
  manager = SndCaenManager(confPath)
  statusLv = manager.getChannelInfo('board', None)
  for ch, st in statusLv.items():
    if st['Status']['value'] != ['On']:
      print(f'LV-{ch} {st["Status"]["value"]}')
  
  statusHv = manager.getChannelInfo('bias', None)
  for ch, st in statusHv.items():
    if st['Status']['value'] != ['On']:
      print(f'HV-{ch} {st["Status"]["value"]}')


if __name__ == '__main__':
  main()
