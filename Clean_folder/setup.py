from setuptools import setup, find_namespace_packages

setup(
    name='Clean_folder',
    version='0.0.1',
    description='Sorting of folder',
    url='https://github.com/TetianaShevch/GoIT_Home_task_7.git',
    author='Tetiana Shevchenko',
    author_email='Shevch_Tatyana@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
    )