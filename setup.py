import setuptools

setuptools.setup(
  include_package_data = True,
  name = 'TestOutput',
  version = '1.0.0',
  description = 'oss-dev output text ex',
  author = 'FarmingWon',
  auth_email = 'thsdnjst#@naver.com',
  url = 'https://github.com/FarmingWon/test_output/',
#   download_url = 'https://github.com/FarmingWon/test_output.git',
  install_requires = ['pytest'],
  long_description = 'oss-dev output text ex',
  long_description_content_type = 'text/markdown',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
)
