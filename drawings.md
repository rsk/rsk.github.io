---
layout: page
title: Drawings
permalink: /drawings/
---


<div class="posts">
  {% assign sorted_posts = site.posts | sort:"number" | reverse %}
  {% for post in sorted_posts %}
  {% if post.tags contains 'drawings' %}
    <article class="post">
      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="entry">
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.excerpt }}</a>
      </div>
      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
      {% if post.tags %}
          {% for tag in post.tags %}
              <a href="/{{ tag }}" class="read-more">{{ tag }}</a>
          {% endfor %}
      {% endif %}
    </article>
  {% endif %}
  {% endfor %}
</div>
