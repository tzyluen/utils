#!/bin/bash
# undelete-file.sh: undelete not overwritten files from Sleuthkit
#                   supported filesystems
#
# usage:
# ./undelete-file.sh  deleted-file-list.txt fstype disk.img
#

#set -xv
fstype=$2
diskimg=$3

cat $1 |
while read line; do
    filetype=`echo "$line" | awk {'print $1'}`
    filenode=`echo "$line" | awk {'print $3'}`
    filenode=${filenode%:}
    filename=`echo "$line" | cut -f 2`

    if [[ "$filename" =~ ".Spotlight-V100" ]]; then
        continue
    fi

    if [ "$filetype" = "d/d" ]; then
        cmd=$(mkdir -p $filename)
        echo $cmd
        $cmd
    else
        cmd=$(icat -r -s "$diskimg" $filenode > "$filename")
        echo $cmd
        $cmd
    fi
done
