import requests
from behave import *
from requests.auth import HTTPBasicAuth

from utilities.resources import APIResources
from utilities.configurations import *
from payload import *


@given('The book details that are needed to be added to the Library')
def step_Impl(context):
    context.url = getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookPayload('sahni4', '279')


@when('we execute the AddBook POSTAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    response_json = context.response.json()
    print(response_json)
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == "successfully added"


@given('The book details with {isbn} and {aisle} added to the Library')
def step_Impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payload = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = HTTPBasicAuth('SahniShweta', 'dd1e5c84f5a903a5df242d48d4ae4ae9314089e7')


@when('I hit gitRepo API of github')
def step_impl(context):
    context.response = context.se.get(APIResources.githubRepo)


@then('status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
