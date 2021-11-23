# COMP3311 21T3 Ass2 ... Python helper functions
# add here any functions to share between Python scripts 
# you must submit this even if you add nothing

# Example output for 3707:
#   id  | code |              name              | uoc | offeredby | career | duration | description 
# ------+------+--------------------------------+-----+-----------+--------+----------+-------------
#  3707 | 3707 | Bachelor of Engineering (Hons) | 192 |       112 | UG     |       48 | 
def getProgram(db,code):
  cur = db.cursor()
  cur.execute("select * from Programs where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

# Example for COMPAS:
#  id |  code  |          name           | offeredby | stype | description 
# ----+--------+-------------------------+-----------+-------+-------------
#   2 | COMPAS | Artificial Intelligence |        89 |     4 | 
def getStream(db,code):
  cur = db.cursor()
  cur.execute("select * from Streams where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

# Example for student 5123523:
#    id    |   family    | given |     fullname      |  birthday  | origin |  name  
# ---------+-------------+-------+-------------------+------------+--------+--------
#  5123523 | Nava Garcia | Cindy | Cindy Nava Garcia | 1985-05-14 |    136 | Mexico
def getStudent(db,zid):
  cur = db.cursor()
  qry = """
  select p.*, c.name
  from   People p
         join Students s on s.id = p.id
         join Countries c on p.origin = c.id
  where  p.id = %s
  """
  cur.execute(qry,[zid])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

# Returns info of OrgUnit given id
def getOrgUnit(db,id):
  cur = db.cursor()
  cur.execute("select * from orgunits where id = %s",[id])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

# Returns list of program_rules with info for given program
# Example for 3707:
#     0        1         2         3                   4       5         6           7         8             9          10                  11        12            13
#  program |  rule  |   id   |        name         | type | min_req | max_req | ao_group | description |   id   |        name         |  type   |   defby    |                                                              definition                                                              
# ---------+--------+--------+---------------------+------+---------+---------+----------+-------------+--------+---------------------+---------+------------+--------------------------------------------------------------------------------------------------------------------------------------
#     3707 | 352648 | 352648 | BE(Hons) Streams    | DS   |       1 |       1 |   685942 |             | 685942 | BE(Hons) Streams    | stream  | enumerated | AEROAH,BINFAH,CEICAH,CEICDH,COMPBH,CVENAH,CVENBH,ELECAH,ELECCH,GMATDH,MANFBH,MECHAH,MINEAH,MTRNAH,PETRAH,SENGAH,SOLAAH,SOLABH,TELEAH
#     3707 | 352649 | 352649 | Industrial Training | CC   |         |         |   685943 |             | 685943 | Industrial Training | subject | enumerated | ENGG4999
#     3707 | 352650 | 352650 | General Education   | GE   |      12 |      12 |   685944 |             | 685944 | General Education   | subject | pattern    | GEN#####
def getProgRules(db,code):
  cur = db.cursor()
  qry = """
    select *
    from   program_rules p
           join rules r on r.id = p.rule
           join academic_object_groups a on r.ao_group = a.id
    where  p.program = %s
    """
  cur.execute(qry,[code])
  infos = cur.fetchall()
  cur.close()
  if infos == []:
    return None
  else:
    return infos

# Returns list of program_rules with info for given program and rule type
# Output same as above
def getTypedProgRules(db, code, type):
  cur = db.cursor()
  qry = """
    select *
    from   program_rules p
           join rules r on r.id = p.rule
           join academic_object_groups a on r.ao_group = a.id
    where  p.program = %s and r.type = %s
    """
  cur.execute(qry,[code, type])
  infos = cur.fetchall()
  cur.close()
  if infos == []:
    return None
  else:
    return infos

# Returns list of rules with info for given stream
# Example output for stream 2 COMPAS:
#   0         1       2                     3                   4       5         6         7           8           9                   10                    11          12                          13
#  stream |  rule  |   id   |             name              | type | min_req | max_req | ao_group | description |   id   |             name              |  type   |   defby    |                                    definition                                    
# --------+--------+--------+-------------------------------+------+---------+---------+----------+-------------+--------+-------------------------------+---------+------------+----------------------------------------------------------------------------------
#       2 | 352667 | 352667 | COMPAS Core                   | CC   |         |         |   685961 |             | 685961 | COMPAS Core                   | subject | enumerated | {COMP9414;COMP9814}
#       2 | 352668 | 352668 | COMPAS Electives              | PE   |      18 |      18 |   685962 |             | 685962 | COMPAS Electives              | subject | enumerated | COMP4418,COMP9318,COMP9417,COMP9418,COMP9434,COMP9444,COMP9491,COMP9517,MATH5836
#       2 | 352669 | 352669 | COMPAS Disciplinary Electives | PE   |         |       6 |   685963 |             | 685963 | COMPAS Disciplinary Electives | subject | pattern    | BINF6###,BINF9###,COMP4###,COMP6###,COMP9##,GSOE92###
def getStreamRules(db,id):
  cur = db.cursor()
  qry = """
    select *
    from   stream_rules s
           join rules r on r.id = s.rule
           join academic_object_groups a on r.ao_group = a.id
    where  s.stream = %s
    """
  cur.execute(qry,[id])
  infos = cur.fetchall()
  cur.close()
  if infos == []:
    return None
  else:
    return infos

# Returns list of stream_rules with info for given stream and rule type
# Used in Prog
# Example output:
#   0         1       2      3              4                 5         6       7             8               9                         10      11      12          13          14            15      16                                  17      18            19          
#  stream |  rule  | id |  code  |         name         | offeredby | stype | description |   id   |              name              | type | min_req | max_req | ao_group | description |   id   |              name              |  type   |   defby    |                                    definition                                    
# --------+--------+----+--------+----------------------+-----------+-------+-------------+--------+--------------------------------+------+---------+---------+----------+-------------+--------+--------------------------------+---------+------------+----------------------------------------------------------------------------------
#       3 | 352670 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352670 | Foundational Computing         | CC   |         |         |   685964 |             | 685964 | Foundational Computing         | subject | enumerated | COMP1511,COMP1521,COMP1531,COMP2511,COMP2521
#       3 | 352671 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352671 | COMPBH Maths                   | CC   |         |         |   685965 |             | 685965 | COMPBH Maths                   | subject | enumerated | {MATH1131;MATH1141},{MATH1231;MATH1241},MATH2069,MATH2099
#       3 | 352672 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352672 | COMPBH Physics and Electronics | CC   |         |         |   685966 |             | 685966 | COMPBH Physics and Electronics | subject | enumerated | {PHYS1121;PHYS1131},{PHYS1221;PHYS1231},ELEC1111,ELEC2133,ELEC2134
#       3 | 352673 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352673 | COMPBH Design                  | CC   |         |         |   685967 |             | 685967 | COMPBH Design                  | subject | enumerated | {ENGG1000;DESN1000},DESN2000
#       3 | 352674 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352674 | COMPBH Advanced Core           | CC   |         |         |   685968 |             | 685968 | COMPBH Advanced Core           | subject | enumerated | COMP3211,COMP3222,COMP3231,COMP3601,COMP4601,COMP4920,COMP4951,COMP4952,COMP4953
#       3 | 352675 |  3 | COMPBH | Computer Engineering |        89 |     1 |             | 352675 | COMPBH Computing Electives     | PE   |      36 |         |   685969 |             | 685969 | COMPBH Computing Electives     | subject | pattern    | ENGG2600,ENGG3060,ENGG3600,ENGG4600,COMP3###,COMP4###,COMP6###,COMP9###
def getStreamRulesByCode(db, code, type):
  cur = db.cursor()
  qry = """
    select *
    from   stream_rules s
           join streams s1 on s.stream = s1.id
           join rules r on r.id = s.rule
           join academic_object_groups a on r.ao_group = a.id
    where  s1.code = %s and r.type = %s
    """
  cur.execute(qry,[code, type])
  infos = cur.fetchall()
  cur.close()
  if infos == []:
    return None
  else:
    return infos

def getSubjectName(db, code):
  cur = db.cursor()
  cur.execute("select name from subjects where code = %s", [code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return "???"
  else:
    return info[0]

# Gets transcript data for given student ordered by term then course code
# Example output for zId: 5124159
#     0         1                   2                   3       4     5
#    code   | term |              name              | mark | grade | uoc 
# ----------+------+--------------------------------+------+-------+-----
#  COMP9318 | 17s1 | Data Warehousing & Data Mining |   65 | CR    |   6
#  COMP9319 | 17s1 | Web Data Compression & Search  |   86 | HD    |   6
#  COMP9417 | 17s1 | Machine Learning & Data Mining |   78 | DN    |   6
#  COMP6714 | 17s2 | Info Retrieval and Web Search  |   69 | CR    |   6
#  COMP9313 | 17s2 | Big Data Management            |   77 | DN    |   6
#  COMP9444 | 17s2 | Neural Networks, Deep Learning |   88 | HD    |   6
def getCourseMarks(db, zId):
  cur = db.cursor()
  qry = """
    select s.code, t.code as term, s.name, e.mark, e.grade, s.uoc
    from   course_enrolments e
           join courses c on c.id = e.course
           join terms t on t.id = c.term
           join subjects s on s.id = c.subject
    where  e.student = %s
    order by t.starting, s.code
    """
  cur.execute(qry,[zId])
  infos = cur.fetchall()
  cur.close()
  if infos == []:
    return None
  else:
    return infos

def getRecentProgStream(db, zId):
  cur = db.cursor()
  qry = """
    select p.program, s.code
    from   program_enrolments p
           join stream_enrolments e on e.partof = p.id
           join streams s on s.id = e.stream
    where  p.student = %s
    order by p.term desc
    """
  cur.execute(qry,[zId])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info