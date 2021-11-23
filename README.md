- Assignment was completed individually in T3 2021 for COMP3311: Database Systems.
- Task was to write three scripts (trans, rules, check) that return student enrolment data.
- This project had a focus on querying a databse using a Python script.
- Project Spec can be found in spec.html with accompanying files in the other *.html files.
- To run application:
    - PostgreSQL must be installed and running
    - To load files:
      ```
      $ createdb mymyunsw
      $ psql mymyunsw -f mymyunsw.dump > log 2>&1
      ```
    - Run python scripts as seen in spec
