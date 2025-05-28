pytest==8.3.5
requests==2.32.3
Faker==30.8.0
pytest-reporter-html1==0.9.2
pytest_steps==1.8.0
python-dotenv==1.0.1


pip install -r requirements.txt


from faker import Faker
fake = Faker()


pytest --template=html1/index.html --report=report.html



https://circleci.com/

version: 2.1

jobs:
  python-job:
    docker:
      - image: circleci/python:3.10.1-node-browsers
    steps:
      - checkout
      - run:
          name: set up venv
          command: |
            python -m venv venv
            . venv/bin/activate
      - run:
          name: install dependencies
          command: |
            . venv/bin/activate
            pip install -r requirements.txt
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            pytest --template=html1/index.html --report=report.html
      - store_artifacts:
          path: report.html
          destination: python-report

workflows:
  build-and-test:
    jobs:
      - python-job


.circleci

config.yml