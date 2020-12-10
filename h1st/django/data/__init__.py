from django.apps.config import AppConfig

from pathlib import Path


class H1stDataModuleConfig(AppConfig):
    # AppConfig.name
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to.
    # It must be set in all AppConfig subclasses.
    # It must be unique across a Django project.
    name = 'h1st.django.data'

    # AppConfig.label
    # Short name for the application, e.g. 'admin'
    # This attribute allows relabeling an application
    # when two applications have conflicting labels.
    # It defaults to the last component of name.
    # It should be a valid Python identifier.
    # It must be unique across a Django project.
    label = 'H1stData'

    # AppConfig.verbose_name
    # Human-readable name for the application, e.g. “Administration”.
    # This attribute defaults to label.title().
    verbose_name = 'Human-First AI: Data'

    # *** DURING AWS EB DEPLOYMENT ***
    # The app module <module '...' (namespace)>
    # has multiple filesystem locations (['...', '...']);
    # you must configure this app with an AppConfig subclass
    # with a 'path' class attribute.

    # AppConfig.path
    # Filesystem path to the application directory,
    # e.g. '/usr/lib/pythonX.Y/dist-packages/django/contrib/admin'.
    # In most cases, Django can automatically detect and set this,
    # but you can also provide an explicit override as a class attribute
    # on your AppConfig subclass.
    # In a few situations this is required; for instance if the app package
    # is a namespace package with multiple paths.
    path = Path(__file__).parent
