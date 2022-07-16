# -*- coding: utf-8 -*-

import requests
import json


def storetype_verify_grab(store_type):

    URL= 'http://microservices.dev.rappi.com'
    headers = {
        'Authorization': 'df3fcd99-e9e4-47a3-b7ff-f642ca4c',
        'Content-Type': 'application/json',
        'user': 'kissflow_retail',
        'cms-onboard-setting-user': 'kissflow_retail'
    }
    err_check = ''
    url = URL+'/api/cms/gateway/cms-stores/api/cms/stores/store-types/?id='+store_type
    print('grabtype: ',url)
    print('grabtype_headers: ', headers)
    response = requests.get(url, headers=headers)
    print('Hola')
    type_id = response.content
    type_id = json.loads(type_id)
    print('GrabType: ',type_id)
    type_id = type_id['data']

    if response.status_code != 200:
        print('err_check: ',err_check)
        return err_check
    else:
        if len(type_id) >= 1:
            print('type_id: ',type_id)
            return type_id
        else:
            return err_check



if __name__ == '__main__':
    storetype_verify_grab('qewwwer100')
