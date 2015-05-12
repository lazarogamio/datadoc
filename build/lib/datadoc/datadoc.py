import cli
from gdata.spreadsheet.service import SpreadsheetsService
import xmltodict
import json
import os
from collections import OrderedDict

class DataDoc(object):

    def __init__(self, args=None):
        """
        Get the options from cli or another source (in the future), and
        instantiate a ShapeGrid object.
        """
        self.cli = cli.CLI()
        self.args = self.cli.parse_arguments(args)

    def main(self):
        
        def fetchData(key):
            # Get data from google doc
            worksheetData = SpreadsheetsService().GetWorksheetsFeed(key,visibility='public', projection='full')
            # print worksheetData
            sheets = xmltodict.parse(str(worksheetData))['ns0:feed']['ns0:entry']
            # Build array of sheet names
            sheetNames = []
            
            try:
                for sheet in sheets:
                    sheetNames.append(sheet['ns0:title']['#text'])
                
            except TypeError:
                return fetchDataSimple(key)




            # Organize data into a dictionary
            niceData = {}
            curr = 0
            for entry in worksheetData.entry:
                # Find worksheet id from url
                worksheet_id = entry.id.text.rsplit('/', 1)[1]
                # Get the current sheet
                thisSheet = SpreadsheetsService().GetListFeed(key,worksheet_id,visibility='public')
                data = xmltodict.parse(str(thisSheet))
                # append the larger data object
                if sheetNames[curr] in niceData:
                    niceData[sheetNames[curr]].append(data)
                else:
                    niceData[sheetNames[curr]] = []
                    niceData[sheetNames[curr]].append(data)
                curr += 1

            processed = {}

            for k in niceData:
                niceData[k] = niceData[k][0]['ns0:feed']['ns0:entry']
                processed[k] = []
                for item in niceData[k]:
                    newitem = {}
                    for j in item:
                        if 'ns2:' in j:
                            newkey = j.split(':')[1]
                            newitem[newkey] = item[j]
                    
                    processed[k].append(newitem)

            return processed
                            

        def fetchDataSimple(key):
            cellData = SpreadsheetsService().GetListFeed(key,visibility='public', projection='full')
            feed = xmltodict.parse(str(cellData))['ns0:feed']['ns0:entry']
                
            processed = []

            for item in feed:
                newitem = {}
                for j in item:
                    if 'ns2:' in j:
                        newkey = j.split(':')[1]
                        newitem[newkey] = item[j]
                
                processed.append(newitem)

            return processed

        def combineFiles(directory):
            data = OrderedDict()

            for i in os.listdir(directory):
                if i != '.DS_Store':

                    name = i.split('.')[0]

                    with open(directory + '/' + i, 'r') as file:
                        datum = json.loads(file.read())
                        data[name] = datum

            return data

        try:
            data = fetchData(self.args.id)
            print 'Fetching your spreadsheet...'
            with open(self.args.dest,'wb') as file:
                file.write(json.dumps(data))
                print 'All done!'
                return

        except AttributeError:
            pass

        try:
            data = combineFiles(self.args.dir)
            print 'Combining your files...'
            with open(self.args.dest,'wb') as file:
                file.write(json.dumps(data))
                print 'All done!'
                return

        except AttributeError:
            pass

def launch_new_instance():
    """
    Launch an instance of Binifier.

    This is the entry function of the command-line tool `binify`.
    """
    datadoc = DataDoc()
    datadoc.main()

if __name__ == '__main__':
    launch_new_instance()

