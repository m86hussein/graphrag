# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

import pytest
from graphrag.query.llm.text_utils import try_parse_json_object
from graphrag.query.structured_search.global_search.search import GlobalSearch


@pytest.mark.parametrize(
    "response",
    [
        '[{"description": "Example", "score": 1}]',
        '"Example"',
        "5",
        "true",
        "```json\n[1, 2]\n```",
    ],
)
def test_try_parse_json_object_returns_empty_dict_for_non_object_json(response):
    _, result = try_parse_json_object(response, verbose=False)

    assert result == {}


def test_global_search_parse_response_falls_back_for_json_array():
    search = GlobalSearch.__new__(GlobalSearch)

    assert search._parse_search_response(  # noqa: SLF001
        '[{"description": "Example", "score": 1}]'
    ) == [{"answer": "", "score": 0}]
