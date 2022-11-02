from .settings import *

INSTALLED_APPS += [
    'rest_framework',
]

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ],
#     'DEFAULT_PARSER_CLASSES': [
#         'rest_framework_xml.parsers.XMLParser',
#         'rest_framework.parsers.JSONParser',
#         'rest_framework.parsers.FormParser',
#         'rest_framework.parsers.MultiPartParser',
#     ],
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework_xml.renderers.XMLRenderer',
#         'rest_framework_csv.renderers.CSVRenderer',
#
#     ],
# }
