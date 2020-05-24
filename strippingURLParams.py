def strip_url_params(url, params_to_strip=None):
    # 0: check if there are any parameters. If not just return the URL
    try:
        params = url[url.index('?'):]
    except ValueError:
        return url
    
    # 1: remove any duplicate query string parameters
    # redefine params now url has possibly changed
    params = url[url.index('?'):]

    # define empty keys and unique keys list
    keys = []
    unique_keys = []

    # create keys and unique keys list
    idx = 0
    #print(params)
    for i in params:

        if idx != len(params) and idx != len(params)-1:
            if params[idx + 1] == '&' or params[idx] == '&' or params[idx] == '=' or params[idx] == '?':

                #print('i=',i,'  idx=',idx,'  params[idx+1]=',params[idx+1],'  params[idx]=',params[idx],'  This row was skipped.')
                idx += 1
                continue
            elif i not in keys:
                unique_keys.append(i)
                keys.append(i)
            else:
                keys.append(i)
        idx += 1

    #print(keys)

    # in this case, no duplicates. Return URL.
    if unique_keys == keys:
        url = url

    # all other cases, we know there are duplicates
    else:
        #change url to list to enable pop method
        url_list = []
        #define key_check list for checking
        key_check = []

        #initialise value_removed to false
        key_removed = False
        for i in range(len(url)):


            if key_removed == True and url[i] == '=':
                # in this case, we've found a duplicate
                # skip the '=' symbol
                # continue, without appending to resulting URL
                #print("duplicate found. Skipping equals sign.")
                continue

            elif key_removed == True and url[i-1] == '=':
                # in this case, we've found a duplicate
                # skip the value
                # continue, without appending to resulting URL
                #print("duplicate found. Skipping value.")
                key_removed = False
                continue

            elif url[i] in keys and url[i] in key_check and url[i-1] == '&':
                # in this case, we've found a duplicate
                # skip the key
                # continue, without appending to resulting URL
                #print("duplicate found. Skipping key and deleting preceding ampersand.")
                key_removed = True
                #ALSO, delete last element of url_list as this will be the unneeded ampersand
                del(url_list[-1])
                continue

            else:
                url_list.append(url[i])

            #append to key check for checking keys:
            if url[i] in keys:
                key_check.append(url[i])

        # finally, join url list
        url = ''.join(url_list)

    # 2: strip parameters
    params = url[url.index('?'):]
    params_list = list(params)
    if params_to_strip != None:
        #print("parameter to strip found")
        # change url to list to enable pop method
        url_list = list(url)
        for i in params_to_strip:
            params_list.pop(params_list.index(i) - 1)  # strip ampersand
            params_list.pop(params_list.index(i) + 1)  # strip equals sign
            params_list.pop(params_list.index(i) + 1)  # strip value
            params_list.pop(params_list.index(i))  # finally, strip key
        url = url[:url.index('?')] + ''.join(params_list)
    return url
