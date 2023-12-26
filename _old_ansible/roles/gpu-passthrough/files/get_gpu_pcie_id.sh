#!/bin/bash
# https://drive.google.com/file/d/1rPTKi_b7EFqKTMylH64b3Dg9W0N_XIhO/view
set -e

bdu=`lspci | grep -i vga | awk '{ print $1 }'`
pcie_id=`lspci -n -s $bdu -v | head -n1 | awk '{ print $3 }'`
echo "$pcie_id"