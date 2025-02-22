## Challenge Description

This CTF challenge requires you to calculate Marginal Income Tax based on provided tax form data. The calculation includes:
- Federal Tax (progressive brackets)
- State Tax
- FICA Tax (7.65%)

### Formula
```
TOTAL TAX = STATE + FEDERAL + FICA
```

## Example Calculation

Given:
```
Status: Single
Income: 956150
State: Dakota
```

Calculation:
- FICA = 0.0765 * 956150 = 73145.475
- STATE = 0 (Dakota has 0% tax rate)
- FEDERAL = Progressive brackets calculation:
  - (11600 - 0) * 0.10
  - (47150 - 11600) * 0.12
  - (100525 - 47150) * 0.22
  - (191950 - 100525) * 0.24
  - (243725 - 191950) * 0.32
  - (609350 - 243725) * 0.35
  - (956150 - 609350) * 0.37
  = 311963.25

Total: 0 + 311963.25 + 73145.475 = 385108.72

## Solution Usage

1. Replace the team number in `tax_calc.py`:
   ```python
   host = '192.168.T.129'  # Replace T with your team number
   ```

2. Run the script:
   ```bash
   python tax_calc.py
   ```

## Important Notes

- All calculations are rounded to 2 decimal places using Python's `round()` function
- FICA is calculated at a flat 7.65%
- No deductions or local taxes are included
- The script connects to the service via netcat on port 1234

## Files

- `tax_calc.py` - Main solution script
- `README.md` - This documentation

## Requirements

- Python 3.x
- Standard library modules used:
  - socket
  - re 
