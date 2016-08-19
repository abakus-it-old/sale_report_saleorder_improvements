{
    'name': 'Sale Order Improvements',
    'version': '9.0.1.0',
    'category': 'Sales',
    'description': 
    """Sale Order Improvements. 

This modules adds a last page to each sales order report with the company sales conditions.

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions.
    """,
    'depends': [
        'base_setup',
        'sale',
    ],
    'data': [
        'report/report_saleorder.xml',
        'report/report_saleorder_conditions.xml',
    ],
    'installable': True,
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
}
