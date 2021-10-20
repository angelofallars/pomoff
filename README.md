<h1 align="center">🍅 Pomoff</h1>

<img src="https://i.imgur.com/nXkjOqU.png" alt="pomoff command line interface" align="right" height="240px">

**Pomoff**, a minimalist Pomodoro timer made in `Python`.

- Configurable durations for work, short break and long break in config.py
- Sound + notifications when each interval is done
- Easy to hack and make your own changes

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Installation

```bash
git clone https://github.com/angelofallars/pomoff
cd pomoff
bash ./install.sh
```

To uninstall, run `bash ./uninstall.sh`.

## Dependencies

- `python3`
- `mpv`

## Run

After installing, simply type `pomoff` into the command line.

```bash
Usage: pomoff [option] ...
  -h, help               see this help page
  -w, work               launch a work interval
  -b, break, shortbreak  launch a short break interval
 -lb, longbreak          launch a long break interval

The config file is located in the /config directory of the pomoff folder.
```

## Configuration

In the `config.py` file, you can edit the duration of the work and break
intervals, change the sound and volume of the end-of-interval bell and more.

## Contributing

Have any ideas on how to make the code better? Feel free to contribute code by
making a fork and a pull request on the `dev` branch.

<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
