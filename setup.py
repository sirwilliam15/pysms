from setuptools import setup

setup(
    name='pysmsapi',
    version='0.1.0',    
    description='API Interface for SMS Backends',
    url='https://github.com/sirwilliam15/pysmsapi',
    author='Will Nazaroff',
    author_email='willnaz15@protonmail.com',
    license='MIT',
    packages=['pysmsapi'],
    install_requires=['requests>=2.25.1'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
