from app import app as dash_app

def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    # Wait until the header with id="header" appears
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales Dashboard"

def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    # Wait until the div with id="visualization" appears
    dash_duo.wait_for_element("#visualization", timeout=10)
    assert dash_duo.find_element("#visualization") is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    # Wait until the radio button with id="region_picker" appears
    dash_duo.wait_for_element("#region_picker", timeout=10)
    assert dash_duo.find_element("#region_picker") is not None
