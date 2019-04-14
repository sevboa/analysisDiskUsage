import codecs
import csv
import io
from time import sleep

from modules.Counter import counter

class csvWorker:
	
	@staticmethod
	def load(fileName, fieldNames, delimeter='\t', encoding='utf-8-sig'):
	    while True:
	        try:
	            with open(fileName, 'r', encoding=encoding) as fileCsv:
	                print('\r load ' + fileName + '                        ')
	                Counter = counter(len(io.open(fileName, 'r', encoding='utf-8-sig').readlines()) - 1, 0.2)
	                innerData = csv.reader(fileCsv, delimiter=delimeter)
	                outStrings = list()
	                for string in innerData:
	                    
	                    Counter.step('data load...')
	                    #string = string[0].split('\t')
	                    outString = dict()
	                    for i in range(0,7):
	                        outString.update({fieldNames[i]: string[i]})
	                    outStrings.append(outString)
	            Counter.lastTell(' data loaded')
	            #outStrings = sortingByFieldNames(outStrings, fieldNames)
	            return outStrings
	        except PermissionError:
	            print('\r!!!Please, close the file ' + fileName, end='')
	            sleep(1)
	
	@staticmethod
	def save(self, innerStrings, fileNameOut, fieldNames):
	    while True:
	        try:
	            with open('./output/' + fileNameOut, 'w', newline='', encoding='utf-8-sig') as outFile:
	                print('\r unload to ' + fileNameOut + '                        ')
	                Counter = counter(len(innerStrings), 0.2)
	                writer = csv.DictWriter(outFile, delimiter=';', fieldnames=fieldNames)
	                writer.writeheader()
	                for string in innerStrings:
	                    Counter.step('data unload...')
	                    inner_dict = string
	                    writer.writerow(inner_dict)
	            Counter.lastTell('data unloaded')
	            outFile.close()
	            print(' complete')
	            break
	        except PermissionError:
	            print('\r!!!Please, close the file ' + fileNameOut, end='')
	            sleep(1)
	    
