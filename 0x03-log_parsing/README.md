# 0x03. Log Parsing

This project contains a script for parsing log data in a specific format and computing metrics from it.

## Requirements
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files must end with a new line
- First line of all files must be exactly `#!/usr/bin/python3`
- Code should use the `PEP 8` style (version 1.7.x)
- All files must be executable

## Task 0: Log parsing

The script `0-stats.py` reads from standard input (stdin) line by line and computes metrics based on the input following this format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints:
- Total file size: `File size: <total size>`
- Number of lines by status code in ascending order (only status codes: 200, 301, 400, 401, 403, 404, 405 and 500)

### Usage

```bash
$ ./0-generator.py | ./0-stats.py
```

The generator script `0-generator.py` creates random log lines to test the parsing script.

### Example Output

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

Note: The actual numbers will vary as the generator produces random values.
