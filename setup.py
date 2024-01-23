import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    description = f.read()
    
    
__version__ = "0.0.0"

REPOSITORY_NAME = "cancer-classifier"
AUTHOR_USER_NAME = "Jothammasila"
SRC_REPOSITORY = "cnnClassifier"
AUTHOE_EMAIL = "jothammasila@fmail.com"


setuptools.setup(
    name=SRC_REPOSITORY,
    version= __version__,
    author=AUTHOR_USER_NAME,
    description="Small pyhton package for cnn app",
    long_description=description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPOSITORY_NAME}",
    project_urls= {
        "Big Tracker": f"https//github.com/{AUTHOR_USER_NAME}/{REPOSITORY_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)