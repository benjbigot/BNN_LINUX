import goslate
import time
import codecs
from datetime import timedelta
def trans(tra,a):
  print tra, a
  gs=goslate.Goslate()
  text=open(tra,"r")
  english=codecs.open(a+'en.vtt','w','utf-8')
  chinese=codecs.open(a+'cn.vtt','w','utf-8')
  tamil=codecs.open(a+'ta.vtt','w','utf-8')
  malay=codecs.open(a+'ms.vtt','w','utf-8')
  french=codecs.open(a+'fr.vtt','w','utf-8')
  lines=text.readlines()
  arr=[]
  for i in range(len(lines)):
	  arr.append(lines[i].split('~'))
  for i in reversed(range(len(arr))):
	 if(arr[i][0]=="\n"):
		arr.pop(i)
  for i in range(len(arr)):
	arr[i][0]=arr[i][0].strip()
	arr[i][1]=arr[i][1].strip()
	arr[i][2]=arr[i][2].strip().replace("\n","")
  def translation(arr,lang):
	print "================ running " , lang
	for i in range(len(arr)):
		englishtext=arr[i][2]
		cTime=str(timedelta(milliseconds=int(arr[i][0]))).split(".")
		cTime=cTime[0]+","+"000"
		cTime=cTime.zfill(12)
		fullD=str(timedelta(milliseconds=int(arr[i][0])+int(arr[i][1]))).split(".")
		fullD=fullD[0]+","+"000"
		fullD=fullD.zfill(12)
		if(lang=="en"):
			english.write(cTime+" --> "+fullD+"\n"+englishtext+"\n\n")
		else:
			if(arr[i][2]!="" and len(arr[i][2])>2):
				print arr[i][2]
				translated=gs.translate(arr[i][2],lang)
				print arr[i][2], translated
				time.sleep(0.5)
			else:
				translated=""
			if(lang=="zh-CN"):
				chinese.write(cTime+" --> "+fullD+"\n"+englishtext+"\n"+translated+"\n\n")
			if(lang=="ta"):
				tamil.write(cTime+" --> "+fullD+"\n"+englishtext+"\n"+translated+"\n\n")
			if(lang=="ms"):
				malay.write(cTime+" --> "+fullD+"\n"+englishtext+"\n"+translated+"\n\n")
			if(lang=="fr"):
				french.write(cTime+" --> "+fullD+"\n"+englishtext+"\n"+translated+"\n\n")				
	print "============== done " , lang

  translation(arr,"en")
  translation(arr,"fr")
  translation(arr,"zh-CN")
  translation(arr,"ta")
  translation(arr,"ms")

  
  
#trans('Fortranslation.txt')
