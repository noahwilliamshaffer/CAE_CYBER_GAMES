#!/usr/bin/env python3
import socket
import re

# Federal tax brackets for single filers (2023)
FEDERAL_BRACKETS = [
    (0, 11600, 0.10),
    (11600, 47150, 0.12),
    (47150, 100525, 0.22),
    (100525, 191950, 0.24),
    (191950, 243725, 0.32),
    (243725, 609350, 0.35),
    (609350, float('inf'), 0.37)
]

# State tax rates (simplified for the challenge)
STATE_RATES = {
    'Dakota': 0.0,  # Example state, add more as needed
}

FICA_RATE = 0.0765  # 7.65% for FICA

def calculate_federal_tax(income):
    total_tax = 0
    for lower, upper, rate in FEDERAL_BRACKETS:
        if income > lower:
            taxable_amount = min(income - lower, upper - lower)
            total_tax += taxable_amount * rate
    return total_tax

def calculate_state_tax(income, state):
    rate = STATE_RATES.get(state, 0.0)
    return income * rate

def calculate_fica(income):
    return income * FICA_RATE

def calculate_total_tax(status, income, state):
    federal = calculate_federal_tax(income)
    state_tax = calculate_state_tax(income, state)
    fica = calculate_fica(income)
    total = federal + state_tax + fica
    return round(total, 2)

def parse_input(data):
    # Extract status, income, and state from input
    status_match = re.search(r'Status: (\w+)', data)
    income_match = re.search(r'Income: (\d+)', data)
    state_match = re.search(r'State: (\w+)', data)
    
    if not all([status_match, income_match, state_match]):
        raise ValueError("Could not parse input data")
    
    status = status_match.group(1)
    income = int(income_match.group(1))
    state = state_match.group(1)
    
    return status, income, state

def main():
    # Connect to the service
    host = '192.168.T.129'  # Replace T with team number
    port = 1234

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            # Receive data
            data = s.recv(1024).decode()
            print(f"Received: {data}")
            
            # Parse and calculate
            status, income, state = parse_input(data)
            total_tax = calculate_total_tax(status, income, state)
            
            # Send result
            response = f"{total_tax}\n"
            s.send(response.encode())
            
            # Get response
            result = s.recv(1024).decode()
            print(f"Server response: {result}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 