import sys

def ingest_log(file_name):
    with open(file_name) as f:
        for line in f:
            meta_data, class_info, ts, name, text = line.split(' ||| ', 4)
            if 'class=user' in class_info: 
                user = class_info[11:]
                if user != 'marley' and 'admin' not in user and 'linkified' not in text:
                    #print line.strip()
                    #print user
                    print text[3:].strip()


if __name__ == '__main__':
    for file_name in sys.argv[1:]:
        ingest_log(file_name)
