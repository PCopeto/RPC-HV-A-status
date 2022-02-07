# PSU control

## set-channel-lv.py
Turn on and off the LV for the boards.
The first argument is either `on` or `off`. Then a list of boards must be provided.

Usage example:
```bash
./set-channel-lv.py [on/off] [boards...]
./set-channel-lv.py on scifi_1x1 scifi_1x2
./set-channel-lv.py off all
```

The boards are listed in the configuration file, as `[board.<name>]`. The naming convention is:
* `scifi_nxm`, with `n` the the station number `1` to `5`, `x` either `x` or `y` and m the board number `1` to `3`. For example: `scifi_5x2`.
* `usn`, with `n=1...3` for the upstream.
* `dsn`, with `n=1...3` for the downstream.
* `veto` for the veto.

The word `all` can be used instead of a list of all the boards.

## set-channel-hv.py
Sets the HV.
The first argument is either `off`, `idle` (used for calibration) or `operation` (used for DCR scan and data taking). Then a list of boards must be provided.

Usage example:
```bash
./set-channel-hv.py [off/idle/operation] [boards...]
./set-channel-hv.py idle scifi_1x1 us1_rl ds3_v
./set-channel-hv.py off all
```

The boards are listed in the configuration file, as `[bias.<name>]`. The naming convention is:
* `scifi_nxm`, with `n` the the station number `1` to `5`, `x` either `x` or `y` and m the board number `1` to `3`. For example: `scifi_5x2`.
* `usn_ab`, with `n=1...5` is the upstream module, `a=l/r` for left and right, `b=l/s` for the large and small SiPMs. E.g. `us2_ls` is upstream 2 left, small SiPMs.
* `dsn_a`, with `n=1...4` is the downstream module, `a=l/r/` for left, right and vertical. For example `ds4_v` is the last DS vertical plane
* `veto_na` with `n=1,2` and `a=l/r`. E.g. `veto_2r`.

The word `all` can be used instead of a list of all the boards.
