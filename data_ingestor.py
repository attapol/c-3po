import sys
import glob

def ingest_log(file_name):
    with open(file_name) as f:
        for line in f:
            try: 
                meta_data, class_info, ts, name, text = line.split(' ||| ', 4)
                if 'class=user' in class_info: 
                    user = class_info[11:]
                    if user != 'marley' and \
                            'admin' not in user and \
                            'jenkins' not in user and \
                            'sensu' not in user and \
                            'linkified' not in text:
                        #print line.strip()
                        #print user
                        print text[3:].strip()
            except ValueError:
                pass


if __name__ == '__main__':
    files = glob.glob(sys.argv[1])
    for file_name in files:
        ingest_log(file_name)
