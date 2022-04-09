from setuptools import setup

package_name = 'echo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yusuke Muramatsu',
    maintainer_email='yukke42@users.noreply.github.com',
    description='The echo package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f"echo = {package_name}:main",
        ],
    },
)
