#!/bin/sh

gunicorn -w 1 'redirect:app'