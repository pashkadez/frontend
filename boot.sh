#!/bin/bash
source .venv/bin/activate
flask db upgrade
#flask translate compile
flask run
