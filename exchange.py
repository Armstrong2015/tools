'''
用来将kindle到处的文本转换成纯文本
'''
def  is_append(sentence):
	if len(sentence) < 3:
		return False

	if sentence.split()[0] == 'Highlight':
		return False

	return True


f = open("C:/Users/hichens/Desktop/kindle.txt", 'r')

sentence = f.readline()
text = []

while sentence:
	if(is_append(sentence)):
		text.append("<blockquote>\n" + sentence +"</blockquote>\n")
	sentence = f.readline()
	

f = open("C:/Users/hichens/Desktop/kindle_exchange.txt", 'w')

for sentence in text:
	f.write(sentence)