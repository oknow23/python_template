#!/bin/bash
FOLDER_NAME=$(pwd | rev | cut -d "/" -f 1 | rev)
FORMAT=zip
FILE_NAME=${FOLDER_NAME}_$(git log --date=short --pretty=format:"%ad-%h" -1).${FORMAT}
if [ -d ${FOLDER_NAME} ]; then
    echo Ouput Execute file zip!!
    zip -r ${FILE_NAME} ${FOLDER_NAME}
else
    echo Output GIT file zip!!
    git archive --format zip -o ${FILE_NAME} HEAD
fi

echo Success !!
