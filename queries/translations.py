def q1() -> str:
    return "MATCH (b:Book) RETURN b.id AS book, b.title AS title"


def q2() -> str:
    return "MATCH (b:Book) WHERE b.year > 2010 RETURN b.id AS book, b.year AS year"


def q3() -> str:
    return """
    MATCH (b:Book)-[:AUTHORED_BY]->(a:Author)
    RETURN b.id AS book, a.name AS author_name
    """


def q4() -> str:
    # Using the topic property as canonical source (aligns with SPARQL :topic predicate)
    return """
    MATCH (b:Book)
    OPTIONAL MATCH (b)-[:ON_TOPIC]->(t:Topic)
    RETURN b.id AS book, t.name AS topic
    """


def q5() -> str:
    return """
    RETURN EXISTS {
        MATCH (b:Book)-[:AUTHORED_BY]->(a1:Author),
              (b)-[:AUTHORED_BY]->(a2:Author)
        WHERE a1 <> a2
    } AS result
    """