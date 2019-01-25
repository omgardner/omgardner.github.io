---
layout: post
title: Song Repetition Visualised
categories: [visualisation, python, seaborn, music]
tags: [visualisation, python, seaborn, music]
permalink: /song-repetition/
excerpt_separator: <!--more-->
---
<blockquote class="reddit-card" data-card-created="1548392069">
	<a href="https://old.reddit.com/r/dataisbeautiful/comments/ac1uxg/repetition_pattern_of_lyrics_in_a_beatles_song_oc/?ref=share&ref_source=embed">Repetition pattern of lyrics in a Beatles song. [OC]</a> from <a href="http://www.reddit.com/r/dataisbeautiful">r/dataisbeautiful</a>
</blockquote>
<script async src="//embed.redditmedia.com/widgets/platform.js" charset="UTF-8"></script>


I decided to recreate an interesting visual for song repetition by Colin Morris. The visual can be seen in [this vox video](https://www.youtube.com/watch?v=HzzmqUoQobc), and at his site: [SongSim](https://colinmorris.github.io/SongSim).
<!--more-->

## How to read the graph
The y-axis shows the lyrics as they occur, with the first lyric at the top. The lyrics are also occuring along the x-axis, but are not shown. At every point where a lyric occurs on the y-axis, you can look across the x-axis to see all occurances of that specific word.

The diagonal appears because both axes show the word in the same order. 

## Method of creation
The code for this visual can be found [here](https://github.com/omgardner/graphs/blob/master/graphs/repetition_patterns/code.py). 

The lyrics were sourced from [kaggle](https://www.kaggle.com/rakannimer/billboard-lyrics]), and have been word-tokenized. 

Then I iterated over the lyrics in two nested loops, comparing word_a to word_b. If equal, take the indexes for both words, and use them as coordinates for a scatterplot.

## Alternate visuals
After a comment about limiting the y-axis to unique words only as they occur, I made the following visualisation for *First Blood by Kavinsky*
![alt-visual](https://raw.githubusercontent.com/omgardner/graphs/master/graphs/repetition_patterns/First_Blood_BY_Kavinsky_alt.png)

## What I learned / Feedback

I made some updates based on reddit feedback:
- changed the colourmap to be diagonal instead of horizontal.

The way i flipped the y-axis was sub-optimal, instead of reversing the data, I could have instead done:
>ax.invert_yaxis()

I could have explored using plt.imshow instead of plt.scatter, but the scatterplot allows for changing shape of points.

I could [mask](https://seaborn.pydata.org/generated/seaborn.heatmap.html) the top half of the graph, as it duplicates information; reflected across *y = n-x* diagonal.
