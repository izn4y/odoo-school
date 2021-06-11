{
    'name': "Schoolmng",
    'version': '1.0',
    'depends': ['base'],
    'author': "Devon",
    'category': 'Human Resources',
    'website': 'https://github.com/izn4y/odoo-school',
    'description': """
        Simple module crud  """,
    'data': [
       'views/iut_Agenda.xml',
       'views/iut_Classe.xml',
       'views/iut_Cours.xml',
       'views/iut_Eleve.xml',
       'views/res_partner.xml',
       'school_menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
