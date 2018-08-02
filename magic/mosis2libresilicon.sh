#!/bin/bash
if [ "$1" != "" ]; then
	if [ "$2" != "" ]; then
		if [ -f $1 ]; then
			cat $1 | \
				sed -e 's/<< polysilicon >>/<< poly >>/g' \
				| sed -e 's/tech scmos/tech ls1u/g' \
				| sed -e 's/<< ndiffusion >>/<< nimplant >>/g' \
				| sed -e 's/<< ntransistor >>/<< nimplant >>/g' \
				| sed -e 's/<< pdiffusion >>/<< pimplant >>/g' \
				| sed -e 's/<< ptransistor >>/<< pimplant >>/g' \
				| sed -e 's/<< polycontact >>/<< contact >>/g' \
				> $2
		fi
	fi
fi

