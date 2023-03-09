from setuptools import setup

setup(
    name='fddbenchmark',
    version='0.0.1',    
    description='Benchmarking fault detection and diagnosis methods',
    url='https://github.com/airi-industrial-ai/fddbenchmark',
    author='Vitaliy Pozdnyakov',
    author_email='pozdnyakov@airi.net',
    license='MIT License',
    packages=['fddbenchmark'],
    install_requires=[
        'numpy>=1.22', 
        'pandas>=1.3', 
        'scikit-learn>=1.2',
        'tqdm>=4.65',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)