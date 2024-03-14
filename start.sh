#!/bin/sh

gunicorn -w 1 'redirect:app' -b 127.0.0.1:${PORT}