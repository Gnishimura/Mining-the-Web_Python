__author__ = 'yimizhao'

# Web scraping using Python BeautifulSoup
'''
 Grab all President Obama's speeches on http://www.americanrhetoric.com/barackobamaspeeches.htm,
 and save the transcripts as .txt files for further text mining.
'''
import requests
from bs4 import BeautifulSoup

website = "http://www.americanrhetoric.com/barackobamaspeeches.htm"
r = requests.get(website)
page = BeautifulSoup(r.content)


# ###PART I: grab the urls###
# get the urls
def filter_link(link):
    href = link.get('href')
    if href:
        return href.startswith("speeches") and href.endswith(".htm")

links = page.find_all('a')
urls = filter(filter_link, links)
urls = [url.get('href') for url in urls]
print(len(urls)) # until March 20,2015, there are 278 urls

# display the urls
def get_url(link):
    pre = "http://www.americanrhetoric.com/"
    return pre+link

full_urls = []
for url in urls:
    full_urls.append(get_url(url))

# ###PART II: fetch the speech content###
# get the speech content
def get_g_data(url):
    re = requests.get(url)
    page_data = BeautifulSoup(re.content)
    g_data = page_data.find_all("font", {"face": "Verdana"})
    return g_data

# write into .txt files
def write_speech(url):
    name = url.split('/')[-1].split('.')[0]
    print('Writing {}...'.format(name))
    with open(name + '.txt', 'w') as f:
        resultset = get_g_data(url)
        for line in resultset:
            f.write(str(line.text))

for url in full_urls:
    write_speech(url)


# running display, 278 .txt files in total
'''
Writing barackobama2004dnc...
Writing barackobamasenatespeechonohioelectoralvotes...
Writing barackobamaknoxcollege...
Writing barackobamasenatefloorspeechpatriotact...
Writing barackobamasenatespeechoncorettascottkingpassing...
Writing barackobamasenatespeechonvotingrightsactrenewal...
Writing barackobamaexploratory...
Writing barackobamacandidacyforpresident...
Writing barackobamabrownchapel...
...
'''

# ###PART III: write urls and file names into .csv files###
# write urls
file1 = open('urls.csv','w')
for item in full_urls:
    file1.write(str(item) + '\n')
file1.close()

# display the first 10 urls
for i in range(10):
   print (full_urls[i])

'''
http://www.americanrhetoric.com/speeches/convention2004/barackobama2004dnc.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamasenatespeechonohioelectoralvotes.htm
http://www.americanrhetoric.com/speeches/barackobamaknoxcollege.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamasenatefloorspeechpatriotact.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamasenatespeechoncorettascottkingpassing.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamasenatespeechonvotingrightsactrenewal.htm
http://www.americanrhetoric.com/speeches/barackobamaexploratory.htm
http://www.americanrhetoric.com/speeches/barackobamacandidacyforpresident.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamabrownchapel.htm
http://www.americanrhetoric.com/speeches/barackobama/barackobamasenatespeechiraqfederalismamendment.htm
'''

# write filenames
files = []
for url in urls:
    file_name = url.split('/')[-1].split('.')[0] + '.txt'
    files.append(file_name)

file2 = open('filenames.csv','w')
for item in files:
    file2.write(item + '\n')
file2.close()

# display the first 10 file names
for i in range(10):
   print (files[i])

'''
barackobama2004dnc.txt
barackobamasenatespeechonohioelectoralvotes.txt
barackobamaknoxcollege.txt
barackobamasenatefloorspeechpatriotact.txt
barackobamasenatespeechoncorettascottkingpassing.txt
barackobamasenatespeechonvotingrightsactrenewal.txt
barackobamaexploratory.txt
barackobamacandidacyforpresident.txt
barackobamabrownchapel.txt
barackobamasenatespeechiraqfederalismamendment.txt
'''