#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys
import csv
from os.path import exists, isdir
from os import makedirs

man_string = """
███████╗ █████╗ ███████╗████████╗███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
█████╗  ███████║███████╗   ██║   ███████╗██║     ██████╔╝███████║██████╔╝█████╗  
██╔══╝  ██╔══██║╚════██║   ██║   ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
██║     ██║  ██║███████║   ██║   ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝
                                                                                    V 0.7
                                                                                Made by Strykez
options:
  -h, --help,          show this help message and exits
  -m, -man, --manual

  -u, --url             sets the script's URL

  -s, --selector        the selector string used in the script
                        
                        selector format --> Column_name:selector.class/another_selector.another_class

                        If column name is empty, it will append to the current column, else it will create a new column and append
                        the data to it

                        Examples: Titles:div.card/div.first_half/p.title --> Gets all the instances of p.title in the specified path
                                  Titles:p.title --> Gets all the instances of p.title in the page
                                  p.title --> If you do not want a column name

  -o, --output          the path where you want the results to be saved in .csv format (creates the directory/ies if necessary)
                        if left blank it will print the selected elements to the terminal
  
  -v, --verbose         displays more information about the steps performed in the script
                        NOTE: Put the verbose argument as the last argument because putting it ahead can make the script crash
"""

def arg_parser():
    if len(sys.argv) == 1:
        raise Exception('No options in the command line')
    

    for arg in sys.argv[1::2]:
        lower_arg = arg.lower()
        next_arg = sys.argv.index(arg) + 1
        global URL, file_path, selector, output_path, verbose_bool

        

        if lower_arg == '-m' or lower_arg == '--manual' or lower_arg == '-man' or lower_arg == '-h' or lower_arg == '--help':
            print(man_string)
            exit()
        elif lower_arg == '-u' or lower_arg == '--url':
            URL = sys.argv[next_arg]
        elif lower_arg == '-s' or lower_arg == '--selector':
            selector = sys.argv[next_arg]
        elif lower_arg == '-o' or lower_arg == '--output':
            output_path = sys.argv[next_arg]
        elif lower_arg == '-v' or lower_arg == '--verbose':
            verbose_bool = True
        else:
            print(f'Argument {arg} not in options')
    

    if URL == '':
        raise Exception('URL not specified')

class ScrapeBot :
    def __init__(self, URL, output, selector):  
        self.URL = URL
        self.output = output
        self.selector = selector

    def process_selectors(self,selector_string):
        self.temp = selector_string.split(':')
        global column_name, selector_array, class_array
        
        if (len(self.temp) == 1):
            for element in self.temp[0].split('/'):
                element = element.split('.')
                selector_array.append(element[0])
                try:
                    class_array.append(element[1])
                except:
                    class_array.append('NONE')


        else:
            column_name = self.temp[0]
            
            for element in self.temp[1].split('/'):
                element = element.split('.')
                selector_array.append(element[0])
                try:
                    class_array.append(element[1])
                except:
                    class_array.append('NONE')

    def find_all_by_index(self, bs, index):
        global selector_array, class_array
        if class_array[index] == 'NONE':
            source = bs.find_all(selector_array[index])
        else:
            source = bs.find_all(selector_array[index], class_= class_array[index])
        return source

    def recursive_search(self, source, level):
        global parser, final_element_array
        bs = BeautifulSoup(str(source), parser)
        next_source = self.find_all_by_index(bs,level) # array of html code snippets that includes the html selector at the level position with it's subsequent class
        if next_source != []:
            for element in next_source:
                if level == len(selector_array)-1:
                    final_element_array.append(element.text)
                else:
                    self.recursive_search(element, level+1)

    def print_final_elements(self, final_element_array, column_name):
        if column_name != '':
            print(column_name)
        for element in final_element_array:
            print(element)

    
    def save_to_csv(self, final_element_array, column_name, output_path):
        
        output_path = output_path.strip('/')
        file_name = output_path.split('/')[-1]
        output_path = output_path.strip(file_name)
        
        if not isdir(output_path):
            makedirs(output_path)

        output_path = output_path + file_name

        if exists(output_path):
            final_data = []
            if column_name == '':
                with open (output_path, 'a', newline='') as csv_output:
                    writer = csv.writer(csv_output)
                    for element in final_element_array:
                        writer.writerow([element])
            else:
                final_element_array.insert(0,column_name)
                with open (output_path, 'r') as csv_input:
                    reader = csv.reader(csv_input)
                    for index, row in enumerate(reader):
                        try:
                            row = row + [final_element_array[index]]
                            final_data.append(row)
                        except:
                            final_data.append(row)

                with open (output_path, 'w', newline='') as csv_output:
                    writer = csv.writer(csv_output)
                    writer.writerows(final_data)
            
        else:
            with open(output_path, 'w', newline='') as csv_output:
                writer = csv.writer(csv_output)
                if (column_name != ''):
                    writer.writerow([column_name])
                for element in final_element_array:
                    writer.writerow([element])

if __name__ == '__main__':
    URL, selector, output_path, column_name = '', '', '', ''
    verbose_bool = False
    selector_array, class_array, final_element_array = [], [], []
    parser = 'html.parser'
    arg_parser()
    
    if selector == '':
        raise Exception('No selector option in the command line')

    if verbose_bool:
        print(f'✔️  Initializing script with the following arguments: URL: {URL}, selector: {selector}, output path: {output_path}')

    page_request = requests.get(URL)
    
    if verbose_bool:
        print(f'✔️  Code of the request is: {page_request}')
    
    source = page_request.text
    
    if verbose_bool:
        print('✔️  Initializing scraper...')
    
    scraper = ScrapeBot(URL, output_path, selector)
    scraper.process_selectors(str(selector))
    
    if verbose_bool:
        print('✔️  Searching the selectors...')
    
    scraper.recursive_search(source, 0)
    if output_path == '':
        if verbose_bool:
            print('✔️  Outputting to screen...')
        scraper.print_final_elements(final_element_array, column_name)
    else:
        if verbose_bool:
            print(f'✔️  Saving to csv file in path: {output_path}')
        scraper.save_to_csv(final_element_array, column_name, output_path)

