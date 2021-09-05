#!/usr/bin/python3

import os
from pcvalidator import validation

# import variables collected with bash script
changed_files = os.environ.get('changed_files').split()
all_assemblies = os.environ.get('all_assemblies').split()
all_modules = os.environ.get('all_modules').split()
undetermined_file_type = os.environ.get('undetermined_file_type').split()

# call validation from the main validation script
validate = validation(changed_files, all_modules, all_assemblies)

if validate.count != 0:
    print("\nThe following files did not pass validation:\n")
    validate.print_report()
    if undetermined_file_type:
        print("\nThe following files can not be identifiyed as modules or assemblies:\n")
        for file in undetermined_file_type:
            print('\t' + file)
        print("\n\tPlease add one of the following tags to modules:")
        print("\n\t\t:_module-type: CONCEPT\n\t\t:_module-type: PROCEDURE\n\t\t:_module-type: REFERENCE")
        print("\n\tOr add one of the following prefixes to the file names:")
        print("\n\t\tcon_, proc_, ref_, assembly_")
else:
    print("All files passed validation.")
