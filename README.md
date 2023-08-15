# python-boto3-utilities

Helper scripts for maintenance.  Script names are self-explanatory.

This script will delete all of the published versions of a single lambda function while ignoring any Aliased versions that you have created.  $LATEST version will also be ignored.  Delete operation is commented out for safety purposes. Run the script first with print to see the list to be delete.
    
    Python Script Name:  DeleteLambdaVersionsByFunctionArnKeepVersionsWithAliases.py
    Requirement:         boto3
    Input variable:      Name of lambda function
