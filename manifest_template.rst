Manifest
========

This document is an auto-generated summary of the studies available. The title
of each section corresponds to the directory within this repo.


{% for study in studies %}
``{{ study.dirname }}``
{{ study.underline }}
{{ study.study.description }}

:genome: {{ study.genomes }}

Tracks
------
{% for track in study.tracks %}
* {{ track.label }}{% if track.description %}: {%endif%}{{ track.description }}
{% endfor %}
{% endfor %}
