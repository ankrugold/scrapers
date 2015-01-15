__author__ = 'ankur'


import requests;
import bs4;



response = requests.get('http://www.thephonedatabase.com/Samsung_Galaxy_Note_II_964_Cell_Phone');
soup = bs4.BeautifulSoup(response.text);

def popandprint(top):

    fsname = top.select('div.feature');
    fsval = top.select('div.text');
    print(fsname.__len__()," ",fsval.__len__());
    names = map(lambda x: x.text,fsname);
    vals =  map(lambda x: x.text,fsval);
    dir = zip(names,vals);
    print(list(dir));





popandprint(soup);
