```py

def ParseNamesByGroup(blob, group_name):
    obj = blob.split('[')
    result_names_list = []
    for o in obj:
        if group_name in o:
            user_name = o.split('"user_name":"')[1].split('"')[0]
            result_names_list.append(user_name)
    return result_names_list
   
data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print result_names_list
```