#!/bin/bash

#
# compare_versions.sh <version 1> <version 2>
#  Output:
#   0 - Both versions are the same
#   1 - Version 1 is higher than version 2
#   2 - Version 2 is higher than version 1
#

NEW=`echo $1 | sed -e "s/.el6//; s/.el7//; s/.x86_64//"`
OLD=`echo $2 | sed -e "s/.el6//; s/.el7//; s/.x86_64//"`

# If they are the same break immediately
if [ $NEW = $OLD ]; then
    echo same version. $NEW versus $OLD  nothing to do
    exit 0
fi

# Break versions into array assuming format like 1.2.3.4-5_1
IFS='.|-|;|_' read -d '' -ra version1 < <(printf '%s;\0' "$NEW")
IFS='.|-|;|_' read -d '' -ra version2 < <(printf '%s;\0' "$OLD")


parts1=${#version1[@]}
parts2=${#version2[@]}

# find the smallest number of version tuples. i.e. 9.5 would have 2 parts and 9.5.1 would have 3
#    we only want to compare the version parts for the version with the smallest parts
[ ${#version1[@]} -le ${#version2[@]} ] && parts=${#version1[@]} || parts=${#version2[@]}

for (( i=0; i<$parts; i++ ))
do
  echo part=$i  ${version1[$i]} ${version2[$i]}
  if [ ${version1[$i]} -gt ${version2[$i]} ]; then
      echo upgrade from ${OLD} to ${NEW}
      exit 1
  elif [ ${version2[$i]} -gt ${version1[$i]} ]; then
      echo downgrade from ${OLD} to ${NEW}
      exit 2
  fi
done

# if everything else matches so far, just choose the longest
if [ ${parts1} -lt ${parts2} ]; then
    echo downgrade from ${OLD} to ${NEW}
    exit 2
elif [ ${parts1} -gt ${parts2} ]; then
    echo upgrade from ${OLD} to ${NEW}
    exit 1
else
    echo same version. $NEW and $OLD  nothing to do
    exit 0 
fi
