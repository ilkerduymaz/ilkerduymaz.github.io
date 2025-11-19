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
/* LaTeX-inspired Academic CV Styling - Theme Compatible */
body {
  line-height: 1.4;
}

.cv-container {
  max-width: 11in;
  margin: 0 auto;
  padding: 0 1in 1in 1in;
  background: var(--global-bg-color);
  font-size: 13pt;
  color: var(--global-text-color);
  font-family: "IBM Plex Sans", Georgia, "Times New Roman", Times, serif;
}

.cv-section {
  margin-bottom: 1.5em;
}

.cv-section h2 {
  font-size: 16pt;
  font-weight: 400;
  color: var(--global-text-color);
  margin: 1.2em 0 0.8em 0;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-bottom: 1px solid var(--global-text-color);
  padding-bottom: 2pt;
}

.cv-section:first-child h2 {
  margin-top: 0;
}

.cv-entry {
  margin-bottom: 1em;
  display: flex;
  align-items: flex-start;
  page-break-inside: avoid;
}

.cv-date {
  font-weight: 400;
  width: 100pt;
  flex-shrink: 0;
  text-align: right;
  padding-left: 15pt;
  order: 2;
  font-size: 12pt;
}

.cv-content {
  flex-grow: 1;
  line-height: 1.3;
  order: 1;
  padding-right: 15pt;
}

.cv-title {
  font-weight: 400;
  font-size: 15pt;
  margin-bottom: 2pt;
}

.cv-institution {
  font-style: italic;
  margin-bottom: 3pt;
}

.cv-description {
  font-size: 12pt;
  line-height: 1.3;
  margin-top: 3pt;
  text-align: justify;
}

.skills-section {
  display: block;
}

.skill-category {
  margin-bottom: 0.8em;
}

.skill-category-title {
  font-weight: 400;
  font-size: 13pt;
  margin-bottom: 4pt;
  display: inline-block;
  width: 120pt;
  vertical-align: top;
}

.skill-items {
  display: inline-block;
  width: calc(100% - 130pt);
  font-size: 12pt;
  line-height: 1.3;
}

/* LaTeX-style lists */
.latex-list {
  margin: 0;
  padding-left: 12pt;
  list-style-type: none;
}

.latex-list li {
  margin-bottom: 3pt;
  text-indent: -12pt;
  padding-left: 12pt;
}

.latex-list li:before {
  content: "• ";
  font-weight: 400;
}

/* Print-friendly styles */
@media print {
  .cv-container {
    max-width: none;
    padding: 0.5in;
    margin: 0;
    box-shadow: none;
    background: white !important;
    color: black !important;
  }
  
  .cv-section h2 {
    color: black !important;
    border-bottom-color: black !important;
  }
  
  .cv-section {
    break-inside: avoid;
  }
  
  .cv-entry {
    break-inside: avoid;
  }
}

@media (max-width: 768px) {
  .cv-container {
    padding: 20pt;
  }
  
  .cv-entry {
    flex-direction: column;
  }
  
  .cv-date {
    width: auto;
    margin-bottom: 5pt;
    padding-left: 0;
    text-align: left;
    order: 0;
  }
  
  .cv-content {
    padding-right: 0;
    order: 1;
  }
  
  .skill-category-title {
    width: 100%;
    display: block;
    margin-bottom: 5pt;
  }
  
  .skill-items {
    width: 100%;
    display: block;
  }
}
</style>

<div class="cv-container">

<div class="cv-section">
  <h2>Education</h2>
  
  <div class="cv-entry">
    <div class="cv-date">Fall 2023<br/>Current</div>
    <div class="cv-content">
      <div class="cv-title">PhD in Psychology</div>
      <div class="cv-institution">Justus-Liebig University Giessen, Giessen, Germany</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2020<br/>Summer 2023</div>
    <div class="cv-content">
      <div class="cv-title">MSc in Psychology</div>
      <div class="cv-institution">Sabanci University, Istanbul, Turkey</div>
      <div class="cv-description">Thesis Title: Integration and Segregation Processes in Motion Perception</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2014<br/>Fall 2019</div>
    <div class="cv-content">
      <div class="cv-title">BA in Psychology</div>
      <div class="cv-institution">Bilkent University, Ankara, Turkey</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Research Interests</h2>
  <div class="cv-description">
    Temporal processing, neural oscillations, neural representations of dynamic visual stimuli, motion perception
  </div>
</div>

<div class="cv-section">
  <h2>Research Experience</h2>
  
  <div class="cv-entry">
    <div class="cv-date">Fall 2023<br/>Current</div>
    <div class="cv-content">
      <div class="cv-title">Graduate Student</div>
      <div class="cv-institution">Kaiser Lab (Dr. Daniel Kaiser)</div>
      <div class="cv-description">
        <ul class="latex-list">
          <li>Characterize neural representations of dynamic categorical changes in visual stimuli, demonstrating distinct temporal dynamics for abrupt versus gradual visual onsets and underscoring the importance of ecologically valid stimuli.</li>
          <li>Lead independent projects and contribute to collaborative work on individual differences in predictive processing, establishing freehand drawings as a novel proxy for assessing internal models of the visual world.</li>
          <li>Supervise a student research project on perceived speed of naturalistic visual stimuli, identifying stable individual differences in the perception of natural speed.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2020<br/>Summer 2023</div>
    <div class="cv-content">
      <div class="cv-title">Graduate Student</div>
      <div class="cv-institution">Alp Visual Neuroscience Lab (Dr. Nihan Alp)</div>
      <div class="cv-description">
        <ul class="latex-list">
          <li>Developed computational models to predict EEG responses to dynamic visual stimuli, executed empirical experiments to test model predictions, and engineered a custom SSVEP analysis pipeline.</li>
          <li>Conceptualized and led multiple independent lines of research investigating integration and segregation processes in motion perception, leveraging 64-channel EEG and psychophysics, culminating in a Master's thesis and two manuscripts.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2016<br/>Fall 2019</div>
    <div class="cv-content">
      <div class="cv-title">Research Assistant</div>
      <div class="cv-institution">Visual Perception & Attention Lab (Dr. Jen Corbett & Dr. Jaap Munneke)</div>
      <div class="cv-description">
        <ul class="latex-list">
          <li>Led data collection and statistical analyses on a study investigating how reward- and value-related factors influence perceptual averaging performance.</li>
          <li>Co-authored a peer-reviewed journal article, contributing directly to theoretical development, experimental refinement, and data interpretation.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Skills</h2>
  
  <div class="skills-section">
    <div class="skill-category">
      <span class="skill-category-title">Methodology:</span>
      <span class="skill-items">EEG, Psychophysics, SSVEP, MVPA, RSA</span>
    </div>
    
    <div class="skill-category">
      <span class="skill-category-title">Programming:</span>
      <span class="skill-items">Python, MATLAB, Julia, Git, Bash</span>
    </div>
    
    <div class="skill-category">
      <span class="skill-category-title">Toolboxes & Software:</span>
      <span class="skill-items">MNE-Python, FieldTrip, CoSMoMVPA, PsychoPy</span>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Publications</h2>
  <ul class="latex-list">{% for post in site.publications reversed %}
    {% if post.category != 'conferences' %}
      {% include archive-single-cv.html %}
    {% endif %}
  {% endfor %}</ul>
</div>

<div class="cv-section">
  <h2>Conference Presentations & Abstracts</h2>
  <ul class="latex-list">
    {% for post in site.publications reversed %}
      {% if post.category == 'conferences' %}
        {% include archive-single-cv.html %}
      {% endif %}
    {% endfor %}
  </ul>
</div>

<div class="cv-section">
  <h2>Internship & Workshops</h2>
  
  <div class="cv-entry">
    <div class="cv-date">June 2025</div>
    <div class="cv-content">
      <div class="cv-title">Closing the Loop: The Role of Feedback in Neural Processing and Perception</div>
      <div class="cv-institution">3-day workshop on neural oscillations and recurrent processing, Lausanne, Switzerland</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">June 2024</div>
    <div class="cv-content">
      <div class="cv-title">Categorization in Perception and Action: Minds, Models, Mechanisms</div>
      <div class="cv-institution">3-day workshop on categorization in perception and action, Marburg, Germany</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">July 2021</div>
    <div class="cv-content">
      <div class="cv-title">NeuroMatch Academy - Computational Neuroscience</div>
      <div class="cv-institution">Summer school for computational neuroscience, Online</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Summer 2017</div>
    <div class="cv-content">
      <div class="cv-title">Internship at Aysel Sabuncu Brain Research Center</div>
      <div class="cv-institution">Interned as a research assistant working on perceptual averaging, Ankara, Turkey</div>
    </div>
  </div>
</div>

<div class="cv-section">
  <h2>Teaching Experience</h2>
  
  <div class="cv-entry">
    <div class="cv-date">Fall 2024<br/>Spring 2025</div>
    <div class="cv-content">
      <div class="cv-title">Co-supervisor</div>
      <div class="cv-institution">Bachelor's Thesis, Justus-Liebig University Giessen</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2020<br/>Spring 2023</div>
    <div class="cv-content">
      <div class="cv-title">Teaching Assistant</div>
      <div class="cv-institution">PSY 350 - Introduction to Neuroscience<br/>PSY 312 - Sensation & Perception, Sabanci University</div>
    </div>
  </div>

  <div class="cv-entry">
    <div class="cv-date">Fall 2016</div>
    <div class="cv-content">
      <div class="cv-title">Teaching Assistant</div>
      <div class="cv-institution">CS 123 - Introduction to Computing and Programming for Social Sciences, Bilkent University</div>
    </div>
  </div>
</div>

</div><!-- End cv-container -->
