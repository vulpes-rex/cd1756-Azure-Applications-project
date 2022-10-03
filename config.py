import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))
params = urllib.parse.quote_plus(
    'Driver=%s;' % 'ODBC Driver 17 for SQL Server' +
    'Server=tcp:%s,1433;' % 'hello-world-server123.database.windows.net' +
    'Database=%s;' % 'hello-world-db' +
    'Uid=%s;' % 'udacityadmin' +
    'Pwd={%s};' % 'Chumlet@1' +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworldblob'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'WOzOvSU61TgCHrT0gPDjWJ09X40xBsdZOnF7vjV4KroJJjlF/XcIsIiGgcPgQq2aCd0PpjdD7GLj+ASt5Jh6Dw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "7_T8Q~YI15H.lz~B~eNRQG8CFkiTS-pVdX5fGcgK"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "5193fef1-6d68-4708-a654-f96a819843da"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session