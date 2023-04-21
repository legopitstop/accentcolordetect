import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='accentcolordetect',
    version='0.0.1',
    author='Legopitstop',
    description='Detect OS accent color from Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/legopitstop/accentcolordetect/',
    packages=setuptools.find_packages(),
    license='MIT',
    keywords=['colordetect', 'tkinter', 'gui', 'windows', 'darwin'],
    author_email='officiallegopitstop@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6'
)