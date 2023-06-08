from setuptools import setup

setup(
    # Metadata
    name='bischoff_and_ratcliff_1995',
    version='0.0.0',
    url='https://github.com/lucasguesserts/bischoff-and-ratcliff-1995',
    author='Lucas Guesser',
    author_email='lucasguesserts@gmail.com',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
	keywords=[
        'container loading problem',
        'knapsack problem',
        'single large object placement problem (slopp)',
        'packing problem'
    ],
    # Options
    install_requires=[
        'pytest',
        'pandas'
    ],
    python_requires='>=3.0',
)
