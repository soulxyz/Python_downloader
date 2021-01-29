# Python_downloader
A Simple Python Download Example
通过`requests`库实现的简易Python下载器案例
下载文件的同时，也列出下载状态和文件类型。

--url.txt 每行是单独的文件URL
--name.txt 每行是单独的文件名，与url.txt一一对应
--download.py  逐行读取`url.txt`文件并下载
--download_name.py 读取`url.txt`和`name.txt`，对应指定的文件名下载保存
--download_mix.py 完善了`download_name.py`可能遇到的`FileNotFoundError`问题。
