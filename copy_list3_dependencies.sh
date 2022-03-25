#!/bin/bash
LIST3_DIR=$1
OUTPUT_DIR=../../$2

LIST2_DIR=../../build/list2

cd "$LIST3_DIR"
BAT_FILES=$(find *.bat)

echo
echo Copying .bat files to destination dir
for file in $BAT_FILES
do
    echo Copying file $file
    cp $file "$OUTPUT_DIR"
done

echo
echo Copying cpp scripts to destination dir
echo Copying head
cp "$LIST2_DIR"/head "$OUTPUT_DIR"
echo Copying tail
cp "$LIST2_DIR"/tail "$OUTPUT_DIR"
echo Success copying list3 dependencies