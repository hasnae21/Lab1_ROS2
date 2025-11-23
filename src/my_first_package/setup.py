from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hasnae',
    maintainer_email='hasnae@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = my_first_package.simple_publisher:main',
            'subscriber = my_first_package.simple_subscriber:main',
            'number_publisher = my_first_package.number_publisher:main',
            'number_subscriber = my_first_package.number_subscriber:main',
            'turtle_square = my_first_package.turtle_square:main',
            'ping_node = my_first_package.ping_node:main',
            'pong_node = my_first_package.pong_node:main',
        ],
    },
)
