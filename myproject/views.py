from pyramid.view import view_config
from bs4 import BeautifulSoup
import httplib2


@view_config(route_name='home', request_method='GET', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'MyProject'}


@view_config(route_name='home', request_method='POST', renderer='templates/index.jinja2')
def result_view(request):
    url = request.params['url']

    http = httplib2.Http()
    response = ''
    status_msgs = ''


    try:
        status, response = http.request(url)
    except:
        status_msgs = True
    extract = BeautifulSoup(response)
    toc = extract.find_all(attrs={'class': 'mw-headline'})
    output = []
    for span in toc:
        output.append(span.text)
    return {
            'extract': output,
            'query': url,
            'status': status_msgs,
            'h2s': toc,
            'searched': True,
            'project': 'MyProject'
            }
