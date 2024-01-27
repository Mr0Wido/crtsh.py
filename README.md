# crtsh.py
**crtsh.py** is a Python script for discovering subdomains from https://crt.sh

### Installation

```
git clone https://github.com/Mr0Wido/crtsh.py.git
cd crtsh.py
python3 crtsh.py
```

### Usage

```
python3 crtsh.py -d example.com
```

### Options
**Flags** |    | Description
---| --- | ---
-h | --help | Show this help message and exit.
-d | --domain | Domain name to search in crt.sh.
-o | --output | Output file to save subdomains.

### Requirments

```
argparse
requests
beautifulsoup4
```
