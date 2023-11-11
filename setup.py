from setuptools import setup

setup(
    name='dsss_homework_2',
    version='1.0',
    author='DanteAdami',
    description='DSSS homework2 - Development of a math game integrating unit tests',
    url='https://github.com/DanteAdami/dsss_homework_2',
    packages=['math-quiz'],
    scripts=[
        'math_quiz/math_quiz.py',
        'math_quiz/tests_math_quiz.py'
    ]
)
