#coding=utf-8

import sys,subprocess,os
#查找最近10分钟被修改的文件
def scanfile():
	#command: find -name '*.php' -mmin -1
	command = "find -name \'*.php\' -mmin -1"
	su = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	STDOUT,STDERR = su.communicate()
	list = STDOUT.split("\n")
	#print(list)
	#print str(list)
	#将文件处理成list类型然后返回。
	return list

#读取文件：
def loadfile(addr):
	data = ""
	#如果文件不存在就跳出函数
	try :
		file = open(addr,'r')
		data = file.read()
	except : 
		return 0
	all_data = addr+"\n"+data+"\n\n"
	file1 = open("content.txt",'a+')
	#避免重复写入
	try:
		shell_content = file1.read()
	except:
		shell_content = "null"
	#如果文件内容不为空再写入，避免写入空的。
	#print shell_content
	if data :
		if all_data not in shell_content:
			file1.write(all_data)
	file.close()
	file1.close()
	#rm_cmd = "rm -rf "+addr #进行linux的系统命令执行，在这里改为
	#print addr
	addr1 = addr+"\n"
	file2 = open("append_file.txt",'a+')
	try :
		append_file = file2.read()
	except :
		append_file = "null"
	if addr1 not in append_file:
		file2.write(addr1)
	file2.close()
		

if __name__ == '__main__':
	while True:

		list = scanfile()
		if list :
			for i in range(len(list)):
				#如果list[i]为空就不读取了
				if list[i]:
					loadfile(str(list[i]))
		else : pass
