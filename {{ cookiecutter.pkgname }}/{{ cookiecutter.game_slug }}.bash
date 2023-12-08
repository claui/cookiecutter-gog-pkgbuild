#!/usr/bin/env bash
set -eu

PKGNAME='{{ cookiecutter.game_slug }}'
echo >&2 "Launching app"
cd "/opt/${PKGNAME}"
exec ./start.sh "$@"
