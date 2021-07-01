#!/bin/bash

# ensure all submodules are on commit
while read hash submodule ref; do
  git -C $submodule branch -a --contains $hash | grep "remotes/origin/master" >/dev/null
  if [ "$?" -eq 0 ]; then
    echo "$submodule ok"
  else
    echo "$submodule: $hash is not on master"
    exit 1
  fi
done <<< $(git submodule status --recursive)
