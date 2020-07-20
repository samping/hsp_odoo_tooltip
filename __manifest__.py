# Copyright 2020  HSP
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "HSP提示增强器",

    'summary': """HSP提示增强器
    """,
   'license': 'LGPL-3',
   'description': """
    HSP提示增强器
   """,
    'author': 'HSP',
    'website': "https://www.garage-kit.com",
    'images': ['static/description/logo.png'],
    'category': 'Tools',
    'version': '13.0.1.0.0',
  
    'depends': [
        'base', 'web',
    ],
    'data': [
       'views/template.xml'
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'installable': True,
}
