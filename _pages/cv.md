---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-section {
  margin-bottom: 3em;
}

.cv-section h2 {
  font-size: 1.4em;
  font-weight: 600;
  color: #333;
  margin-bottom: 1.5em;
  letter-spacing: 0.5px;
}

.cv-item {
  margin-bottom: 2em;
  padding-bottom: 1.5em;
  border-bottom: 1px solid #eee;
}

.cv-item:last-child {
  border-bottom: none;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.5em;
}

.item-title {
  font-weight: 600;
  font-size: 1.1em;
  color: #222;
  margin: 0;
}

.item-subtitle {
  color: #666;
  font-size: 0.95em;
  margin: 0.2em 0 0 0;
}

.item-date {
  color: #888;
  font-size: 0.9em;
  font-weight: 400;
  white-space: nowrap;
  margin-left: 1em;
}

.item-description {
  color: #555;
  line-height: 1.5;
  margin-top: 0.8em;
}

.skills-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2em;
}

.skill-group {
  flex: 1;
  min-width: 200px;
}

.skill-group h4 {
  font-size: 1em;
  font-weight: 600;
  color: #333;
  margin: 0 0 0.8em 0;
}

.skill-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.skill-list li {
  color: #555;
  margin-bottom: 0.3em;
  font-size: 0.95em;
}

@media (max-width: 768px) {
  .item-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .item-date {
    margin-left: 0;
    margin-top: 0.3em;
  }
  
  .skills-container {
    flex-direction: column;
    gap: 1.5em;
  }
}
</style>

<div class="cv-section">
  <h2>Education</h2>
  
  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">Ph.D in Version Control Theory</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">2018 (expected)</div>
    </div>
    <div class="item-description">
      Focus on distributed version control systems and collaborative software development methodologies.
    </div>
  </div>

  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">M.S. in Jekyll</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">2014</div>
    </div>
    <div class="item-description">
      Specialized in static site generation and modern web development frameworks.
    </div>
  </div>

  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">B.S. in GitHub</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">2012</div>
    </div>
    <div class="item-description">
      Foundation in software development, version control, and open source collaboration.
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Work Experience</h2>
  
  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">Academic Pages Collaborator</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">Spring 2024</div>
    </div>
    <div class="item-description">
      Updates and improvements to template. Supervisor: The Users.
    </div>
  </div>

  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">Research Assistant</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">Fall 2015</div>
    </div>
    <div class="item-description">
      Merging pull requests. Supervisor: Professor Hub.
    </div>
  </div>

  <div class="cv-item">
    <div class="item-header">
      <div>
        <div class="item-title">Research Assistant</div>
        <div class="item-subtitle">GitHub University</div>
      </div>
      <div class="item-date">Summer 2015</div>
    </div>
    <div class="item-description">
      Tagging issues. Supervisor: Professor Git.
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Skills</h2>
  
  <div class="skills-container">
    <div class="skill-group">
      <h4>Technical</h4>
      <ul class="skill-list">
        <li>Programming Languages</li>
        <li>Data Analysis</li>
        <li>Statistical Software</li>
        <li>Version Control</li>
      </ul>
    </div>
    
    <div class="skill-group">
      <h4>Research</h4>
      <ul class="skill-list">
        <li>Experimental Design</li>
        <li>Data Collection</li>
        <li>Academic Writing</li>
        <li>Literature Review</li>
      </ul>
    </div>
    
    <div class="skill-group">
      <h4>Leadership</h4>
      <ul class="skill-list">
        <li>Project Management</li>
        <li>Team Collaboration</li>
        <li>Presentation Skills</li>
        <li>Critical Thinking</li>
      </ul>
    </div>
  </div>
</div>

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
