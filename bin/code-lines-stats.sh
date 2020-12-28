#!/bin/bash

# java lines stats
# shellcheck disable=SC2038
find . "(" -name "*.java" ")" -print | xargs wc -l

# other lines stats
find . "(" -name "*.m" -or -name "*.mm" -or -name "*.cpp" -or -name "*.h" -or -name "*.rss" ")" -print | xargs wc -l

