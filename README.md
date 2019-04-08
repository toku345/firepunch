# FIREPUNCH 🔥👊🏻

[![Build Status](https://travis-ci.com/toku345/firepunch.svg?branch=master)](https://travis-ci.com/toku345/firepunch)
[![Maintainability](https://api.codeclimate.com/v1/badges/e6f8871b24dbedcf3b7d/maintainability)](https://codeclimate.com/github/toku345/firepunch/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e6f8871b24dbedcf3b7d/test_coverage)](https://codeclimate.com/github/toku345/firepunch/test_coverage)

## Description

Notify specific GitHub repos change of the day before on every morning!

## Requirement

- Python 3.7


## Installation

### cli

``` console
$ pipenv install --dev
$ pipenv shell

# If you use direnv
$ cp .envrc.sample .envrc
$ $EDITOR .envrc # set your GitHub access token
$ direnv allow

# or set `export GITHUB_ACCESS_TOKEN=XXXXXX` to your .bash_profile / .zshenv
```

If you send messages to slack, you need slack_token

``` console
# If you use direnv
$ $EDITOR .envrc # set your GitHub access token
$ direnv allow

# or set `export SLACK_TOKEN=XXXXXX` to your .bash_profile / .zshenv
```


### testing

``` console
$ pipenv run pytest
# or
$ pipenv shell
$ pytest
```

## Usage

### cli

``` console
$ ./cli.py <repo_name>

# e.g.
$ ./cli.py toku345/firepunch
```

![cli_image](images/cli_image.png)

## License

Apache License 2.0
