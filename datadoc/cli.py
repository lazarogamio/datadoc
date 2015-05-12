#!/usr/bin/env python

import argparse

class CLI(object):
    """
    Handles command-line interface options
    """

    def parse_arguments(self, args=None):
        """
        Implement command-line arguments
        """
        self.parser = argparse.ArgumentParser(usage='datadoc [fetch, combine]')
        self.sub = self.parser.add_subparsers()
        
        self.fetch = self.sub.add_parser('fetch', help='Grab a google spreadsheet and save it down.', usage='datadoc fetch [spreadsheetID] [outfile]')

        self.fetch.add_argument('id',
            help='ID of google doc to use'
        )

        self.fetch.add_argument('dest',
            help='Output file destination'
        )

        self.combine = self.sub.add_parser('combine', help='Combine multiple files into one.', usage='datadoc combine [folder] [outfile]')

        self.combine.add_argument('dir',
            help='Directory with the data files you want to use.'
        )

        self.combine.add_argument('dest',
            help='Output file destination'
        )


        return self.parser.parse_args(args)

