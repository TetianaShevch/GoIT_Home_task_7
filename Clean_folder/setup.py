from setuptools import setup, find_namespace_packages

setup(
    name='Clean_folder',
    version='0.0.1',
    description='Soring of folder',
    # url:'http://github.com/dummy_user/useful',
    author='Tetiana Shevchenko',
    author_email='Shevch_Tatyana@gmail.com'
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
    )