# max-words

This utility was written with two flavors.
The first flavor, Must, can be viewed either from master branch or from 0.1
The second flavor, Advantage, can be viewed from branch 0.2

## Dependencies
**Python 3.7** or higher is required.
For the rest, simply run `pip install singleton-decorator pytest pytest-html`

## Execution
Under the `src/` directory, execute either `max-words-must.py` or `max-words-advantage.py` as follows::

```python max-words.py -h                                                                        
usage: max-words.py [-h] num_of_words filename_or_directory [filename_or_directory ...] [--debug]

Find the most common words in given file/dir path(s)                                            
                                                                                                
positional arguments:                                                                           
  num_of_words  Amount of most common words returned                                            
  file_or_dir   Absolute path to file(s) or directory/directories                               
                                                                                                
optional arguments:                                                                             
  -h, --help    show this help message and exit                                                 
  --debug       Activate debug logs                                                             
                                                                                                
Examples:                                                                                       
max-words.py 3 /tmp                                                                           
max-words.py 5 /home/user/file.txt                                                            
max-words.py 10 /var/log/ /tmp/file.txt
max-words.py -h  
```

## Tests
1. Add the full path of max-words\src and max-words\test to `PYTHONPATH` (i.e. ```PYTHONPATH=C:\git\word_count\max-words\src:C:\git\word_count\max-words\test```)
2. Execute `pytest --html=report.html` from command line
