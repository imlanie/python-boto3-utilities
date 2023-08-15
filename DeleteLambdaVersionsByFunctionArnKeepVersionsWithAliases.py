
import boto3

lambda_client = boto3.client('lambda', region_name='us-west-2')

function_name = 'your-function-name-only'
pages = {}
lst_to_keep = []

paginator = lambda_client.get_paginator('list_versions_by_function')
pages = paginator.paginate(FunctionName=function_name, PaginationConfig={
                           'MaxItems': 100, 'PageSize': 12})

aliases = lambda_client.list_aliases(
    FunctionName=function_name)['Aliases']

for page in pages:

    item = page['Versions']

    for i in range(len(item)):
        fnc_arn = item[i]['FunctionArn']

        # extract the version number from the ARN to be used to compare with alias version number
        get_colon = fnc_arn.rfind(':')
        get_colon = get_colon + 1
        fnc_ver = fnc_arn[get_colon:]

        for a in aliases:
            alias_version = a['FunctionVersion']
            if alias_version == fnc_ver:

                keep_fnc = fnc_ver
                # build a list of functions that have aliass
                lst_to_keep.append(fnc_arn)
                print(lst_to_keep)

                # print("match found: " + alias_version + "=" + fnc_ver)
                # print(
                #     "This function has an associated Alias, do not delete it " + keep_fnc)

        # ignore any functions that are in the functions to keep list
        if fnc_arn in lst_to_keep:
            pass
        else:
            print("function version to delete: " + fnc_arn)
            # lambda_client.delete_function(FunctionName=fnc_arn)
