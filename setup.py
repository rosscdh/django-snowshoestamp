from setuptools import setup

setup(
    name="django-snowshoestamp",
    packages=['snowshoestamp'],
    version='0.1.0',
    author="Ross Crawford-d'Heureuse",
    license="MIT",
    author_email="ross@lawpal.com",
    url="https://github.com/rosscdh/django-snowshoestamp",
    description="A Django app for integrating with snowshoestamp",
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'sssapi',
        'requests_oauthlib',
        'django-braces',
    ]
)
