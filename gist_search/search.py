from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    results = []
    
    gists = get_gists(username)
    
    for gist in gists:
        if description and description.lower() not in gist['description'].lower():
            continue
            
        if file_name:
            found = False
            
            for fname in gist['files']:
                if file_name.lower() in fname.lower:
                    found = True
                    break
            if not found:
                continue
            
        results.append(gist)
        
        
    return results
#         if description and file_name:
            
#         elif description:
            
#         elif file_name:
        
#         if description:
#             if description.lower() in gist['description'].lower():
#                 results.append(gist)
                
#         if file_name:
#             for fname in gist['files']:
#                 if file_name.lower() in fname.lower():
#                     if gist not in results:
#                         results.append(gist)
#                     break

