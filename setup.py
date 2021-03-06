from setuptools import setup, find_packages
from setuptools.command.test import test


class Tox(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = ["-v", "-epy"]
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        tox.cmdline(self.test_args)

setup(
    name='boosh',
    version='0.1.0.dev1',
    packages=find_packages(),
    install_requires=[
        'botocore>=0.94.0',
    ],
    entry_points={
        'console_scripts': [
            'boosh_proxy = boosh.ssh:main',
        ],
    },
    tests_require=['tox'],
    cmdclass={'test': Tox},
    author='Paul Handly',
    author_email='ph@betaworks.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
