{
    'name': 'jmlm/odoo Development Tutorials',
    'version': '14.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'jmlm/Odoo Development Tutorials For Beginners',
    'sequence': '0',
    'license': 'AGPL-3',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'http://odoomates.tech',
    'live_test_url': 'https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1',
    'depends': ['base', 'mail', 'sale', 'web', 'website', 'board' ],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/secquence.xml',
        'data/mail_template.xml',
        'data/data.xml',
        'data/cron.xml',
        'wizards/create_appointment.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/template.xml',
        'views/sale_order.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/appointment.xml',
        'reports/sale_report_inherit.xml',
        'views/lab.xml',
        'views/dashboard.xml',
        'views/server_action.xml',
        'views/patient.xml',
        'views/patient2.xml',
        'views/menu.xml',
        #'reports/my_header.xml',
        #'reports/my_footer.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# Video Explanation: https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1
