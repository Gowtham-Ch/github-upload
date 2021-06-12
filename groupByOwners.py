def group_by_owners(file_dict):
    output = {}
    for file, owner in file_dict.items():
        output[owner] = output.get(owner, []) + [file]
    return output

files = {    
    'File3.doc': 'Shyak',
    'Test1.txt': 'Person1',
    'Test2.txt': 'Person2',
    'File2.py': 'Godly',
    'Test3.txt': 'Person1',
    'File.txt': 'Danielle'
}

print(group_by_owners(files))
