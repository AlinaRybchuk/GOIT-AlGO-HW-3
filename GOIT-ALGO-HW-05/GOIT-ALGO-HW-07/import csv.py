import csv

def write_contacts_to_file(filename, contacts):
    with open (filename, 'w', newline = '', encoding = 'utf-8') as fh:  
     columns = ['name', 'email', 'phone', 'favorite']       
     writer = csv.DictWriter(fh, delimiter = ",", fieldnames=columns)
     writer.writeheader()
     for row in contacts:
         writer.writerow(row)       
           
def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', encoding = 'utf-8', newline = '') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
              favorite = row.get("favorite")  
        if favorite == "True" and "False":
              row ['favorite'] = True
        else:
              row['favorite'] = False
        contacts.append(row)  
    return contacts