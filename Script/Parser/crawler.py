from mimetypes import init
import re
from turtle import title
from urllib import response
from bs4 import BeautifulSoup
import requests
from time import sleep
import timeit
import os
import re
from Parser import parser, buckets, valid_name, isLegalName
from cleaner import keyword_ls, cleaner

keyword_ls = ["module", "let", "sig", "type"]#, "try", "match", "map"]
buckets = ["[", "]", "(", ")" , "{", "}" ]
valid_name = re.compile("^'*([a-z]|[A-Z])+([a-z]|[_]|[A-Z]|[\.]|[0-9])*'*$")

def getML(docs_url):
    '''
        input  <- A file url from GitHub.
        effect <- Store the raw file to local.
        return -> int   1 : successfully download a file
                        0 : no file has been downloaded
    '''
    response = requests.get(docs_url, headers={'User-Agent': "Mozilla/5.0"})
    response_code = response.status_code
    
    if response_code != 200:
        print("Fail to connect to the given document url.")
        return None
    
    html_content = BeautifulSoup(response.content, 'html.parser')
    if sizeChecker(html_content):
        try:
            file_name = html_content.select('strong.final-path')[0].string
            raw_file_url = "https://raw.githubusercontent.com" + html_content.find(id="raw-url")["href"].replace('/raw','')
        
        
            response = requests.get(raw_file_url, headers={'User-Agent': "Mozilla/5.0"})
            content = cleaner(response.content.decode("utf-8"))
            ls = content.split("\n\n")
            content = []
            for exp in ls:
                content.append(parser(exp))
            open("test4\\" + file_name, "w").write(("\n\n").join(content))
            
            return 1
        except:
            print("An Error occurs when downloading file {}.\n".format(file_name))
            return 0
    
    return 0

def sizeChecker(file_html):
    '''
        input  <- file page content in html
        effect <- check whether the size of the file is qualified
                  (in this case, #line >= 50)
        return -> boolean True for #line >= 50
                          False    #line <  50
    '''
    info = file_html.find("div", class_ = "text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1").text.split()
    if info[0].isnumeric() and int(info[0]) >= 50:
        return True
    return False

def getAllML(module_url):
    '''
        input  <- A sub-module url on GitHub.
        effect <- Traverse through the files and modules inside of
                  it and call for getML for all the OCaml files.
        return -> number of OCaml files pulled.
    '''
    counter = 0

    response = requests.get(module_url, headers={'User-Agent': "Mozilla/5.0"})
    response_code = response.status_code
    
    if response_code != 200:
        print("Fail to connect to the given sub-module url.")
        return 0
    
    html_content = BeautifulSoup(response.content, 'html.parser')
    
    for file in html_content.find_all("div", class_="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item"):
        file_type = file.select("svg")[0]["aria-label"]
        if file_type == "Directory":
            # accumulate the # of pulled files
            counter += getAllML("https://github.com" + file.find("a",class_ = "js-navigation-open Link--primary")["href"])
        
        else:
            file = file.find("a",class_ = "js-navigation-open Link--primary")
            if file:
                file_name = file["title"]

                if re.search("[.]ml$", file_name):
                    file_url = file["href"]
                    counter+= getML("https://github.com" + file_url)

                    sleep(3)
    
    return counter

def surfing(search_url, counter):
    '''
        input <- search page from GitHub
        effect <- Loop through the given url and download all the OCaml files.
        return -> Number of downloaded files
        
    '''
    num = 0
    
    if not counter:
        return num
    
    response = requests.get(search_url, headers={'User-Agent': "Mozilla/5.0"})
    response_code = response.status_code
    
    if response_code != 200:
        print("Fail to connect to the given search page url.")
        return None

    html_content = BeautifulSoup(response.content, 'html.parser')
    
    for repo in html_content.find_all("a", class_ = "v-align-middle"):
        repo_url = "https://github.com" + repo["href"]
        repo_name = repo.text
        print("Start looking at repo: " + repo_name + "\n")

        start = timeit.default_timer()
        file_num = getAllML(repo_url)
        stop = timeit.default_timer()

        print("Finishing with {}. \nDownloaded Files: {}.\nTime consumed : {}s.\n----------------------------------".format(repo_name, file_num, (stop-start)) )
        num += file_num
        sleep(10)
    
    next_page = html_content.find(rel="next")
    next_page_url = "https://github.com" + next_page["href"]
    return num + surfing(next_page_url, counter-1)

         



start = timeit.default_timer()
# getML("https://github.com/ocaml/ocaml/blob/trunk/asmcomp/arm/reload.ml")
# getAllML("https://github.com/realworldocaml/examples")
surfing("https://github.com/search?l=OCaml&p=100&q=ocaml&type=Repositories", 1)
stop = timeit.default_timer()
print('Time: ', stop - start)  
#if __name__ == "__main__":
#    print("Crawler running")
