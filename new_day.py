import shutil, os

day = int(input('Day:'))

try:
	shutil.copytree(os.getcwd()+'\\Day0 [TEMPLATE]',os.getcwd()+'\\Day{}'.format(day))
	print('Folder creation successful')
except Exception as e:
	print('Failure')
	print(e)
	raise ValueError(e)
print('press enter to close')
input()