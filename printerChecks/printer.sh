#!/bin/bash
#Casey Beach. This is my printer script. There are many like it but this one is mine...


USER="McSmash T"
DATE=$(date)
PRINTERS=$( snot -s $1 | tr -d " " | grep -o '>\s\?\(fab\|eb\)[0-9]\{0,9\}[a-z]\{2\}[0-9]' | tr -d '>' )

for printer in $PRINTERS ; do

cat test | sed -e "s/#info/${USER} ${DATE} ${printer}/" | lpr -P$printer

done

