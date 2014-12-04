from django.shortcuts import render_to_response

req_item = [
    {
        "id": 1,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "hg",
        "quantity": 1,
        "description": "hgfjjhg",
        "ashramId": "Kaka Ashram hfghhhhhhhhhhhhhhhhhhhhh"
    },
    {
        "id": 2,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "erte",
        "quantity": 1,
        "description": "erter",
        "ashramId": "Kaka Ashram hghjghgjhgjg"
    },
    {
        "id": 3,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "hg",
        "quantity": 1,
        "description": "hgfjjhg",
        "ashramId": "Kaka Ashram"
    },
    {
        "id": 4,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "erte",
        "quantity": 1,
        "description": "erter",
        "ashramId": "Kaka Ashram"
    },    {
        "id": 5,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "hg",
        "quantity": 1,
        "description": "hgfjjhg",
        "ashramId": "Kaka Ashram"
    },
    {
        "id": 6,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "erte",
        "quantity": 1,
        "description": "erter",
        "ashramId": "Kaka Ashram"
    },    {
        "id": 7,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "hg",
        "quantity": 1,
        "description": "hgfjjhg",
        "ashramId": "Kaka Ashram"
    },
    {
        "id": 8,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "erte",
        "quantity": 1,
        "description": "erter",
        "ashramId": "Kaka Ashram"
    },
    {
        "id": 9,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "hg",
        "quantity": 1,
        "description": "hgfjjhg",
        "ashramId": "Kaka Ashram"
    },
    {
        "id": 10,
        "createdDate": "2014-12-03T19:07:31.172Z",
        "modifiedDate": "2014-12-03T19:07:31.172Z",
        "name": "erte",
        "quantity": 1,
        "description": "erter",
        "ashramId": "Kaka Ashram"
    },
]


def sample_html(request):
    return render_to_response('home.html', {"item_list":req_item})

def donations_html(request):
    return render_to_response('donations.html')