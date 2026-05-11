from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="disease-prediction",
    version="1.0.0",
    author="Suchismita Bangal",
    author_email="suchismitabangal05@gmail.com",
    description="A machine learning web application for predicting Diabetes, Heart Disease, and Kidney Disease",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Suchismita185/Disease_Prediction",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.40.0",
        "streamlit-option-menu>=0.3.13",
        "scikit-learn>=1.5.0",
        "pandas>=2.2.0",
        "numpy>=1.26.4",
    ],
)
