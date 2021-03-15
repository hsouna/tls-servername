# tls-servername
This python script is usefull to get servernames from the 'TLS_Ext_ServerName' using scapy


## Set up
Make sure you have Python3+ installed

### Clone the repo
```bash
$ git clone https://github.com/hsouna/tls-servername
```

### Install requirements 

```bash
$ pip install -r requirements.txt
```

### Usage

```bash
$ python3 get_servername_from_tls.py -h             
usage: get_servername_from_tls.py [-h] -f FILENAME [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Input file name
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file name

```

### Output

![Screenshot from 2021-03-16 00-28-55](https://user-images.githubusercontent.com/13191315/111234510-f7246400-85ee-11eb-809a-f33fcf65adfd.png)
