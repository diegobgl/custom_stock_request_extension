
{
    'name': 'Custom Stock Request Progress',
    'version': '1.0',
    'category': 'Stock',
    'summary': 'Muestra una barra de progreso en el formulario de solicitud de stock',
    'description': '''
    Este módulo añade una barra de progreso en el formulario de órdenes de solicitud de stock, indicando
    los campos que se deben completar en orden y habilitándolos conforme se vayan llenando.
    ''',
    'depends': ['stock_request', 'web'],
    'data': [
        'views/stock_request_order_views_inherit.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_stock_request_extension/static/src/js/stock_request_progress.js',
        ],
    },
    'installable': True,
    'application': False,
}
