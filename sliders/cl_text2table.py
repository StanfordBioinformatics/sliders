#!/usr/bin/env python
"""Command-line tool for converting text2table using FlexTableParser.
"""

__author__ = 'pbilling@stanford.edu (Paul Billing-Ross)'

import sys
import argparse

from sliders import flextableparser

BUILT_IN_SCHEMAS = {
                    'fastqc': 'table_schemas/fastqc.json',
                    'flagstat': 'table_schemas/flagstat.json'
                   }

def parse_args(args):

    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '-i',
                        '--input_files',
                        dest = 'input_files',
                        nargs = '+',
                        help = 'Input file path',
                        required = True)
    parser.add_argument(
                        '-s',
                        '--schema',
                        dest = 'schema',
                        type = str,
                        help = 'Table conversion schema',
                        choices = ['fastqc', 'flagstat'],
                        required = False)
    parser.add_argument(
                        '-j',
                        '--json_file',
                        dest = 'json_file',
                        type = str,
                        help = 'JSON config file with table conversion schema',
                        required = False)
    parser.add_argument(
                        '-v',
                        '--static_values',
                        dest = 'static_values',
                        nargs = '+',
                        help = 'Static values to be added as columns',
                        required = False)
    parser.add_argument(
                        '-o',
                        '--output_file',
                        dest = 'output_file',
                        type = str,
                        help = 'Output file path',
                        required = False)
    parser.add_argument(
                        '-a',
                        '--append',
                        dest = 'append',
                        type = bool,
                        help = 'Append instead of write output file',
                        default = False)
    
    if len(sys.argv[1:]) < 1:
        print('No arguments specified')
        parser.print_help()
        sys.exit()
    args = parser.parse_args(args)
    return(args)

def main():

    # Create table parser
    table_parser = flextableparser.FlexTableParser()

    # Parse command-line arguments
    args = parse_args(sys.argv[1:])

    # Configure parser with built-in schema or specify custom config file
    if args.schema:
        schema_file = built_in_schemas[args.config]
    elif args.json_file:
        schema_file = json_file
    table_parser.configure(schema_file)

    if args.static_values:
        # To-do: Parse key:value string
        table_parser.add_static_values(args.static_values)

    if args.output
        output = open(args.output, )
    
    table_parser.configure(schema_file)
    table_parser.add_static_values(static_values)

    for input_file in input_files:  
        table_parser.parse_file(input_file) >>

if __name__ == '__main__':
    main()

