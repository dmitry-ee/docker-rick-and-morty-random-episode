# Rick and Morty episode Randomizer
[![image version](https://img.shields.io/docker/v/dmi7ry/rick-and-morty-random-episode?sort=semver)](https://hub.docker.com/r/dmi7ry/time-exporter)
[![Image Pulls](https://img.shields.io/docker/pulls/dmi7ry/rick-and-morty-random-episode.svg)](https://hub.docker.com/r/dmi7ry/time-exporter)

Already watched whole series?
Tired from obvious episode order?

![clumsy shit](http://i.imgur.com/Rmhz4.gif)

## Usage
```bash
$ docker run --rm dmi7ry/rick-and-morty-random-episode:5.0.0
```
or
```bash
$ docker run --rm dmi7ry/rick-and-morty-random-episode:5.0.0 --offline true
```

```
        ___
    . -^   `--,
   /# =========`-_
  /# (--====___====\
 /#   .- --.  . --.|
/##   |  * ) (   * ),
|##   \    /\ \   / |  ┌─┐┬ ┬┌─┐┬ ┬  ┌┬┐┌─┐
|###   ---   \ ---  |  └─┐├─┤│ ││││  │││├┤
|####      ___)    #|  └─┘┴ ┴└─┘└┴┘  ┴ ┴└─┘
|######           ##|  ┬ ┬┬ ┬┌─┐┌┬┐  ┬ ┬┌─┐┬ ┬  ┌─┐┌─┐┌┬┐
 \##### ---------- /   │││├─┤├─┤ │   └┬┘│ ││ │  │ ┬│ │ │
  \####           (    └┴┘┴ ┴┴ ┴ ┴    ┴ └─┘└─┘  └─┘└─┘ ┴
   `\###          |
     \###         |
      \##        |
       \###.    .)
        `======/

Selected Episode: s1e7 -- "Raising Gazorpazorp"
```
And enjoy your pseudo-randomized (~like your meaningless life~) episode pick
