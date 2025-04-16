-- Drop tables if they exist
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;

-- Create Account table
CREATE TABLE accounts (
    account_name VARCHAR(20) PRIMARY KEY,
    accounting_region VARCHAR(50),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Transactions table
CREATE TABLE transactions (
    transaction_id VARCHAR(100) PRIMARY KEY,
    account_name VARCHAR(20),
    amount NUMERIC(12, 2),
    trade_date DATE,
    settlement_date DATE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_name) REFERENCES accounts(account_name)
);
