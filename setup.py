from setuptools import setup, find_packages

setup(
    name='aiogram-broadcaster',
    version='0.0.7',
    author='getvalet',
    author_email='ваша_почта@example.com',
    description='Сохраненная версия пакета',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/getvalet/aiogram-broadcaster-0.0.7',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        # Сюда можно добавить зависимости, если они есть
    ],
)

