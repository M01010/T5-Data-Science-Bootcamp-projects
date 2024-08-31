# how to use
1. enter username - if the user exists it will use the old date for the user, otherwise it will create a new user.
2. choose choice between the following:
    - add: add a transaction
    - view date: view transactions by date
    - view category: view transactions by category
    - update: update a transaction
    - delete: delete a transaction
    - report: view transaction reports
    - exit: exit and save user data
## add
1. enter id (string): if it exists we will stop adding the transaction
2. enter amount (float)
3. enter category (food/transportation/entertainment/salary/other)
4. enter date (mm/dd/yyyy) e.g. 01/01/2020

## update
1. enter id (string): if it exists we will stop updating the transaction
2. enter what you will change (amount, category, date)
3. enter the value
## delete
1. enter id (string): if it exists we will delete it otherwise we will exit
## report
choices:
- expense
- income
- total category
- average category

