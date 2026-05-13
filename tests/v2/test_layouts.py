from fastapi import status


def test_get_layouts_success(client, auth_headers):
    response = client.get(
        "/api/v2/layouts",
        headers=auth_headers
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["status_code"] == 200
    assert body["message"] == "Layouts retrieved successfully"

    data = body["data"]

    assert isinstance(data, dict)

    assert "page" in data
    assert "limit" in data
    assert "total" in data
    assert "layouts" in data

    assert data["limit"] == 10
    assert isinstance(data["layouts"], list)

    if data["layouts"]:
        layout = data["layouts"][0]

        assert "layout_id" in layout
        assert "name" in layout
        assert "description" in layout
        assert "thumbnail_url" in layout