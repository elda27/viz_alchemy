from setuptools import setup
from pathlib import Path

# Get version from main script
__version__ = None

src_dir = Path(__file__).parent.absolute()
version_file = src_dir / 'viz_alchemy' / 'version.py'
with open(version_file, 'r') as fp:
    exec(fp.read())

fndoc = Path(src_dir) / 'README.md'
with open(fndoc, 'r') as fp:
    README = fp.read()

setup(
    name='viz_alchemy',
    version=__version__,
    description='Visualize database relationship for SQLAlchemy',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT Licences',
    url='https://github.com/elda27/viz_alchemy',
    maintainer='elda27',
    # maintainer_email=None,
    platforms=['any'],
    install_requires=[
        "sqlalchemy",
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage'
        ],
    },
    packages=[
        "viz_alchemy"
    ],
    entry_points={
        'console_scripts': [
            "viz_alchemy = viz_alchemy.main:main"
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        # (https://pypi.org/pypi?%3Aaction=list_classifiers)
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    # keywords=None,
)
