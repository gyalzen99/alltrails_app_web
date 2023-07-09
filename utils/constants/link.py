def set_redirect_link(page_name):
    return "{% url " + page_name + "%}?data_id="