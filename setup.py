from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='il-supermarket-scraper',
    url='https://github.com/jladan/package_demo',
    author='Sefi Erlich',
    author_email='erlichsefi@gmail.com',
    # Needed to actually package something
    packages=['il-supermarket-scraper'],
    # Needed for dependencies
    install_requires=['retry==0.9.2',
                        "mock==4.0.3","requests==2.27.1","lxml==4.8.0","beautifulsoup4==4.10.0"],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)