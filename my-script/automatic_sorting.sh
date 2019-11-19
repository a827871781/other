#!/bin/bash

# 移动alfred-workflow

# 第一个参数:需要移动文件后缀名
# 第二个参数:移动的文件夹名

mvFile() {
	echo ""
	suffix=$1
	fileDir=$2
	#判断 下载文件夹下,是否存在 文件夹,如果不存在 就创建
	if [ ! -d "$downloadsPath/$fileDir" ]; then
		mkdir $fileDir
	fi
	echo "info:开始整理后缀名为: $suffix 的文件"
	files=$(ls *.$suffix 2>/dev/null | wc -l)
	echo "info:下载目录下 $suffix 后缀的文件有:$files 个"
	if [ $files -ne 0 ]; then
		echo "info: $suffix 文件移动至 $downloadsPath/$fileDir 文件夹下"
		mv $downloadsPath/*.$suffix $downloadsPath/$fileDir
	fi
	echo "info:后缀名为: $suffix 文件 整理结束."
	echo ""
}

downloadsPath="/Users/syz/Downloads"

cd $downloadsPath

mvFile "alfredworkflow" "alfred-workflow"

mvFile "dmg" "App-package"

mvFile "war" "java-package"

mvFile "jar" "java-package"

mvFile "pdf" "pdf-package"

mvFile "bmp" "images"
mvFile "jpg" "images"
mvFile "jpeg" "images"
mvFile "png" "images"
mvFile "gif" "images"

mvFile "rar" "压缩文件"
mvFile "zip" "压缩文件"

mvFile "gz" "linux安装文件"

mvFile "doc" "office-package"
mvFile "docx" "office-package"
mvFile "xls" "office-package"
mvFile "xlsx" "office-package"
mvFile "ppt" "office-package"

if [ ! -d "$downloadsPath/other" ]; then
	echo "info:创建 other 目录."
	mkdir other
fi

echo "info:其他所有文件 移动至 other 目录."

mv $downloadsPath/*.* $downloadsPath/other/
