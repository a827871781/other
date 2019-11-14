#!/bin/bash
echo y | yum remove vim

echo y | yum install vim

cd ~

wget https://raw.githubusercontent.com/a827871781/other/master/.vimrc -O .vimrc



bundlePath="~/.vim/bundle/"

if [ ! -d $bundlePath ]; then
  mkdir -p "$bundlePath"
fi

cd $bundlePath

git clone https://github.com/scrooloose/nerdtree.git

source ~/.vimrc
