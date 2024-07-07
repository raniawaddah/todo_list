# -*- coding: utf-8 -*-
{
    'name': "To-Do List",


    'author': "Rania",


    'category': '',
    'version': '0.1',

    'depends': ['base', 'sale', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'reports/todo_report.xml',

    ],

    # 'assets': {
    #   'web.assets_backend':['app_one/static/src/css/property.css']
    # },

    'application':True,

}
