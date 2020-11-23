from django.apps.config import AppConfig


class H1AIDataAppConfig(AppConfig):
    # AppConfig.name
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to.
    # It must be set in all AppConfig subclasses.
    # It must be unique across a Django project.
    name = 'h1ai_django.data'

    # AppConfig.label
    # Short name for the application, e.g. 'admin'
    # This attribute allows relabeling an application
    # when two applications have conflicting labels.
    # It defaults to the last component of name.
    # It should be a valid Python identifier.
    # It must be unique across a Django project.
    label = 'H1AI_Data'

    # AppConfig.verbose_name
    # Human-readable name for the application, e.g. “Administration”.
    # This attribute defaults to label.title().
    verbose_name = 'Human-First AI: Data Management'
