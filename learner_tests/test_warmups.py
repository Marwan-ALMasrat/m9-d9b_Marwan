"""Learner-written tests for queries/warmups.py."""

import pytest

from queries.warmups import q1_list_recipes, q2_filter_by_cuisine, q3_subclass_traversal


def test_q1_list_recipes_returns_all_five(driver):
    cypher = q1_list_recipes()
    with driver.session() as session:
        rows = [record["name"] for record in session.run(cypher)]
    assert len(rows) == 5


def test_q3_traversal_picks_up_subclasses(driver):
    cypher, params = q3_subclass_traversal("Chinese")
    with driver.session() as session:
        rows_q3 = [record["name"] for record in session.run(cypher, params)]

    cypher2, params2 = q2_filter_by_cuisine("Chinese")
    with driver.session() as session:
        rows_q2 = [record["name"] for record in session.run(cypher2, params2)]

    assert len(rows_q3) > len(rows_q2)