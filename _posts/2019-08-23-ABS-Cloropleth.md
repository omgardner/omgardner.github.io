---
layout: post
title: Visualising ABS Housing Income by Suburb
categories: [visualisation, GIS]
tags: [python, QGIS, ABS, choropleth]

permalink: /abs-choropleth/
excerpt_separator: <!--more-->
---
Median Weekly income distribution by NSW Suburb
![png](\images\abs-choropleth\NSW_choropleth.png)

<!--more-->

## About

I've been looking at some Australian Census data, and decided to use it as part of a QGIS project.
The data is for *median weekly median household income by suburb* (SSC), taken from the August 2016 Census as part of a GeoPackage. The above image is located around the Sydney area.

This is a **choropleth** - a map that splits an area into multiple subregions, and assigns a color (or other formatting) in relation to a variable's value.

The suburb labels that are shown are high median income (black text white background) and low median income (white text black background). I had to join the suburb names via a separate CSV, which required a basic [python script](\images\abs-choropleth\edit_ssc_code.py) to format the suburb codes the same way.

*Project Goals:* The goal of the project was to see if the income data backs up the intuition that income increases with proximity to city CBDs.

Also, the idea was to use QGIS understand things like ShapeFiles, rules-based labeling, and joins between attribute tables.

## Observations

- In general, there is a noticeable pattern. The closer a suburb is towards a CBD, the higher the income of the suburb becomes. This was the thought behind the visualisation, and it holds mostly true.

### Outliers

#### Low Incomes

- Some areas have a weekly median income of 0. 
  - This could be the null value chosen for missing / insufficient data
  - Some of these areas are national parks. There may be nobody registered as living within those areas. All areas of Australia, as far as I have seen belong to a SSC (suburb identifier).

#### High Incomes outside of CBDs

- mining towns have a much higher income then their surrounding suburbs

## Wider view of all Australia

![png](\images\abs-choropleth\all-aus-chorpoleth.png)