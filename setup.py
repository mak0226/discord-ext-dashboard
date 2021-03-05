from setuptools import setup
import re

version = ""
with open("discord/ext/dashboard/__init__.py") as f:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError("version is not set")
		

readme = ""
with open('README.md') as f:
	readme = f.read()
	

requirements = ["discord.py>=1.5.1"]

setup(name='discord-ext-dashboard',
      author='Penguin Master',
      url='https://github.com/PenguinMaster0226/discord-ext-dashboard',
      version=version,
      packages=['discord.ext.dashboard'],
      license='MIT',
      description='A webhook and request based discord.py extension for making a bot dashboard.',
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires='>=3.5.3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
