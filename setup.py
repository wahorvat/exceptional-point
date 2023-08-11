"""Install exceptional_point."""
import os
import sys

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install as InstallCommandBase
from setuptools.dist import Distribution

# To enable importing version.py directly, we add its path to sys.path.
version_path = os.path.join(
    os.path.dirname(__file__), 'tensorflow_probability', 'python')
sys.path.append(version_path)
from version import __version__  # pylint: disable=g-import-not-at-top

# Ditto for required_packages.py
sys.path.append(os.path.dirname(__file__))
from required_packages import REQUIRED_PACKAGES  # pylint: disable=g-import-not-at-top, g-bad-import-order

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
    name=project_name,
    version=__version__,
    description='exceptional point simulation '
                'pt symmetry breaking',
    long_description=long_description,
    long_description_content_type='text/markdown',',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=REQUIRED_PACKAGES,
    # Add in any packaged data.
    include_package_data=True,
    package_data={'': ['*.so']},
    exclude_package_data={'': ['BUILD', '*.h', '*.cc']},
    zip_safe=False,
    distclass=BinaryDistribution,
    cmdclass={
        'pip_pkg': InstallCommandBase,
    },
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='exceptional point simulation',
)
