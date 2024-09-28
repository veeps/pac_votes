---
title: "PAC Contributions"
output: 
  html_document:
    keep_md: true
date: "2024-09-28"
---



## Exploring Insurance PAC Contributions

Exploring contribution data on the following insurance PACS: Humana, CVS Aetna, Elevance, United Health, HCSC, Centene. This explores data from 1992 to 2024. In total, $28.5M has been contributed to candidates - 56% to Republicans and 43.6% to Democrats. Throughout the years, Elevance has contributed the most amount of money to candidates. I'll have to understand this value more, but 8.5M over the last 32 years doesn't seem like that much money to me.



|PAC           |TOTAL     |
|:-------------|:---------|
|Elevance      |8,498,429 |
|United Health |7,860,825 |
|Humana        |5,474,533 |
|CVS Aetna     |3,372,700 |
|Centene       |1,779,071 |
|HCSC          |1,567,700 |

## Contributions by Party Affiliation
Here's a quick breakdown to see how each insurance PAC contributes by party affiliation. It looks like most of the PACS are pretty evenly split with their contributions. Elevance and United Health has contributed more to Republican candidates. 


![](pac_eda_files/figure-html/affiliation-1.png)<!-- -->

## Yearly PAC Contributions

Here's how much each PAC has contributed over the years. We see that Elevance has been making more contributions over the years, but United Health has started contributing more since 2011. Curious if the passing of Obamacare has anything to do with that.



```{=html}
<div class="plotly html-widget html-fill-item-overflow-hidden html-fill-item" id="htmlwidget-c2104769289926dae5a1" style="width:672px;height:480px;"></div>
<script type="application/json" data-for="htmlwidget-c2104769289926dae5a1">{"x":{"visdat":{"12da56f0413ea":["function () ","plotlyVisDat"]},"cur_data":"12da56f0413ea","attrs":{"12da56f0413ea":{"x":{},"y":{},"legendgroup":{},"mode":"lines","showlegend":true,"opacity":1,"color":{},"alpha_stroke":1,"sizes":[10,100],"spans":[1,20],"type":"scatter"}},"layout":{"width":900,"margin":{"b":40,"l":60,"t":25,"r":10},"title":"Annual PAC Contributions to Candidates","yaxis":{"domain":[0,1],"automargin":true,"title":"Total Contributions"},"xaxis":{"domain":[0,1],"automargin":true,"title":"Year"},"hovermode":"closest","showlegend":true},"source":"A","config":{"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false},"data":[{"x":[2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024],"y":[121500,400500,312250,234250,162000,205000,292200,332000,513000,489500,310500],"legendgroup":"CVS Aetna","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"CVS Aetna","marker":{"color":"rgba(252,141,98,1)","line":{"color":"rgba(252,141,98,1)"}},"textfont":{"color":"rgba(252,141,98,1)"},"error_y":{"color":"rgba(252,141,98,1)"},"error_x":{"color":"rgba(252,141,98,1)"},"line":{"color":"rgba(252,141,98,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[2006,2008,2010,2012,2014,2016,2018,2020,2022,2024],"y":[27250,53600,67800,75750,96600,151200,220071,351800,504000,231000],"legendgroup":"Centene","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"Centene","marker":{"color":"rgba(102,194,165,1)","line":{"color":"rgba(102,194,165,1)"}},"textfont":{"color":"rgba(102,194,165,1)"},"error_y":{"color":"rgba(102,194,165,1)"},"error_x":{"color":"rgba(102,194,165,1)"},"line":{"color":"rgba(102,194,165,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024],"y":[20150,56950,71850,112500,190000,215000,331400,430580,559500,692999,791000,777250,790750,727000,820500,1080500,830500],"legendgroup":"Elevance","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"Elevance","marker":{"color":"rgba(141,160,203,1)","line":{"color":"rgba(141,160,203,1)"}},"textfont":{"color":"rgba(141,160,203,1)"},"error_y":{"color":"rgba(141,160,203,1)"},"error_x":{"color":"rgba(141,160,203,1)"},"line":{"color":"rgba(141,160,203,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[2010,2012,2014,2016,2018,2020,2022,2024],"y":[78200,173000,250000,272000,271000,197000,178500,148000],"legendgroup":"HCSC","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"HCSC","marker":{"color":"rgba(231,138,195,1)","line":{"color":"rgba(231,138,195,1)"}},"textfont":{"color":"rgba(231,138,195,1)"},"error_y":{"color":"rgba(231,138,195,1)"},"error_x":{"color":"rgba(231,138,195,1)"},"line":{"color":"rgba(231,138,195,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024],"y":[1500,15950,12650,26512,76925,160418,150999,197107,331550,638672,618000,485750,710500,552000,497500,599500,399000],"legendgroup":"Humana","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"Humana","marker":{"color":"rgba(166,216,84,1)","line":{"color":"rgba(166,216,84,1)"}},"textfont":{"color":"rgba(166,216,84,1)"},"error_y":{"color":"rgba(166,216,84,1)"},"error_x":{"color":"rgba(166,216,84,1)"},"line":{"color":"rgba(166,216,84,1)"},"xaxis":"x","yaxis":"y","frame":null},{"x":[1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024],"y":[4000,20850,41700,65500,227350,185000,261125,336000,377000,413200,452000,658000,1026000,1036500,1185100,1065000,506500],"legendgroup":"United Health","mode":"lines","showlegend":true,"opacity":1,"type":"scatter","name":"United Health","marker":{"color":"rgba(255,217,47,1)","line":{"color":"rgba(255,217,47,1)"}},"textfont":{"color":"rgba(255,217,47,1)"},"error_y":{"color":"rgba(255,217,47,1)"},"error_x":{"color":"rgba(255,217,47,1)"},"line":{"color":"rgba(255,217,47,1)"},"xaxis":"x","yaxis":"y","frame":null}],"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.2,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":[]}</script>
```

## Candidates That Have Received the Most Money

Here are the top 20 candidates who have received the most money from insurance PACS in the last 16 years (since 2008). 


|CAND_NAME                       |TOTAL   |affiliation |office |state |
|:-------------------------------|:-------|:-----------|:------|:-----|
|MCCARTHY, KEVIN                 |231,238 |REP         |H      |CA    |
|HOYER, STENY HAMILTON           |229,500 |DEM         |H      |MD    |
|GUTHRIE, STEVEN BRETT           |225,500 |REP         |H      |KY    |
|SCALISE, STEPHEN JOSEPH "STEVE" |199,500 |REP         |H      |LA    |
|BRADY, KEVIN PATRICK            |181,500 |REP         |H      |TX    |
|PALLONE, FRANK JR               |181,500 |DEM         |H      |NJ    |
|NEAL, RICHARD E                 |178,000 |DEM         |H      |MA    |
|KUSTER, ANN MCLANE              |163,000 |DEM         |H      |NH    |
|KIND, RONALD JAMES              |161,500 |DEM         |H      |WI    |
|LAHOOD, DARIN MCKAY             |160,000 |REP         |H      |IL    |
|BERA, AMERISH                   |159,000 |DEM         |H      |CA    |
|SHIMKUS, JOHN M                 |151,500 |REP         |H      |IL    |
|SMITH, JASON T                  |150,171 |REP         |H      |MO    |
|RYAN, PAUL D                    |148,500 |REP         |H      |WI    |
|SCHRADER, KURT                  |146,000 |DEM         |H      |OR    |
|BILIRAKIS, GUS M                |145,500 |REP         |H      |NA    |
|CARDENAS, TONY                  |143,000 |DEM         |H      |CA    |
|PETERS, SCOTT                   |136,000 |DEM         |H      |CA    |
|MCMORRIS RODGERS, CATHY         |135,500 |REP         |H      |WA    |
|ROSKAM, PETER                   |133,000 |REP         |H      |IL    |
