<h1 align="center">🍅 Pomoff</h1>

<img src="https://i.imgur.com/nXkjOqU.png" alt="pomoff command line interface" align="right" height="240px">

**Pomoff**, a minimalist Pomodoro timer made in `Python`.

- Configurable durations for work, short break and long break in config.py
- Sound + notifications when each interval is done
- Easy to hack and make your own changes

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Installation

### [Axyl OS](https://axyl-os.github.io/)

`sudo pacman -S axyl-pomoff-git`

### Other operating systems (Linux)

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

Just make sure to develop and make pull requests on the `dev` branch instead of
the `main` branch.

**Contribute to pomoff and get your awesome profile picture displayed here!**

<a href="https://github.com/angelofallars/pomoff/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=angelofallars/pomoff" />
</a>

*Made with [contrib.rocks](https://contrib.rocks).*

## Supporting this project

This project is free and open-source and will always be that way.

If you like this project, please consider donating to help me improve this project even further.

<a href="https://www.buymeacoffee.com/angelofallaria" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" width="140"></a>

<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
