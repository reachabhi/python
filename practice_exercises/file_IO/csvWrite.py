'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

from csv import writer
def add_user(first_name,last_name):
    with open('users.csv', 'a') as f:
        csv_writer = writer(f)
        csv_writer.writerow([first_name,last_name])
def read_user():
    with open('users.csv') as f:
        data = reader(f)
        for row in data:
            print(row)

        
