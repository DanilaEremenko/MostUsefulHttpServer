# MostUsefulHttpServer
## Dependencies
gradle >= 5.0

## Running

    gradle startService

## Examples of working


    request: GET http://localhost?year=2017
    response: {"errorCode": 200, "dataMessage": "13/09/2017"}
    
    request: GET http://localhost?year=2020
    response: {"errorCode": 200, "dataMessage": "12/09/2020"}
    
    request: GET  http://localhost?year=2017s
    response: {"errorCode": 1, "dataMessage": "BAD YEAR NUMBER"}
    
    request: GET http://localhost?yssdear=2017
    response: {"errorCode": 2, "dataMessage": "BAD REQUEST"}