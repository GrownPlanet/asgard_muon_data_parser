#!/bin/bash

if [ ! -d ".venv" ]; then
    python -m venv .venv
    source .venv/bin/activate
    pip install numpy matplotlib
else
    source .venv/bin/activate
fi

python organize_100m.py & python organize_100m_s.py
