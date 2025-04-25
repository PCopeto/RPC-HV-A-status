#!/usr/bin/env python3

import argparse
from SndCaenManager import SndCaenManager
import json
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Read HV and current values and save to a file.')
    parser.add_argument('channels', type=str, nargs='+', help='List of channels to read (or "all").')
    parser.add_argument('-o', '--output', type=str, default='hv_readings.json', help='Output filename.')
    args = parser.parse_args()

    if 'all' in args.channels:
        args.channels = None

    confPath = '../DcsConf/config_SND.toml'
    manager = SndCaenManager(confPath)

    data = manager.getChannelInfo('bias', args.channels)

    timestamp = datetime.now().isoformat()
    output_data = {
        "timestamp": timestamp,
        "channels": data
    }

    with open(args.output, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"HV and current values saved to {args.output}")

if __name__ == '__main__':
    main()

