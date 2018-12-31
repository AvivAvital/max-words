# max-words

This utility was written with two flavors.
The first flavor, Must, can be viewed either from master branch or from 0.1
The second flavor, Advantage, can be viewed from branch 0.2

## Dependencies
**Python 3.7** or higher is required.
For the rest, simply run `pip install singleton-decorator pytest pytest-html`

## Execution
Under the `src/` directory, execute `max-words.py` as follows::

```python max-words.py -h                                                                        
usage: max-words.py [-h] num_of_words timestamp_or_datetime_range [timestamp_or_datetime_range ...] [--debug]                               
                                                                                                                                            
Find the most common words in given file/dir path(s)                                                                                        
                                                                                                                                            
positional arguments:                                                                                                                       
  num_of_words       Amount of most common words returned                                                                                   
  date_or_timestamp  timestamp/datetime format                                                                                              
                                                                                                                                            
optional arguments:                                                                                                                         
  -h, --help         show this help message and exit                                                                                        
  --debug            Activate debug logs                                                                                                    
                                                                                                                                            
Examples:                                                                                                                                   
max-words.py 3 1300000000                                                                                                                  
max-words.py 3 1300000000-1300000001                                                                                                
max-words.py 3 1300000000-1300000001,1300000002-1300000003                                                                             
max-words.py 10 "Sun Aug 30 14:32:28 IDT 2015"-"Sun Aug 30 14:32:36 IDT 2015"                                                               
max-words.py 5 "Sun Aug 30 14:32:28 IDT 2015"-"Sun Aug 30 14:32:36 IDT 2015","Wed Dec 12 00:00:00 IDT 2018"-"Wed Dec 12 10:52:39 IDT 2018"
max-words.py -h                                                                                                                             
```

## Tests
1. Add the full path of max-words\src and max-words\test to `PYTHONPATH` (i.e. ```PYTHONPATH=C:\git\word_count\max-words\src:C:\git\word_count\max-words\test```)
2. Execute `pytest --html=report.html` from command line
