---
layout: page
title: Photography
permalink: /photography/
---


<div class="posts">
  {% assign sorted_posts = site.posts | sort:"number" | reverse %}
  {% for post in sorted_posts %}  
  {% if post.tags contains 'photography' %}
    <article class="post">

      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="entry">
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.excerpt }}</a>
      </div>

      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
      {% if post.tags %}
      <a href="/photography" class="read-more">{{ post.tags }}</a>
      {% endif %}
    </article>
  {% endif %}
  {% endfor %}

</div>
