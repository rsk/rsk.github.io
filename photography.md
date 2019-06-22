---
layout: page
title: Photography
permalink: /photography/
---


<div class="posts">

  {% for post in site.posts %}
  {% if post.tags contains 'photography' %}
    <article class="post">

      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="entry">
        {{ post.excerpt }}
      </div>

      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
      {% if post.tags %}
      <a href="/photography" class="read-more">{{ post.tags }}</a>
      {% endif %}
    </article>
  {% endif %}
  {% endfor %}

</div>
