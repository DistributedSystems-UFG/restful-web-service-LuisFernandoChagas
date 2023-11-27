import requests
import const

def serviceTester():
    api_base_url_employee = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    api_base_url_wage = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/wage'

    print ('Will connect to: ' + api_base_url_employee)
    
    # Test get_all_employees endpoint
    api_url = api_base_url_employee
    print ('Calling GET on endpoint: ' + api_url)
    response = requests.get(api_url)
    print (response.json())

    # Test get_an_employee endpoint
    api_url = api_base_url_employee + '/201'
    print ('Calling GET on endpoint: ' + api_url)
    response = requests.get(api_url)
    print (response.json())

    # Test get_highest_wage endpoint
    api_url = api_base_url_wage + '/highwage'
    print ('Calling GET on endpoint: ' + api_base_url_wage + '/highwage')
    response = requests.get(api_base_url_wage+'/highwage')
    print (response.json())

    # Test get_avarage_wage endpoint
    api_url = api_base_url_wage + '/averagewage'
    print ('Calling GET on endpoint: ' + api_base_url_wage + '/averagewage')
    response = requests.get(api_base_url_wage+'/averagewage')
    print (response.json())

    # Test update_employee endpoint
    api_url = api_base_url_employee + '/101'
    update = {"title":"Programmer"}
    print ('Calling PUT on endpoint: ' + api_url)
    response = requests.put(api_url, json=update)
    print (response.json())
    
    # Test update_salary endpoint
    api_url = api_base_url_employee + '/201'+'/4000'
    print ('Calling PUT on endpoint: ' + api_url)
    response = requests.put(api_url, json=update)
    print (response.json())

    # Test create_employee endpoint
    api_url = api_base_url_employee
    employee = {"id":"301", "name":"Juaríssimo Salvo", "title":"Sr Programmer", "salary":"3000"}
    print ('Calling POST on endpoint: ' + api_url)
    response = requests.post(api_url, json=employee)
    print (response.json())

    # Test delete_employee endpoint
    api_url = api_base_url_employee + '/101'
    print ('Calling DELETE on endpoint: ' + api_url)
    response = requests.delete(api_url)
    print (response.json())

    # This endpoint does not exist in the service -- will result in an HTTP 404 error
    api_url = api_base_url_employee + '/201/40000/Programmer'
    print ('Calling PUT on endpoint: ' + api_url)
    try:
        response = requests.put(api_url, json=update)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh: 
        print("HTTP Error") 
        print(errh.args[0])
    else:
        print (response.json())

if __name__ == '__main__':
    serviceTester()
