from app.app import create_app

def test_client(client):
    """
    Test that docker is running

    Args:
    """
    response = client.get("/")
    print(response.status_code)
    assert response.status_code == 200