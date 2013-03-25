xml_reports_merger
==================

for merging xml reports built by internal testing tool

HOW TO USE IT

  this tool found by two files, Mario and Luigi, Luigi do the detect xml reports job, and Mario will generate final xml report depends on Luigi
  
  when you use RIATest do some tests on web, RIATest will logging testing steps into xml file, we call it result_0.xml here,
and then there is possiblities that result_0.xml contains some failed scripts, we usally pick the failed scripts out, and test them again,
when finished, RIATest generate a new report we call it result_1.xml here.

  now we got two xml reports here, they are result_0.xml and result_1.xml, and we need just one report for analysis, so result_0 and result_1 should
be merged to on final version, we name the final version of result_final.xml, that is really what we need.

  before you use this tool, please make sure python2.7 up already installed.
  
  assume that, result_0 and result_1 under C:\xml_reports, copy this project into this path, and type the commands below:
  
  python ui.py -i result_1.xml result_0.xml -o result_final.xml
  
  P.S. (1)make sure there is no duplicated file named result_final.xml in the path
       (2)newer file always be merged into elder one.

