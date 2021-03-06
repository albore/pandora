#!/usr/bin/python
import fileinput, sys, os, random
baseDir = '/home/bsc21/bsc21887/pandora/examples/gujarat_cellphones2/explore'
taskFile = 'rainStddev.txt'

numExecutions = 10

rainStddevValues = ['1','100', '200', '300','400', '500', '600', '700', '800', '900', '1000', '1100', '1200', '1300', '1400', '1500', '1600', '1700', '1800', '1900', '2000', '2100', '2200', '2300', '2400', '2500']

xmlTemplate = 'templates/config_template_rainStddev.xml'

numExecutionKey = 'NUMEXEC'
rainStddevKey = 'RAIN_STDDEV'

def replaceKey( fileName, key, value ):
	for line in fileinput.FileInput(fileName,inplace=1):
		if key in line:
			line = line.replace(key, value)
		sys.stdout.write(line)
	fileinput.close()

os.system('rm -rf rainStddev/')
os.system('mkdir rainStddev')

index = 0
print 'creating test workbench'

for numExecution in range(0,numExecutions):
	for rainStddev in rainStddevValues:
		print 'creating gujarat_cellphones instance: ' + str(index) + ' for rain std dev: ' + rainStddev + ' and execution: ' + str(numExecution)
		dirName = 'rainStddev/results_rainStddev'+rainStddev+'_ex'+str(numExecution)
		os.system('mkdir '+dirName)
		configName = dirName + '/config.xml'			
		os.system('cp '+xmlTemplate+' '+configName)
		replaceKey(configName, rainStddevKey, rainStddev)
		replaceKey(configName, numExecutionKey, str(numExecution))
		index += 1

print 'workbench done, submitting tasks'
index = 0

taskFile = open(taskFile, 'w')
for rainStddev in rainStddevValues:
	for numExecution in range(0,numExecutions):
		print 'writing gujarat_cellphones instance: ' + str(index) + ' with rain std dev: ' + rainStddev + ' and execution: ' + str(numExecution)
		dirName = 'rainStddev/results_rainStddev'+rainStddev+'_ex'+str(numExecution)
		taskFile.write('cd '+baseDir+'/'+dirName+' && ../../../gujarat_cellphones\n')
		index += 1
taskFile.close()

