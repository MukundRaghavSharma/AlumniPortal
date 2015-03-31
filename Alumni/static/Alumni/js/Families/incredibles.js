
    google.load("visualization", "1", {packages:["orgchart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');
        data.addRows([
    ['Samiah Akhtar'',''],'
['Arish Gupta'',''],'
['Rona Song'',''],'
['Brian Loo'',''Brian Loo'' ',' ',],
['Linda Min'',''Linda Min'' ',' ',],
['Salman Khoja'',''Salman Khoja'' ',' ',],
['Eric Tang'',''],'
['Alex Voo'',''Alex Voo'' ',' ',],
['Steven Yi'',''Steven Yi'' ',' ',],
['David Leong'',''David Leong'' ',' ',],
['Andrew Yi'',''Andrew Yi'' ',' ',],
['Billy Litner'',''Billy Litner'' ',' ',],
['Bin Yang'',''Bin Yang'' ',' ',],
['Kent Yeung'',''Kent Yeung'' ',' ',],
['Victoria Docherty'',''Victoria Docherty'' ',' ',],
['Hyejoo Kim'',''Hyejoo Kim'' ',' ',],
['Yeonjoo Kim'',''],'
['Stephanie Schneider'',''Stephanie Schneider'' ',' ',],
['Gina Seguiti'',''Gina Seguiti'' ',' ',],
['Yinglu Yao'',''Yinglu Yao'' ',' ',],
['Vince Ye'',''Vince Ye'' ',' ',],
['Arthur Hong'',''Arthur Hong'' ',' ',],
['Elise Lim'',''Elise Lim'' ',' ',],
['Dorothy Yu'',''Dorothy Yu'' ',' ',],
['Christine Pak'',''Christine Pak'' ',' ',],
['Mia Wang'',''Mia Wang'' ',' ',],
['Andrew Gumbs'',''Andrew Gumbs'' ',' ',],

    )];

    var chart = new google.visualization.OrgChar(document.getElementById('chart_div'));
    chart.draw(data, {allowHtml: true, nodeClass:"node"});
    }
    