from setuptools import find_packages, setup

from conexp import __version__

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='conexp-to-python',
      version=__version__,
      description='Simple convertor from .cex files into python dicts.',
      keywords='fca formal concept analysis conexp cex',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='https://github.com/mikulatomas/conexp-to-python',
      author='Tomas Mikula',
      author_email='mail@tomasmikula.cz',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.4',
      install_requires=['xmltodict'],
      tests_require=[],
      zip_safe=False,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
      ],)
