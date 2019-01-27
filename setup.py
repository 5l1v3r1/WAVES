from setuptools import setup

setup(
    name='WAVES',
    version='1.0.0',
    packages=['bin', 'WAVESCore', 'WAVESCore.net', 'WAVESCore.net.jsparser', 'WAVESCore.file', 'WAVESCore.attack',
              'WAVESCore.config', 'WAVESCore.config.attacks', 'WAVESCore.config.reports',
              'WAVESCore.config.vulnerabilities', 'WAVESCore.report', 'WAVESCore.language'],
    url='http://github.com',
    license='',
    author='Babajee Gubbala, Aviral Agarwal, Nitin Sharma',
    author_email='gzbjdq123@gmail.com',
    description='Web Application Vulnerability Scanner'
)
