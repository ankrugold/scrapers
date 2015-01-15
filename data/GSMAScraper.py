__author__ = 'ankur'

import requests;
import bs4;



response = requests.get('http://www.gsmarena.com/asus_zenfone_2_ze551ml-6917.php');
soup = bs4.BeautifulSoup(response.text);
# names = soup.select('div#specs-list p ').pop().text;

def popandprint(top):
    sfsname = top.select('th');
    if(sfsname.__len__()>0):
        sfsname=sfsname.pop().text;
    fsname = top.select('td.ttl a');
    if(fsname.__len__()>0):
        fsname=fsname.pop().text;
    fsval = top.select('td.nfo')
    if(fsval.__len__()>0):
        fsval=fsval.pop().text;
    print("feature",fsname,"superf",sfsname,"fvalue",fsval);


# print(nfsname ,nfsval);
topl = soup.select('div#specs-list table tr');
top = topl.pop();
for top in topl:
    popandprint(top);




# sfsnames = soup.select('div#specs-list table tr th');
# fsnames = soup.select('div#specs-list table tr td.ttl a');
# fsvals = soup.select('div#specs-list table tr td.nfo');
#
# sfsname = sfsnames.pop().text;
# fsname = fsnames.pop().text;
# fsval = fsvals.pop().text;
#
# print(sfsname,fsname,fsval);