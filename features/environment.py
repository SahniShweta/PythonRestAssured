import requests
from utilities.resources import APIResources
from utilities.configurations import *
from payload import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        url1 = getConfig()['API']['endpoint'] + APIResources.deleteBook
        deleteBook_response = requests.post(url1, json=deleteBookPayload(context.bookID), headers=context.headers , )

        assert deleteBook_response.status_code == 200

        res_json = deleteBook_response.json()
        print(res_json['msg'])
        assert res_json['msg'] == 'book is successfully deleted'