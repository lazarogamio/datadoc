#DataDoc

A command-line tool that fetches data from google spreadsheets and saves it as json in the filesystem.

##Installation

DataDoc is available in the Python Package Index.

    $ pip install datadoc

##Usage

To view options, use the help flag.

    $ datadoc --help
    usage: datadoc [fetch, combine]

    positional arguments:
      {fetch,combine}
        fetch          Grab a google spreadsheet and save it down
        combine        Combine multiple files into one.

    {fetch}
    usage: datadoc fetch [id] [dest]
    positional arguments:
    id          ID of google doc to use
    dest        Output file destination

    {combine}
    usage: datadoc combine [dir] [dest]
    positional arguments:
      dir         Directory with the data files you want to use.
      dest        Output file destination

##Examples

####Command line

To grab a google doc and save it in the current directory as `data.json`:

    $ datadoc fetch spreadsheet_id data.json

To combine json files in a directory and convert them to a named dictionary in `data.json`:

    $ datadoc combine directory data.json

####Python
    
    from datadoc import datadoc as doc
    
    # Returns a python dictionary
    test = doc.fetchData('spreadsheet_id')
    
    # Returns a python dictionary of all json files in the directory
    test = doc.combineFiles('directory_name')

##Caveats

- For the `fetch` command to work, the spreadsheet needs to be published
- Output is only in json at the moment
- Combine only takes json
