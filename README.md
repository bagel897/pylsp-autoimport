# pylsp-autoimport

"autoimport plugin for pylsp"
Simple around [autoimport](https://github.com/lyz-code/autoimport)

This is a plugin for [Python LSP Server](https://github.com/python-lsp/python-lsp-server).

## Installation

To use this plugin, you need to install this plugin in the same virtualenv as python-lsp-server itself.

``` bash
pip install pylsp-autoimport
```

Then run `python-lsp-server` as usual, the plugin will be auto-discovered by
`python-lsp-server` if you've installed it to the right environment. Refer to
`python-lsp-server` and your IDE/text editor documentation on how to setup
`python-lsp-server`.

## Configuration
Not implemented yet
... TODO ...

## Features

This plugin adds the following features to `pylsp`:
- autoimporting

## Developing

Install development dependencies with (you might want to create a virtualenv first):

``` bash
git clone git@github.com:bageljrkhanofemus/pylsp-autoimport.git pylsp-autoimport
cd pylsp-autoimport
pip install -e '.[dev]'
```

### Enabling logging

To enable logging in pylsp:

    pylsp -v --log-file /tmp/pylsp.log

### Enabling tcp mode

Normally, editors communicate with language servers through standard
input/output. Optionally, you can run pylsp in tcp mode if you want to be able
to use the standard input/output, for example so you can use IPython or pudb,
using the --tcp flag:

    pylsp -v --log-file /tmp/pylsp.log --tcp --port 7090

Consult your lsp client documentation on how to connect to tcp-mode language
server, but if it doesn't support connecting to a language server via TCP, then
usually can configure `netcat`/`nc` to be your "language server" that will
proxy requests to a tcp-mode language server:

    nc localhost 7090

TODO: document how to connect to pylsp via pylsp from LSP clients.
### Testing 

Run `pytest` to run plugin tests.
TODO: Implement tests



## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) from 
[python-lsp/cookiecutter-pylsp-plugin](https://github.com/python-lsp/cookiecutter-pylsp-plugin)
project template.
