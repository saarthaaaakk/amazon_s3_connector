
{
    'name': "Odoo Amazon S3 Connector",
    'version': "17.0.1.0.0",
    'category': "Document Management",
    'summary': """ Connect with Amazon S3 Files from Odoo""",
    'description': """This module was developed to upload to Amazon S3 Cloud 
                      Storage as well as access files from Amazon S3 Cloud 
                      Storage in Odoo.""",
    'author': '',
    'company': '',
    'maintainer': '',
    'website': "",
    'depends': ['base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/amazon_dashboard_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/amazon_upload_file_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'amazon_s3_connector/static/src/js/amazon.js',
            'amazon_s3_connector/static/src/xml/amazon_dashboard_template.xml',
            'amazon_s3_connector/static/src/scss/amazon.scss'
        ]
    },
    'external_dependencies': {'python': ['boto3']},
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'uninstall_hook': 'uninstall_hook'
}
