# Date Range Cli
A cli program written in python 3 that outputs all dates between two inputted dates inclusively or non-inclusively

## Usage
``` console
python3 date_range.py <start_date> \end_date> [options]
```

## options
- `-i`, `--inclusive`: Includes both the start and end dates in the range.
- `-s`, `--start-inclusive`: Includes the start date in the range.
- `-i`, `--end-inclusive`: Includes the end date in the range.

## examples
`python3 date_range.py 28/10/2023 21/06/2024`: lists dates starting at 29/10/2023 to 20/06/2024.\
`python3 date_range.py -i 28/10/2023 21/06/2024`: lists dates starting at 28/10/2023 to 21/06/2024.\
`python3 date_range.py -s 28/10/2023 21/06/2024`: lists dates starting at 28/10/2023 to 20/06/2024.\
`python3 date_range.py -e 28/10/2023 21/06/2024`: lists dates starting at 29/10/2023 to 21/06/2024.
