{
    'name': 'MQTT MAnresa Demo',
    'version': '1.0',
    'summary': 'Live MQTT data display in Odoo',
    'description': 'Fetches counter from mosquitto.',
    'author': 'Daniel',
    'category': 'Tools',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/mqtt_dashboard.xml',],
    'installable': True,
    'application': False,
}