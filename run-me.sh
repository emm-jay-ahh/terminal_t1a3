#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
	echo "ERROR:

    Python3 is not installed
    Please goto https://www.python.org/downloads/
    DOWNLOAD and INSTALL Python3" >&2

	exit 1
fi

sudo python3 net-whack.py $1
