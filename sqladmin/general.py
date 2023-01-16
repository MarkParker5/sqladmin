
def https_url_for(request, name: str, **path_params) -> str: 
    return request.url_for(name, **path_params).replace('http', 'https', 1)

