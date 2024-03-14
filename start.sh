#!/bin/sh

gunicorn -w 1 'redirect:app' -b 0.0.0.0:${PORT}