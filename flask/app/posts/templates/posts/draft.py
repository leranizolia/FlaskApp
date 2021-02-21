{% extends 'base.html' %}

{% block title %}
    Blueprint index page
{% endblock %} | Flask app


{% block content_title %}
    Posts
{% endblock %}


{% block content %}

    {% for post in pages.items %}

        <p>
            <a href="{{ url_for('posts.post_detail', slug=post.slug) }}">{{post.title}}</a>
        </p>

    {% endfor %}

    <nav>
        <ul class="pagination">
             {% if not pages.has_prev %}
            <li><a>&laquo;</a></li>
             {% else %}
                <li>
                    <a href="./?page={{ pages.prev_num }}" aria-disabled="true">&laquo;</a>
                </li>
            {% endif %}

            {% for page  in pages.iter_pages() %}

                {% if page == pages.page %}
                    <li><a href="./?page={{ page }}"  style="background-color: grey">{{ page }}</a> </li>
                {% else %}

                <li>
                    <a href="./?page={{ pages.prev_num }}"> {{ page }} <span class="sr-only">(current)</span></a>
                </li>

                {% endif %}


            {% endfor %}

            {% if not pages.has_next %}
            <li><a>&raquo;</a></li>
             {% else %}
                <li>
                    <a href="./?page={{ pages.next_num }}" aria-disabled="true">&raquo;</a>
                </li>
            {% endif %}


        </ul>
    </nav>


{% endblock %}

@posts.route('/<slug>/edit', methods=['POST', 'GET'])
def edit_post(slug):
    post = Post.query.filter(Post.slug==slug).first()
    if