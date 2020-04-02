import json,jsonpath

a = '''
{
    "data": {
        "pagingSearchData": {
            "paging": {
                "pageSize": "10",
                "pageNumber": "1",
                "pageIndex": "1",
                "totalRecordNumber": "1"
            },
            "results": [
                {
                    "id": "6312727f5d9611392da56edefe3b2781",
                    "partNo": "946-08762-TL",
                    "totalInStock": "3050",
                    "totalInStockUnit": "PCS",
                    "totalInTransit": "3050",
                    "mgtMode": "VMI",
                    "uom": "PCS",
                    "inventorySituations": [
                        {
                            "emergency": "WARNING",
                            "estimateStocksLevels": [
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "1000",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582214400000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "1000",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582300800000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "1000",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582387200000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "300",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582473600000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "1000",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582560000000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "91970",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582646400000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "300",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582732800000"
                                }
                            ],
                            "warehouseCode": "Y1",
                            "warehouseName": "Y1",
                            "inStock": "3000",
                            "inStockUnit": "PCS",
                            "availableStock": "0",
                            "availableStockUnit": "PCS",
                            "plannedIn": "3000",
                            "plannedOut": "7000",
                            "inboundQuantities": [
                                {
                                    "dateTime": "1582128000000",
                                    "quantity": "900"
                                },
                                {
                                    "dateTime": "1582214400000",
                                    "quantity": "3000"
                                },
                                {
                                    "dateTime": "1582300800000",
                                    "quantity": "3000"
                                },
                                {
                                    "dateTime": "1582387200000",
                                    "quantity": "3000"
                                },
                                {
                                    "dateTime": "1582473600000",
                                    "quantity": "900"
                                },
                                {
                                    "dateTime": "1582560000000",
                                    "quantity": "3000"
                                },
                                {
                                    "dateTime": "1582646400000",
                                    "quantity": "15"
                                },
                                {
                                    "dateTime": "1582732800000",
                                    "quantity": "900"
                                }
                            ],
                            "outboundQuantities": [
                                {
                                    "dateTime": "1582128000000",
                                    "quantity": "1500"
                                },
                                {
                                    "dateTime": "1582214400000",
                                    "quantity": "7000"
                                },
                                {
                                    "dateTime": "1582300800000",
                                    "quantity": "7000"
                                },
                                {
                                    "dateTime": "1582387200000",
                                    "quantity": "7000"
                                },
                                {
                                    "dateTime": "1582473600000",
                                    "quantity": "1500"
                                },
                                {
                                    "dateTime": "1582560000000",
                                    "quantity": "7000"
                                },
                                {
                                    "dateTime": "1582646400000",
                                    "quantity": "92000"
                                },
                                {
                                    "dateTime": "1582732800000",
                                    "quantity": "1500"
                                }
                            ],
                            "outboundPolymerizationQuantities": {
                                "4": {
                                    "id": "4",
                                    "quantity": "22500"
                                },
                                "5": {
                                    "id": "5",
                                    "quantity": "100500"
                                },
                                "6": {
                                    "id": "6",
                                    "quantity": "0"
                                },
                                "7": {
                                    "id": "7",
                                    "quantity": "0"
                                }
                            },
                            "inboundPolymerizationQuantities": {
                                "4": {
                                    "id": "4",
                                    "quantity": "9900"
                                },
                                "5": {
                                    "id": "5",
                                    "quantity": "3915"
                                },
                                "6": {
                                    "id": "6",
                                    "quantity": "0"
                                },
                                "7": {
                                    "id": "7",
                                    "quantity": "0"
                                }
                            }
                        },
                        {
                            "emergency": "WARNING",
                            "estimateStocksLevels": [
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "30",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582214400000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "30",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582300800000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "30",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582387200000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "12400",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582473600000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "30",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582560000000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "399940",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582646400000"
                                },
                                {
                                    "stockStatus": "MIN",
                                    "dynamicStock": "782000",
                                    "safeLowerLimit": "26000",
                                    "safeUpperLimit": "120000",
                                    "estimateDate": "1582732800000"
                                }
                            ],
                            "warehouseCode": "Y8",
                            "warehouseName": "Y8",
                            "inStock": "50",
                            "inStockUnit": "PCS",
                            "availableStock": "0",
                            "availableStockUnit": "PCS",
                            "plannedIn": "50",
                            "plannedOut": "70",
                            "inboundQuantities": [
                                {
                                    "dateTime": "1582128000000",
                                    "quantity": "8700"
                                },
                                {
                                    "dateTime": "1582214400000",
                                    "quantity": "50"
                                },
                                {
                                    "dateTime": "1582300800000",
                                    "quantity": "50"
                                },
                                {
                                    "dateTime": "1582387200000",
                                    "quantity": "50"
                                },
                                {
                                    "dateTime": "1582473600000",
                                    "quantity": "8700"
                                },
                                {
                                    "dateTime": "1582560000000",
                                    "quantity": "50"
                                },
                                {
                                    "dateTime": "1582646400000",
                                    "quantity": "30"
                                },
                                {
                                    "dateTime": "1582732800000",
                                    "quantity": "9000"
                                }
                            ],
                            "outboundQuantities": [
                                {
                                    "dateTime": "1582128000000",
                                    "quantity": "5000"
                                },
                                {
                                    "dateTime": "1582214400000",
                                    "quantity": "70"
                                },
                                {
                                    "dateTime": "1582300800000",
                                    "quantity": "70"
                                },
                                {
                                    "dateTime": "1582387200000",
                                    "quantity": "70"
                                },
                                {
                                    "dateTime": "1582473600000",
                                    "quantity": "5000"
                                },
                                {
                                    "dateTime": "1582560000000",
                                    "quantity": "70"
                                },
                                {
                                    "dateTime": "1582646400000",
                                    "quantity": "400000"
                                },
                                {
                                    "dateTime": "1582732800000",
                                    "quantity": "800000"
                                }
                            ],
                            "outboundPolymerizationQuantities": {
                                "4": {
                                    "id": "4",
                                    "quantity": "5210"
                                },
                                "5": {
                                    "id": "5",
                                    "quantity": "1200070"
                                },
                                "6": {
                                    "id": "6",
                                    "quantity": "0"
                                },
                                "7": {
                                    "id": "7",
                                    "quantity": "0"
                                }
                            },
                            "inboundPolymerizationQuantities": {
                                "4": {
                                    "id": "4",
                                    "quantity": "8850"
                                },
                                "5": {
                                    "id": "5",
                                    "quantity": "9080"
                                },
                                "6": {
                                    "id": "6",
                                    "quantity": "0"
                                },
                                "7": {
                                    "id": "7",
                                    "quantity": "0"
                                }
                            }
                        }
                    ]
                }
            ]
        },
        "polymerizationRules": [
            {
                "id": "4",
                "title": "plannedInAndOutOneStage",
                "titleDescribe": "0-3 Days Planned In&Out",
                "beginDay": "0",
                "endDay": "3"
            },
            {
                "id": "5",
                "title": "plannedInAndOutTwoStage",
                "titleDescribe": "4-7 Days Planned In&Out",
                "beginDay": "4",
                "endDay": "7"
            },
            {
                "id": "6",
                "title": "plannedInAndOutThreeStage",
                "titleDescribe": "8-15 Days Planned In&Out",
                "beginDay": "8",
                "endDay": "15"
            },
            {
                "id": "7",
                "title": "plannedInAndOutThreeStage",
                "titleDescribe": "16 Days+ Planned In&Out",
                "beginDay": "16",
                "endDay": null
            }
        ]
    },
    "success": true,
    "errorType": null,
    "errorCode": null,
    "errorData": null,
    "message": null
}
'''

b = json.loads(a)

x = jsonpath.jsonpath(b,'$..results[0].id')
print(x)