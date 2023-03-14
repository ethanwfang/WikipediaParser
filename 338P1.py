import requests
import pandas as pd
from bs4 import BeautifulSoup



#Send a GET request to the webpage
url = 'https://en.wikipedia.org/wiki/Operating_system'
response = requests.get(url)

def add(large_string, string_array, urlArray):
    ind = 0
    for string in string_array:
        large_string = large_string.replace(string, f"{string} \n\n (IV) Wikipedia: {string} -- {extract_text(urlArray[ind])} \n")
        ind+=1
    return large_string

def extract_text(url):
    # send a request to the page
    response = requests.get(url)
    # create a BeautifulSoup object to parse the page HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    # find the first paragraph of the page and return its text
    return soup.find('p', {'class':''}).get_text()

#Creating new text file
with open('Project1.pdf', mode='a') as file:
    file.write('This text will be appended to the file.\n')
    file.write(extract_text(url))

    # I'm gonna parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now we extract the h2 from the soup
    h2_text_arr = []
    h3_text_arr = []
    thing = []
    h2_elements = soup.find_all('h2')
    
    for h2 in h2_elements:
        h2_text_arr.append(h2.text)
        file.write('(Title) ' + h2.text + '\n')
        #Find the h3 elements that come after the h2 element
        h3_elements = h2.find_next_siblings('h3')
        for h3 in h3_elements:
            h3_text_arr.append(h3.text)
            file.write('(Section) ' + h3.text + '\n')
            p_elements = h3.find_next_siblings('p')
            for p in p_elements:
                file.write('(Paragraph) ' + p.text)
                file.write('\n')
                for link in p.find_all('a'):
                    if "/wiki/" in str(link):
                        actual = 'https://en.wikipedia.org' + link.get("href")
                        txt = link.text
                        file.write('(Definition) Wikipedia: "' + txt + '" -- ')
                        file.write(extract_text(actual))
                        file.write('\n')
            
            








'''
for p in p_elements:
                file.write('(III) ' + p.text)
                file.write('\n')
                for link in p.find_all('a'):
                    if "/wiki/" in str(link):
                        actual = 'https://en.wikipedia.org' + link.get("href")
                        txt = link.text
                        file.write('(IV) Wikipedia: "' + txt + '" -- ')
                        file.write(extract_text(actual))
                        file.write('\n')

for p in p_elements:
                stringBuilder = ''
                stringBuilder += '(III) ' + p.text + '\n'
                for link in p.find_all('a'):
                    if "/wiki/" in str(link):
                        actual = 'https://en.wikipedia.org' + link.get("href")
                        txt = link.text
                        stringBuilder += '(IV) Wikipedia: "' + txt + '" -- '
                        stringBuilder += extract_text(actual)
                        stringBuilder += '\n'
                file.write(stringBuilder)

for p in p_elements:
                strin = p.text
                strArr = strin.split()
                linkArr = []
                linkUrl = []
                for link in p.find_all('a'):
                    if "/wiki/" in str(link):
                        txt = link.text
                        linkArr.append(txt)
                        actual = 'https://en.wikipedia.org' + link.get("href")
                        linkUrl.append(actual)
                print(linkArr)
                count = 0
                for word in strArr:
                    file.write(' ' + word)
                    if count < len(linkArr):
                        print('enter linkArr')
                        if word == linkArr[count]:
                            print('enter wahoooo')
                            file.write('\n\n')
                            file.write('(IV) Wikipedia: "' + word + '" -- ')
                            file.write(extract_text(linkUrl[count]))
                            file.write('\n')
                            count += 1

actual = 'https://en.wikipedia.org' + link.get("href")
            file.write('(I) Wikipedia: ' + txt + '\t')
            file.write(extract_text(actual))
            file.write('\n')


for p in p_elements:
                urlArray = []
                linkArray = []
                bigString = p.text
                for link in p.find_all('a'):
                    if "/wiki/" in str(link):
                        actual = 'https://en.wikipedia.org' + link.get("href")
                        txt = link.text
                        urlArray.append(actual)
                        linkArray.append(txt)
                print(urlArray)
                file.write(add(bigString, linkArray, urlArray))
'''



                    
                        

                        
                    


                


            
            



