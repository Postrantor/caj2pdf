from setuptools import setup

package_name = 'caj2pdf'

setup(
    name=package_name,
    version='0.1.2',
    packages=[package_name],
    include_package_data=True,
    package_data={
        package_name: ['lib/**/*']
    },
    install_requires=[
        'imagesize==1.3.0',
        'PyPDF2==2.2.0'
    ],
    zip_safe=True,
    maintainer='postrantor',
    maintainer_email='postrantor@gamil.com',
    description='AF RED configurator tools',
    license='MIT License',
    entry_points={
        'console_scripts': [
            'caj2pdf = {}.{}:convert_caj_to_pdf'.format(
                package_name, 'main'),
        ],
    },
)
