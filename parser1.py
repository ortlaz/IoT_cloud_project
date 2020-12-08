import xml.etree.ElementTree as xml
import random
import json
import time
from html.parser import HTMLParser

#класс для парсинга HTML
class MyHP(HTMLParser):

    #конструктор
    def __init__(self, filename):
        super(MyHP, self).__init__()
        self.f = filename

    #запись названия
    def handle_starttag(self, tag, attrs):
        if tag == "p":
            for attr in attrs:
                self.f.write(attr[1]+": ")

                #вывод в консоль
                print(attr[1]+": ")

    #запись значения
    def handle_data(self, data):
        self.f.write(data+'\n')

        #вывод в консоль
        print(data+'\n')


#генерация html
def createHTML(filename, _id, prop, val):
    html = xml.Element('html')
    body = xml.Element('body')
    html.append(body)
    div = xml.SubElement(body, 'div', attrib={'class': 'data'})
    id = xml.SubElement(div, 'p', attrib={'id': 'id'})
    id.text = str(_id)
    name = xml.SubElement(div, 'p', attrib={'id': 'name'})
    name.text = filename.split('.')[0]                         #получение значения из имени файла
    pr = xml.SubElement(div, 'p', attrib={'id':prop})
    pr.text = val

    #запись в файл
    with open(filename, "w") as fh:
        xml.ElementTree(html).write(fh, encoding='unicode', method='html')


#генерация XML
def createXML(filename,_id,prop,val):
    root = xml.Element("Data")
    id = xml.SubElement(root, "id")
    id.text = str(_id)
    name = xml.SubElement(root, "name")
    name.text = filename.split('.')[0]       #получение значения из имени файла
    pr = xml.SubElement(root, prop)
    pr.text = val
    tree = xml.tostring(root, "utf-8")

    #запись в файл
    with open(filename, "w") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>' + tree.decode("utf-8"))


#генерация JSON
def createJSON(filename, _id, prop, val):
    data = {
        "id": _id,
        "name": filename.split('.')[0],     #получение значения из имени файла
        prop: val
    }

    #запись в файл
    with open(filename, "w") as fh:
        fh.write(json.dumps(data))   


#парсинг HTML
def parseHTML(filename):

    #запись в файл .txt
    with open(filename.split('.')[0]+'_html'+'.txt','w') as file:
        parser = MyHP(file)

        #получение данных из html файла
        with open(filename, "r") as rf:

            #вывод в консоль
            parser.feed(rf.read())


#парсинг XML
def parseXML(filename):

    #чтение из xml файла
    root = xml.parse(filename).getroot()

    #запись в файл .txt
    with open(filename.split('.')[0]+'_xml'+'.txt', 'w') as file:
        for tag in root:
            file.write("%s: %s" % (tag.tag, tag.text)+'\n')

            #вывод в консоль
            print("%s: %s" % (tag.tag, tag.text)+'\n')


#парсинг JSON
def parseJSON(filename):
    with open(filename, "r") as rf, open(filename.split('.')[0]+'_json'+'.txt','w') as file:

        #чтение из json файла
        lst = json.load(rf) 

        #запись в файл .txt
        for key in lst:
            file.write(key + ": " + str(lst.get(key))+'\n')

            #вывод в консоль
            print(key + ": " + str(lst.get(key))+'\n')
    

if __name__=="__main__":
    id = random.randint(0,50)                      #генерация id

    for item in range(5):

        destination = round(random.uniform(1,35), 3)   #генерация наполненности
        move = random.randint(0,1)                     #генерация движения

        #Для датчика дыма
        print("Датчик дыма\n")
        createXML("SmokeAlarm.xml", id, 'smoke', '0')
        createJSON("SmokeAlarm.json", id, 'smoke', '0')
        createHTML("SmokeAlarm.html", id, 'smoke', '0')

        parseXML("SmokeAlarm.xml")
        parseJSON("SmokeAlarm.json")
        parseHTML("SmokeAlarm.html")

        #Для дальнометра
        print("Дальнометр\n")
        createXML("Cap.xml", id, 'move', str(move))
        createJSON("Cap.json", id, 'move', str(move))
        createHTML("Cap.html", id, 'move', str(move))

        parseXML("Cap.xml")
        parseJSON("Cap.json")
        parseHTML("Cap.html")

        #Для датчика движения
        print("Датчик движения\n")
        createXML("Destination.xml", id, 'destination', str(destination))
        createJSON("Destination.json", id, 'destination', str(destination))
        createHTML("Destination.html", id, 'destination', str(destination))   

        parseXML("Destination.xml")
        parseJSON("Destination.json")
        parseHTML("Destination.html") 

        time.sleep(3)


