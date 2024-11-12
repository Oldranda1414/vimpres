#!/bin/bash

# This script is used to preview the presentation.

# Generate presentation html
marp slides.md

# Open the presentation in the browser
open slides.html