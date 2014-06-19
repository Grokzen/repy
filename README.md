# REPY (REgex PYthon cli)

This is a small cli tool that enables testing of regex.



# Python dependencies

 - docopt>=0.6.1



# Install from source

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
make sdist && pip install dist/repy-14.06.tar.gz
```



# Usage

```
repy-cli -r "\".HN .+" -t "\"SHN 7"
```

Output

```
# Search for all matches
>>> regex = re.compile(self.regex)
>>> r = regex.search(self.text)
>>> r is not None
True

# Find what indexes the regex matched
>>> r.regs
((0, 6),)

# Test if regex matches text
>>> m = regex.match(self.text)
>>> m is not None
True

# List the groups found
>>> r.groups()
()

# List the named dictionary objects found
>>> r.groupdict()
{}

# Run findall
>>> f = regex.findall(text)
>>> f
['"SHN 7']

# Run timeit test
>>> setup = ur'import re; regex =re.compile('".HN .+');string='"SHN 7'
>>> t = timeit.Timer('regex.search(string)',setup)
>>> t.timeit(10000)
0.0032029151916503906
```



# docopt string

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



# repy version scheme

Stable releases follow the same name scheme ubuntu uses: <year>.<month>.<minor-release>

For example, a stable release made in March of 2014 will be labled: 14.03

If a second release is done the same month then it will be labled: 14.03.1



# Authors

```
Johan Grok Andersson <Grokzen@gmail.com>
```



# Contribution guide

TODO: Write contribution guide



# License

MIT (See LICENSE file)
