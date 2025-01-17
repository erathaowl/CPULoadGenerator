from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cpu-load-generator',
      version='1.2.1',
      description='CPU load generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/erathaowl/CPULoadGenerator',
      author='Erathaowl',
      author_email='erathaowl@gmail.com',
      license='MIT',
      classifiers=[
              "License :: OSI Approved :: MIT License",
              "Programming Language :: Python :: 3",
          ],
      packages=find_packages(),
      include_package_data=True,
      install_requires=['psutil']
      )
