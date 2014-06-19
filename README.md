# REPY (REgex PYthon command line tool)

This is a small cli tool that enables testing of regex.



# Installation

This document will describe how to install this tool.



## Python dependencies

 - docopt>=0.6.1



## Install from source

It is reccomended to install and run repy inside a virtualenv.

Currently only installation from source is available. This package do not exit on any pip mirror yet.

Follow these steps to install repy in your enviroment.

Clone this git repo to disk

```shell
git clone git@github.com:Grokzen/repy.git; cd repy
```

Install with

```shell
python setup.py install
```

or create a sdist that can be installed with pip

```shell
make sdist
```



## repy version scheme

Stable releases follow the same name scheme ubuntu uses: <year>.<month>.<minor-release>

For example, a stable release made in March of 2014 will be labled: 14.03

If a second release is done the same month then it will be labled: 14.03.1




# Usage

This document will describe how to use this tool and provide usefull examples.



## CLI Input considerations

If you input contains spaces or " they must be escaped out with pythons standard escape character \

For example

```Shell
repy-cli -r "\".HN .+" -t "\"SHN 7" -vvvvv
```

Will test the regex

```
".HN .+
```

With the text

```
"SHN 7
```



## docopt string

Multiple -v will give different logging levels when running repy. '-vvvvv' will output DEBUG logging messages and '-v' will only output CRITICAL logging messages.

```
Usage:
  repy -i [-v ...]
  repy -r REGEX -t TEXT [-v ...]
  repy --version [--help]

Options:
  -i --interactive         run in interactive mode
  -r --regex               regex to match text to
  -t --text                text to match regex against. Only supports single line input.
  -h --help                show this help
  -v --verbose             verbose terminal output
  -V --version             display the version number and exit
```



# Authors list

```
Johan Grok Andersson <Grokzen@gmail.com>
```



# Contribution guide

TODO: Write contribution guide



# License

MIT (See LICENSE file)
