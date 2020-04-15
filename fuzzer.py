import sys
import requests
import logging


def main():

    logging.basicConfig(filename=sys.argv[3],level=logging.INFO)

    url=sys.argv[1]
    try:
        wordlistfile= open(sys.argv[2])
    except:
        print("File could not be opened or found....")
        sys.exit()
    
    lines = wordlistfile.readlines()

    for line in lines:
        search=url+line
        search=search.rstrip()
        search+="/"
        re= requests.get(search)
        if re.status_code == 200 or re.status_code == 403 :
            logging.info(search + " ---> " + str(re.status_code))

if __name__== "__main__":
    main()