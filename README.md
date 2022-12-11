# FastScrape
### A simple web scraper written in python and beautifulfoup.

<br>

### **It is meant to be run in the terminal as a command rather than a standalone script.** 

<br>

### **⚠️Note that I am not responsable for any misuse of this script.⚠️**

<br>

# Installation
## **If you don't have git**:
### Click the code button and download the zip, then extract it:
### Insert gif here


<br>

## **If you have git**:
### Use the following command in the termial/command line:
```
git clone <link> 
```

<br>
 
# Usage
## Now you can run the script with this command:
```
./main.py
```
<br>

## To make it run as a command to the following:

<br>

### **For Linux users:**
### Open the terminal in the folder which contains the **main.py** script and type the following:
```
cp ./main.py fastscrape
chmod +x fastscrape
mv fastscrape /bin
fastscrape
```

### You can replace the fastscrape name with any name you want for the command 

<br>

### **For Windows users:**
- Make a bin folder inside your User's folder
- Copy the main.py script in it and remove it's extension
- Rename the main file as the name you want the command to have (In this case fastscrape)
- Type path in Windows search bar and hit enter
- Add the folder in the path as per this gif:

## **INSERT GIF**


<br>

# Commands

```
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
```
### **Notes:**
- The script requires a valid URL and a valid selector to work.
- The verbose argument must be put last in order for the command to work.

<br>

# Features
- If no output argument is given it will print the requested code in the **console**
- You can give a specific path as an output argument, such as: **Desktop/myfolder/results.csv**
- You can give a specific path as a selector argument. For example: **-s div.product_container/div.desc/p**
- You can add columns to the .csv file to make it more easily readable in Excel. Example: **-s Price:div.product_info/p.price**  
- If the path **does not** exist, the program will **create** it
- If no **Column Name** is detected in the selector, it will append the result to the last column created
- If another column exists in the .csv file, it will **append** the result in a different one

<br>

# Example usage
## Using **[QuotesToScrape](https://quotes.toscrape.com/)** website as a dummy example.

<br>

## Extracting all the elements with a specific selector and class (in this example all quotes) and outputting into a folder:

```
./main.py -url https://quotes.toscrape.com/ -selector span.text -o Desktop/some_folder/quotes.csv
```

<br>

## Extracting all the elements from a specific path:

```
./main.py -url https://quotes.toscrape.com/ -selector div.col-md-8/div.quote/span.text -o Desktop/some_folder/quotes.csv
```

<br>

## Outputting the quotes in an excel-friendly column format:

```
./main.py -url https://quotes.toscrape.com/ -selector Quotes:div.col-md-8/div.quote/span.text -o Desktop/some_folder/quotes.csv
```

<br>

## Appending more quotes to the **Quotes** column:

```
./main.py -url https://quotes.toscrape.com/page/2/ -selector div.col-md-8/div.quote/span.text -o Desktop/some_folder/quotes.csv
```

<br>

## Creating a new **Other_Quotes** column in the .csv file with the quotes from page 3:

```
./main.py -url https://quotes.toscrape.com/page/3/ -selector Other_Quotes:div.col-md-8/div.quote/span.text -o Desktop/some_folder/quotes.csv
```

<br>

# Issues
## Feel free to submit issues with bugs that need fixing or with new features that you wish to be added.

## add gif image

<br>

## You can also reach me trough my socials:
- Email: strykez_1@protonmail.com
- Discord: [Roshy#5849](https://discord.com/)
- Twitter: [@strykez_dev](https://twitter.com/strykez_dev)

<br>

# License
### This repo is created under the MIT Licence.
### [LICENCE.MD](df)